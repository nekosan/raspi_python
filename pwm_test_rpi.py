import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)

p.start(0)

try:
	while True:
		for i in range(0, 99):
			p.ChangeDutyCycle(i)
			time.sleep(0.01)
		for i in range(100, 1, -1):
			p.ChangeDutyCycle(i)
			time.sleep(0.01)


except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

