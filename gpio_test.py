import wiringpi
import time

if __name__ == '__main__':
	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)
	io.pinMode(18, io.OUTPUT)
	io.digitalWrite(18, io.HIGH)
	while True:
		io.digitalWrite(18, io.LOW)
		time.sleep(0.5)
		io.digitalWrite(18, io.HIGH)
		time.sleep(0.5)
