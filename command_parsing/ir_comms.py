import serial
import json
import random
import time
import datetime
import threading, Queue
import logging
import struct
import collections

from bottle import route, run, template
import IR_functions as irfun
import time
import logging

"""
logging.basicConfig(filename=__file__.replace('.py','.log'),level=logging.DEBUG,format='%(asctime)s [%(name)s.%(funcName)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')
"""

# from http://stackoverflow.com/questions/18752980/reading-serial-data-from-arduino-with-python
class IRSerialCommunicator(threading.Thread):
    def __init__(self, dataQ, errQ, port, baudrate=115200):
        self.logger = logging.getLogger('IRSerialCommunicator')
        self.logger.debug('initializing')
        threading.Thread.__init__(self)
        self.ser = serial.Serial(port, baudrate)
        self.ser.timeout = 1
        #self.ser.flushInput()
        self.readCount = 0
        self.sleepDurSec = 5
        self.waitMaxSec = self.sleepDurSec * self.ser.baudrate / 10
        self.dataQ = dataQ
        self.errQ = errQ
        self.keepAlive = True
        self.stoprequest = threading.Event()
        self.setDaemon(True)
        self.dat = None
        self.inputStarted = False
        self.ver = 0.1

    def run(self):
        self.logger.debug('Serial reader running')
        dataIn = False
        while not self.stoprequest.isSet():
          if not self.isOpen():
            self.connectForStream()

          while self.keepAlive:
            dat = self.ser.readline()
            # some data validation goes here before adding to Queue...
            if len(dat) > 2:
                self.dataQ.put([time.time(), dat])
            if not self.inputStarted:
                self.logger.debug('reading')
            self.inputStarted = True
          self.dat.close()
          self.close()
          self.join_fin()

    def join_fin(self):
        self.logger.debug('stopping')
        self.stoprequest.set()

    def isOpen(self):
        self.logger.debug('Open? ' + str(self.ser.isOpen()))
        return self.ser.isOpen()

    def open(self):
          self.ser.open()

    def stopDataAquisition(self):
        self.logger.debug('Setting keepAlive to False')
        self.keepAlive = False

    def close(self):
        self.logger.debug('closing')
        self.stopDataAquisition()
        self.ser.close()

    def write(self, msg):
        self.ser.write(msg)

    def readline(self):
        return self.ser.readline()

    def connectForStream(self, debug=True):
        '''Attempt to connect to the serial port and fail after waitMaxSec seconds'''
        self.logger.debug('connecting')
        if not self.isOpen():
          self.logger.debug('not open, trying to open')
          try:
            self.open()
          except serial.serialutil.SerialException:
            self.logger.debug('Unable to use port ' + str(self.ser.port) + ', please verify and try again')
            return
        while self.readline() == '' and self.readCount < self.waitMaxSec and self.keepAlive:
            self.logger.debug('reading initial')
            self.readCount += self.sleepDurSec
            if not self.readCount % (self.ser.baudrate / 100):
              self.logger.debug("Verifying MaxSonar data..")
              #//some sanity check

        if self.readCount >= self.waitMaxSec:
            self.logger.debug('Unable to read from MaxSonar...')
            self.close()
            return False
        else:
          self.logger.debug('MaxSonar data is streaming...')

        return True

# sending-specific functions
def packIntegerAsShort(value):
    """Packs a python 2 byte arduino int"""
    return struct.pack('h', value)    #should check bounds





# TODO make this thread-safe, add commands to queue etc.
def send_pulses(ser, pulses):
    packet_start = 1313
    packet_end   = 1414
    ser.write(packIntegerAsShort(packet_start))
    for el in pulses:
        ser.write(packIntegerAsShort(el))
    ser.write(packIntegerAsShort(1414))


