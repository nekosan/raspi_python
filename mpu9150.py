import smbus
import time
import math as M

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
        self.acc_scale = 2.0
        self.address = 0x68
        self.acc = [0, 0, 0]
        self.gyr = [0, 0, 0]
        self.gyr_offset = [0.0, 0.0, 0.0]

        self.write(0x6b, 0x00)
        self.write(0x37, 0x02)
        self.write(0x1a, 0x02)

    def set_gyr_offset(self):
        self.gyr_offset[0] = self.read(0x43) << 8
        self.gyr_offset[0] += self.read(0x44)
        self.gyr_offset[1] = self.read(0x45) << 8
        self.gyr_offset[1] += self.read(0x46)
        self.gyr_offset[2] = self.read(0x47) << 8
        self.gyr_offset[2] += self.read(0x48)
        for i in range(len(self.gyr_offset)) :
            if self.gyr_offset[i] >= 32768:
                self.gyr_offset[i] -= 65536
            self.gyr_offset[i] = float(self.gyr_offset[i])


    def getdata_acc(self):
        self.acc[0] = self.read(0x3b) << 8
        self.acc[0] += self.read(0x3c)
        self.acc[1] = self.read(0x3d) << 8
        self.acc[1] += self.read(0x3e)
        self.acc[2] = self.read(0x3f) << 8
        self.acc[2] += self.read(0x40)
        for i in range(len(self.acc)) :
            if self.acc[i] >= 32768:
                self.acc[i] -= 65536
            self.acc[i] = float(self.acc[i])

    def getdata_gyr(self):
        self.gyr[0] = self.read(0x43) << 8
        self.gyr[0] += self.read(0x44)
        self.gyr[1] = self.read(0x45) << 8
        self.gyr[1] += self.read(0x46)
        self.gyr[2] = self.read(0x47) << 8
        self.gyr[2] += self.read(0x48)
        for i in range(len(self.gyr)) :
            if self.gyr[i] >= 32768:
                self.gyr[i] -= 65536
            self.gyr[i] = float(self.gyr[i]) - self.gyr_offset[i]

    def calc_acc_deg(self):
        acc_deg = []
        try:
            acc_deg.append(M.asin(self.acc[0] / M.sqrt(self.acc[0] ** 2 + self.acc[2] ** 2)) * (180.0 / M.pi))
            acc_deg.append(M.asin(self.acc[1] / M.sqrt(self.acc[1] ** 2 + self.acc[2] ** 2)) * (180.0 / M.pi))
        except ZeroDivisionError:
            return 1
        else :
            return acc_deg

if __name__ == '__main__':
    mpu = Mpu9150()

    mpu.set_gyr_offset()
    print 'Get gyro offset value.'
    while True:
        mpu.getdata_acc()
        mpu.getdata_gyr()
        for i in range(3):
            print str(mpu.acc[i]) + ' ' + str(mpu.gyr[i])
        print mpu.calc_acc_deg()
        time.sleep(0.2)
