import servo
import time
def up():	
	time.sleep(.5)
	servo.move(2,80)

def down():
	time.sleep(.5)
	servo.move(2,0)

def mid():
	time.sleep(.5)
	servo.move(2,30)