##### command sending dispatcher
from collections import deque
command_q = deque(maxlen=2)
def command_sender():
    while True:        
        # queue fetching 
        while True:
            try:
                item = command_q.pop() #non-blocking call                       
                break # break out of the fetching loop, we have item
            except IndexError:
                # wait for tiny bit between checking
                time.sleep(0.1)
                # continue
                continue
        # TODO try twice/check confirmation?
        try:
            logging.info(item.run_action())
            logging.debug("Command sent")
        except Exception as e:
            msg = "Error send: {}".format(e)
            logging.warn(msg)
            logging.exception(e)
        # wait between issuing commands
        time.sleep(5)



# defaults for readings/state
current_state = {
    "temp" :        "22",       # from last command sent
    "power_toggle": "1", # from last command sent
    "mode":         "AUTO",
    "fan_speed":    "4",
    # now stuff from sensors
    "state_onoff": False,  # calculated property from sensors
    "state_standby": False,  # calculated property from sensors    
    "L0" : "0", # reference
    "L1" : "0", # operation - on/off
    "L2" : "0", # standy   
    "L3" : "0", # ambient  
    # computed state
    "operational_state" : 3,
    "last_success_reading" : 0,
}

# prevent concurrent modification of the dictionary
state_lock = threading.Lock()
def set_state(temp, mode, fan_speed, power_toggle):
    with state_lock:
        current_state["temp"] = temp
        current_state["mode"] = mode
        current_state["fan_speed"] = fan_speed
        current_state["power_toggle"] = power_toggle
        current_state["timestamp"] = time.time()
    
    
LIGHT_DIFF = 100 #TODO move to config
TIMEOUT_SECONDS = 10 #when is reading considered stale
def determine_state():
    ref     = int(current_state["L0"])
    on_off  = int(current_state["L1"])
    standby = int(current_state["L2"])
    
    with state_lock:
        # is the A/C running?
        if on_off - ref > LIGHT_DIFF:
            current_state["state_onoff"] = True
        else:
            current_state["state_onoff"] = False
        
        if standby - ref > LIGHT_DIFF:
            current_state["state_standby"] = True
        else:
            current_state["state_standby"] = False
    
        # determine operational state    
        since_last = time.time() - current_state["last_success_reading"]
        if since_last > TIMEOUT_SECONDS:
            current_state["operational_state"] = 3
        elif current_state["state_onoff"] and current_state["state_standby"]:
            current_state["operational_state"] = 2
        elif current_state["state_standby"]:
            current_state["operational_state"] = 1
        else:
            current_state["operational_state"] = 0

def determine_state_loop():
    logging.info("Command")
    while True:
        try:            
            determine_state()
            # wait 0.5s
            time.sleep(0.5)
                
        except Exception as e:
            msg = "Error determining state: {}".format(e)
            logging.warn(msg)
            logging.exception(e)

# 
t = threading.Thread(target=determine_state_loop)
t.daemon = True
t.start()


# operational states representation
operational_states = {
    0   : "Off",
    1   : "Standby",
    2   : "In operation",
    3   : "Error/could not determine",
}



##### command receiving processing
lines = collections.deque(maxlen=50)
def command_reader():
    while True:
        try:
            a = dataQ.get()
            if len(a) > 1:
                d_time = datetime.datetime.fromtimestamp(a[0])
                time_formatted = d_time.strftime('%H:%M:%S')
                lines.append("{}: {}".format(time_formatted, str(a[1]).strip()))
                
                # now parse the command:
                text_contents = a[1]
                readings = text_contents.split(";")
                for reading in readings:
                    try:
                        key, val = reading.split(":")
                        with state_lock:
                            current_state[key] = val.strip()
                            # mark last reading
                            current_state["last_success_reading"] = time.time()
                    except ValueError:
                        # invalid combination, ignore..
                        continue
                
                
        except Exception as e:
            msg = "Error receive: {}".format(e)            
            logging.warn(msg)
            logging.exception(e)


##### web routing
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

import json
@route('/json_info')
def json_out():    
    return json.dumps(current_state)

