import servo
import time
def speak():
	servo.move(1,40)
	servo.move(1,3)
	time.sleep(0.5)
	servo.move(1,20)
	time.sleep(.5)
	servo.move(1,3)
	time.sleep(.5)
	servo.move(1,20)
	time.sleep(.5)
	servo.move(1,3)
        time.sleep(.5)
        servo.move(1,20)
def open():
	time.sleep(1)
	servo.move(1,50)

def close():
	time.sleep(1)
	servo.move(1,3)

def smile():
	time.sleep(.5)
	servo.move(1,40)
