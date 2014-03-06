import serial
import json
import random

import threading, Queue

import logging
"""
logging.basicConfig(filename=__file__.replace('.py','.log'),level=logging.DEBUG,format='%(asctime)s [%(name)s.%(funcName)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='a')
"""

# from http://stackoverflow.com/questions/18752980/reading-serial-data-from-arduino-with-python
class maxSonarSerialThread(threading.Thread):
  def __init__(self, dataQ, errQ, port=None, baudrate=None):
    self.logger = logging.getLogger('sonarSerialThread')
    self.logger.debug('initializing')
    threading.Thread.__init__(self)
    self.ser = serial.Serial()
    self.ser.timeout = 1
    if port is None:
      self.ser.port = "/dev/tty.usbserial-A6004amR"
    else:
      self.ser.port = port
    if baudrate is None:
      self.baudrate = 115200
    else:
      self.baudrate = baudrate
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
    self.logger.debug('running')
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
          #some sanity check

    if self.readCount >= self.waitMaxSec:
        self.logger.debug('Unable to read from MaxSonar...')
        self.close()
        return False
    else:
      self.logger.debug('MaxSonar data is streaming...')

    return True

  def isOpen(self):
    self.logger.debug('Open? ' + str(self.ser.isOpen()))
    return self.ser.isOpen()

  def open(self):
    self.ser.open()

  def stopDataAquisition(self):
    self.logger.debug('Falsifying keepAlive')
    self.keepAlive = False

  def close(self):
    self.logger.debug('closing')
    self.stopDataAquisition()
    self.ser.close()

  def write(self, msg):
    self.ser.write(msg)

  def readline(self):
    return self.ser.readline()


port = "/dev/tty.usbmodem1421"
dataQ = Queue.Queue()
errQ = Queue.Queue()
ser = maxSonarSerialThread(dataQ, errQ, port=port)
ser.daemon = True
ser.start()



while dataQ.qsize() > 0:
    a = dataQ.get(timeout=1)
    print str(a)





import struct
def packIntegerAsShort(value):
    """Packs a python 2 byte arduino int"""
    return struct.pack('h', value)    #should check bounds

ser.write(packIntegerAsShort(250))




array_send = [277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 277, 284, 89, 97, 89, 191, 183, 191, 89, 97, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 97, 89, 191, 183, 97, 370, 0]


ser.write(packIntegerAsShort(1313))
for el in array_send+array_send:
    ser.write(packIntegerAsShort(el))
ser.write(packIntegerAsShort(1414))


ser.write(packIntegerAsShort(110))


a = dataQ.get(timeout=2)


# http://stackoverflow.com/questions/8730927/convert-python-long-int-to-fixed-size-byte-array
def base256_encode(n, minwidth=0): # int/long to byte array
    if n > 0:
        arr = []
        while n:
            n, rem = divmod(n, 256)
            arr.append(rem)
        b = bytearray(reversed(arr))
    elif n == 0:
        b = bytearray(b'\x00')
    else:
        raise ValueError

    if minwidth > 0 and len(b) < minwidth: # zero padding needed?
        b = (minwidth-len(b)) * '\x00' + b
    return b


a = dataQ.get(timeout=2)
print str(a)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/distance")
def distance():
  distance = read_distance_from_serial()
  return json.dumps({'distance': distance})

def read_distance_from_serial():
  a = dataQ.get()
  print str(a)
  return a