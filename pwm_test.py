import wiringpi
import time

pin = 1

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
io.pinMode(pin, io.PWM_OUTPUT)

while True:
	count = 0
	while count < 1000:
		io.pwmWrite(pin, count)
		count += 10
		time.sleep(0.05)
	
