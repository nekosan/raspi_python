import smbus
import time

bus = smbus.SMBus(1)
address = 0x68

def write(value):
	bus.write_byte_data(address, 0, value)
	return -1

def read(reg):
	value = bus.read_byte_data(address, reg)
	return value 


while True:
	time.sleep(1)
	v = read(0x75)
	print v
