import servo
import time


def left():
	time.sleep(.5)
	servo.move(5,170)
	
def mid():
	time.sleep(.5)
	servo.move(5,175)

def right():
	time.sleep(.5)
	servo.move(5,180)
