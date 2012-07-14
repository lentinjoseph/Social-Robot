import servo
import time
def up():
	time.sleep(.5)
	servo.move(6,90)

def mid():
	time.sleep(.5)
	servo.move(6,150)

def down():
	time.sleep(.5)
	servo.move(6,180)
