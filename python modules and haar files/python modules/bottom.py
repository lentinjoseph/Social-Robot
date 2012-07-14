import servo
import time

def left():
	time.sleep(.5)
	servo.move(8,50)

def mleft1():
	time.sleep(.5)
	servo.move(8,60)
def mleft2():
        time.sleep(.5)
        servo.move(8,70)
def mleft3():
        time.sleep(.5)
        servo.move(8,80)

def mleft4():
        time.sleep(.5)
        servo.move(8,90)
def mleft5():
        time.sleep(.5)
        servo.move(8,100)

def mid():
        time.sleep(.5)
        servo.move(8,110)
def mright1():
        time.sleep(.5)
        servo.move(8,120)
def mright2():
        time.sleep(.5)
        servo.move(8,130)
def mright3():
        time.sleep(.5)
        servo.move(8,140)
def right():
	time.sleep(.5)
	servo.move(8,150)

def left1():
	mleft5()
	mleft4()
	mleft3()
	mleft2()
	mleft1()
	left()
def ltor():
	time.sleep(.5)
	left()
        time.sleep(.5)
	mleft1()
        time.sleep(.5)
	mleft2()
        time.sleep(.5)
	mleft3()
        time.sleep(.5)
	mleft4()
        time.sleep(.5)
	mleft5()
        time.sleep(.5)
	mid()
        time.sleep(.5)
	mright1()
        time.sleep(.5)
	mright2()
        time.sleep(.5)
	mright3()
        time.sleep(.5)
	right()


def rtol():
	
        time.sleep(.5)
        right()
        time.sleep(.5)
        mright3()
        time.sleep(.5)
        mright2()
        time.sleep(.5)
        mright1()
        time.sleep(.5)
        mid()
        time.sleep(.5)
        mleft5()
        time.sleep(.5)
        mleft4()
        time.sleep(.5)
        mleft3()
        time.sleep(.5)
	mleft2()
	time.sleep(.5)
	mleft1()
	time.sleep(.5)
	left()