# lock to represent manipulation of power state,
# wait with any other
power_toggle_lock = threading.Lock()

# send stuff
# http://127.0.0.1:8080/send_command/23/HEAT/4
# http://127.0.0.1:8080/send_command/23/HEAT/4
@route('/send_command/<temp>/<mode>/<fan_speed>')
def send_stuff(temp, mode, fan_speed, power_toggle=False):
    # make sure we do not enqueue other stuff
    try:
        params = temp, mode, fan_speed, power_toggle    
        command = GenericIRCommandWrapper(params)
        # append while discarding prev items
        command_q.append(command)    
        return "OK: Enqueued {} {} {}".format(
            int(temp), mode, int(fan_speed))  
    except Exception, e:
        return "ERR: {} {} {} {}".format(
            str(e), int(temp), mode, int(fan_speed))


@route('/set_full_state/<temp>/<mode>/<fan_speed>/<desired_state>')
def set_full_state(temp, mode, fan_speed, desired_state):
    try:
        params = temp, mode, fan_speed, desired_state    
        command = PowerIRCommandWrapper(params)
        # append while discarding prev items
        command_q.append(command)
        return "OK: Enqueued {} {} {} {}".format(
            int(temp), mode, int(fan_speed), desired_state)  
    except Exception, e:
        return "ERR: {} {} {} {} {}".format(
            str(e), int(temp), mode, int(fan_speed), desired_state)
    send_stuff(temp, mode, fan_speed)
    time.sleep(2)
    return set_power(desired_state)
    

@route('/set_power/<desired_state>')
def set_power(desired_state):    
    raise Exception("Deprecated function")    


output_template = """<html>
    <head>
        <meta name="author" content="Petr">
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="2">
    </head>
    <body>
        <pre>{}</pre>
    </body>
</html>
"""

@route('/read')
def read_out():
    # trigger_read()
    return output_template.format("\n".join(list(lines)[::-1]))


def get_time_formatted():
    d_time = datetime.datetime.fromtimestamp(time.time())
    time_formatted = d_time.strftime('%H:%M:%S')
    return time_formatted



class GenericIRCommandWrapper(object):    
    """Wrapper for commands to be enqueued"""
    def __init__(self, params):
                
        temp, mode, fan_speed, power_var = params  
        try:
            if int(temp) < 16 or int(temp) > 30:
                raise TypeError("Invalid temperature")
            
            if str(mode) not in ["HEAT",  "COOL",  "AUTO",  "FAN" ,  "DEHUM"]:
                raise TypeError("Invalid mode")

            if int(fan_speed) not in [1, 2, 3, 4]:
                raise TypeError("Invalid fan speed")

            if str(power_var) not in ["0", "1"]:
                raise TypeError("Invalid power/toggle state")
            
        except ValueError:
            raise TypeError("Invalid parameters")
        
        # all good!        
        self.params = params
    
    def send_stuff(self):
        temp, mode, fan_speed, power_toggle = self.params
        
        try:
            power_toggle = True if power_toggle == '1' else False
            command = irfun.construct_full_command(
                int(temp), 
                mode,
                int(fan_speed),
                power_toggle
            )
            pulses = irfun.arduino_flat_array(command)        
            # send once
            send_pulses(ser, pulses)                                              
            logging.debug(pulses)
            # repeat if not power toggle
            if not power_toggle:
                time.sleep(3)
                send_pulses(ser, pulses)        
            
            # store state
            set_state(*self.params)
            msg = "SENT: {} {} {} {}".format(int(temp), mode, int(fan_speed), power_toggle)  
            lines.append("{}: {}".format(get_time_formatted(), msg))
            return msg
        except (ValueError, KeyError):
            msg = "ERR: Malformed input {} {} {} {}".format(int(temp), mode, int(fan_speed), power_toggle)  
            lines.append("{}: {}".format(get_time_formatted(), msg))
            return msg
    
    def run_action(self):        
        return self.send_stuff()


