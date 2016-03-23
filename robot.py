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

pfl = GPIO.PWM(fwdleft, 50)
pfr = GPIO.PWM(fwdright, 50)
prl = GPIO.PWM(revleft, 50)
prr = GPIO.PWM(revright, 50)
pfl.start(0)
pfr.start(0)
prl.start(0)
prr.start(0)

def right(power=100):
  if power > 0:
      prl.ChangeDutyCycle(power)
  else:
      pfl.ChangeDutyCycle(-power)

def left(power=100):
  if power > 0:
      prr.ChangeDutyCycle(power)
  else:
      pfr.ChangeDutyCycle(-power)

def stop():
  pfl.ChangeDutyCycle(0)
  pfr.ChangeDutyCycle(0)
  prl.ChangeDutyCycle(0)
  prr.ChangeDutyCycle(0)

try:
	print("R E A D Y")
except KeyboardInterrupt:
	print("E X I T")
	GPIO.cleanup()
