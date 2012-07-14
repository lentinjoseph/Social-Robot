import servo
import time

def left():
	time.sleep(1)
	servo.move(4,35)
def leftmid():
	time.sleep(1)
	servo.move(4,50)
def mid():
	time.sleep(1)
	servo.move(4,66)

def rightmid():
	time.sleep(1)
	servo.move(4,80)
def right():
	time.sleep(1)
	servo.move(4,90)

def lsearch():
	right()
	rightmid()
	mid()
	leftmid()
	left()

def rsearch():
	left()
	leftmid()
	mid()
	rightmid()
	right()
	
