import servo
import time

def left():
	time.sleep(.5)
	servo.move(3,0)

def right():
	time.sleep(.5)
	servo.move(3,10)

def mid():
	time.sleep(.5)	
	servo.move(3,5)


