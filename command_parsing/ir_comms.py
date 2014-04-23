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


# def trigger_read():    
#     while dataQ.qsize() > 0:
#         a = dataQ.get(timeout=1)
#         if len(a) > 1:
#             lines.append("{}: {}".format(a[0], str(a[1]).strip()))



##### command sending dispatcher
command_q = Queue.Queue(maxsize=2)
def command_sender():
    while True:
        item = command_q.get() #blocking call        
        # TODO try twice/check confirmation?
        try:
            print item.run_action()     
            print "Command sent"       
        except Exception as e:
            msg = "Error send: {}".format(e)
            print msg
        # wait between issuing commands
        time.sleep(5)

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
        except Exception as e:
            msg = "Error receive: {}".format(e)
            print msg


##### web routing
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# send stuff
# http://127.0.0.1:8080/send_command/23/HEAT/4/0
# http://127.0.0.1:8080/send_command/23/HEAT/4/1
@route('/send_command/<temp>/<mode>/<fan_speed>/<power_toggle>')
def send_stuff(temp, mode, fan_speed, power_toggle):
    params = temp, mode, fan_speed, power_toggle    
    command = IRCommandWrapper(params)
    command_q.put(command)    
    return "Enqueued: {} {} {} {}".format(int(temp), mode, int(fan_speed), power_toggle)  




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


class IRCommandWrapper(object):    
    
    def __init__(self, params):
        self.params = params
    
    def send_stuff(self):
        temp, mode, fan_speed, power_toggle = self.params
        # def construct_command_part(temperature, mode, fan_speed, power_toggle):  
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
            print pulses
            # repeat if not power toggle
            if not power_toggle:
                time.sleep(3)
                send_pulses(ser, pulses)        
            return "SENT: {} {} {} {}".format(int(temp), mode, int(fan_speed), power_toggle)  
        except (ValueError, KeyError):
            return "Malformed input."
    
    def run_action(self):        
        return self.send_stuff()



if __name__=="__main__":    
    
    
    port = "/dev/ttyACM0"
    dataQ = Queue.Queue(maxsize=100)
    errQ = Queue.Queue(maxsize=100)
    ser = IRSerialCommunicator(dataQ, errQ, port=port, baudrate=9600)
    ser.daemon = True
    ser.start()
    
    # start command dispatcher    
    num_worker_threads = 1
    for i in range(num_worker_threads):
         t = threading.Thread(target=command_sender)
         t.daemon = True
         t.start()
         t = threading.Thread(target=command_reader)
         t.daemon = True
         t.start()
    
    # run webserver
    # run(server='cherrypy', host='0.0.0.0', port=8080)
    run(host='0.0.0.0', port=8080)


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
