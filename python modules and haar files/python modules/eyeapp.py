import servo
import time

def down():
	time.sleep(.5)
	servo.move(7,5)

def mdown():
	time.sleep(.5)
	servo.move(7,20)

def mid():
	time.sleep(.5)
	servo.move(7,50)

def mup():
	time.sleep(.5)
	servo.move(7,60)

def up():
	time.sleep(.5)
	servo.move(7,70)

def btop():
	down()
	time.sleep(.5)
	mdown()
	time.sleep(.5)
	mid()
	time.sleep(.5)
	mup()
	time.sleep(.5)
	up()
	
def topb():
	up()
	time.sleep(.5)
	mup()
	time.sleep(.5)
	mid()
	time.sleep(.5)
	mdown()
	time.sleep(.5)
	down()
