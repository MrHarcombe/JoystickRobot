import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

fwdleft = 22
fwdright = 18

revleft = 17
revright = 23

motors = [fwdleft,fwdright,revleft,revright]

for item in motors:
	GPIO.setup(item, GPIO.OUT)

def forward(power=100):
	GPIO.output(fwdright, True)
	GPIO.output(fwdleft, True)

def right(power=100):
	GPIO.output(revright, True)
	GPIO.output(fwdleft, True)

def left(power=100):
	GPIO.output(fwdright, True)
	GPIO.output(revleft, True)

def reverse(power=100):
	GPIO.output(revleft, True)
	GPIO.output(revright, True)

def stop():
	GPIO.output(revleft, False)
	GPIO.output(revright, False)
	GPIO.output(fwdright, False)
	GPIO.output(fwdleft, False)

try:
	print("R E A D Y")
except KeyboardInterrupt:
	print("E X I T")
	GPIO.cleanup()
        #