class PowerIRCommandWrapper(GenericIRCommandWrapper):
    """Used to set power to the A/C unit"""
    
    def send_stuff(self):
        
        temp, mode, fan_speed, desired_state = self.params
        
        """Overrides normal send stuff"""
        desired_state = True if str(desired_state) == "1" else False
    
        # TODO - move this to the command sender?
        if current_state["operational_state"] > 2:            
            msg = "ERR: Not in operation"
            lines.append("{}: {}".format(get_time_formatted(), msg))
            return msg
        
        toggle_power = True
        # we are in operation, but do we need to toggle power?
        if desired_state and current_state["operational_state"] == 2:
            msg = "OK: Already ON"    
            lines.append("{}: {}".format(get_time_formatted(), msg))
            toggle_power = False
            
        elif not desired_state and current_state["operational_state"] == 1:
            msg = "OK: Already OFF" 
            lines.append("{}: {}".format(get_time_formatted(), msg))
            toggle_power = False
        
        if not toggle_power:
            # convert desired state to power toggle
            power_toggle = "0"
            params = temp, mode, fan_speed, power_toggle   
            self.params = params
            return super(PowerIRCommandWrapper, self).send_stuff()                        
            
        else:
            # let's try to send ON command
            NO_ATTEMPTS = 3         # number of re-send attempts
            NO_WAITS = 2            # how many times to wait and check
        
            # proceed to sending
            for i in range(NO_ATTEMPTS):            
                # send stuff
                power_toggle = "1"                
                params = temp, mode, fan_speed, power_toggle   
                self.params = params
                
                # TODO - get return state of this
                super(PowerIRCommandWrapper, self).send_stuff()

                # wait for the system to update itself
                time.sleep(2.5)

                # check a few times if all went well
                for _ in range(NO_WAITS):
                    if desired_state \
                        and current_state["operational_state"] == 2:
                        msg = "OK: Switched ON"
                        lines.append("{}: {}".format(get_time_formatted(), msg))
                        return msg
                    elif not desired_state \
                        and current_state["operational_state"] == 1:     
                        msg = "OK: Switched OFF"
                        lines.append("{}: {}".format(get_time_formatted(), msg))
                        return msg       
                    # wait between checking again
                    time.sleep(2)

                # wait between send attempts
                time.sleep(6)
            # if
            return "ERR: Not able to action command"

if __name__=="__main__":    

    # TODO make this configurable    
    port = "/dev/ttyACM0"
    dataQ = Queue.Queue(maxsize=100)
    errQ = Queue.Queue(maxsize=100)
    ser = IRSerialCommunicator(dataQ, errQ, port=port, baudrate=9600)


    mock_serial = False
    if mock_serial:
        import os, pty, serial
        master, slave = pty.openpty()
        s_name = os.ttyname(slave)
        ser = IRSerialCommunicator(dataQ, errQ, port=s_name, baudrate=9600)
    else:
        ser = IRSerialCommunicator(dataQ, errQ, port=port, baudrate=9600)
    ser.daemon = True
    ser.start()
    
    
    # start command dispatcher    
    sender = threading.Thread(target=command_sender)
    sender.daemon = True
    sender.start()
    reader = threading.Thread(target=command_reader)
    reader.daemon = True
    reader.start()

    # run webserver, multi threaded, world-accessible
    run(server='cherrypy', host='0.0.0.0', port=8080)
    # run(host='0.0.0.0', port=8080)



"""


ser.write(packIntegerAsShort(250))




array_send = [277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 370, 0]


packet_start = 1313
packet_end   = 1414
ser.write(packIntegerAsShort(packet_start))
for el in array_send+array_send:
    ser.write(packIntegerAsShort(el))
ser.write(packIntegerAsShort(1414))


ser.write(packIntegerAsShort(110))


a = dataQ.get(timeout=2)
"""
