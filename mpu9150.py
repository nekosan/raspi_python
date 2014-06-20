import smbus
import time

bus = smbus.SMBus(1)
address = 0x68

class Mpu9150:
	def write(self, reg, value):
		self.bus.write_byte_data(self.address, reg, value)
		return -1

	def read(self, reg):
		value = self.bus.read_byte_data(self.address, reg)
		return value 
	
	def __init__(self):
		self.bus = smbus.SMBus(1)	
		self.address = 0x68
		self.acc = [0, 0, 0]
		self.gyr = [0, 0, 0]

		self.write(0x6b, 0x00)
		self.write(0x37, 0x02)
		self.write(0x1a, 0x02)

	def getdata(self):
		self.acc[0] = self.read(0x3b) << 8
		self.acc[0] += self.read(0x3c)
		self.acc[1] = self.read(0x3d) << 8
		self.acc[1] += self.read(0x3e)
		self.acc[2] = self.read(0x3f) << 8
		self.acc[2] += self.read(0x40)



if __name__ == '__main__':
	mpu = Mpu9150()
	
	while True:
		mpu.getdata()	
		print mpu.acc[0]
		time.sleep(1.0)
