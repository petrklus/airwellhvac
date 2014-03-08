import serial
import json
import random
import time
import threading, Queue
import logging
import struct

from bottle import route, run, template
import IR_functions as irfun



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
            self.dataQ.put(dat)
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


def send_pulses(ser, pulses):
    packet_start = 1313
    packet_end   = 1414
    ser.write(packIntegerAsShort(packet_start))
    for el in pulses:
        ser.write(packIntegerAsShort(el))
    ser.write(packIntegerAsShort(1414))


import collections
lines = collections.deque(maxlen=50)
def trigger_read():    
    while dataQ.qsize() > 0:
        a = dataQ.get(timeout=1)
        if len(a) > 1:
            lines.append(str(a).strip())


# bottle functions and definiti
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# example: 
@route('/send_command/<temp>/<mode>/<fan_speed>/<power_toggle>')
def send_stuff(temp, mode, fan_speed, power_toggle):
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
        
        # repeat
        if not power_toggle:
            time.sleep(0.05)
            send_pulses(ser, pulses)
        
        return "SENT: {} {} {} {}".format(int(temp), mode, int(fan_speed), power_toggle)  
    except (ValueError, KeyError):
        return "Malformed input."


    # ...

@route('/read')
def read_out():
    trigger_read()
    return "\n".join(lines)

if __name__=="__main__":    
    port = "/dev/tty.usbmodem1421"
    dataQ = Queue.Queue(maxsize=100)
    errQ = Queue.Queue(maxsize=100)
    ser = IRSerialCommunicator(dataQ, errQ, port=port, baudrate=115200)
    ser.daemon = True
    ser.start()
    
        
    run(host='localhost', port=8080)


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
