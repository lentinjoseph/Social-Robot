#!/usr/bin/env python

################################################
# Module:   servo.py
# Created:  2 April 2008
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.2
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleServos" sketch.
'''
################################################

import serial

usbport = '/dev/ttyUSB0'
ser = serial.Serial(usbport, 9600)
#print ser

def move(servo, angle):
    '''Moves the specified servo to the supplied angle.

    Arguments:
        servo
          the servo number to command, an integer from 1-4
        angle
          the desired servo angle, an integer from 0 to 180

    (e.g.) >>> servo.move(2, 90)
           ... # "move servo #2 to 90 degrees"'''
    
    if(servo==1):
	
    	if (3 <= angle <= 50):	#Initial values of servo1 mouth
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 10 and 50.\n"
    if(servo==2):
	
    	if (0 <= angle <= 80):	#Initial values of servo2 left ear
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 80.\n"

    if(servo==3):
	
    	if (0 <= angle <= 10):	#Initial values of servo3 left eyebrow
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==4):
	
    	if ((angle==35) | (angle==50) | (angle==66) | (angle==80) | (angle==90)):	#Initial values of servo4  eyes
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 35 and 90.\n"

    if(servo==5):
	
    	if (170 <= angle <= 180):	#Initial values of servo5 right eyebrow
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==6):
	
    	if (90 <= angle <= 180):	#Initial values of servo6 right ear
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"
    if(servo==7):
	
    	if (5 <= angle <= 70):	#Initial values of servo7 eye appartus
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==8):
	
    	if (50 <= angle <= 150):	#Initial values of servo8 bottom
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"
    if(servo==9):
	
    	if (0 <= angle <= 180):	#Initial values of servo8 bottom
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==10):
	
    	if (0 <= angle <= 180):	#speech
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==11):
	
    	if (0 <= angle <= 180):	#motion
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"

    if(servo==12):
	
    	if (0 <= angle <= 180):	#faces
        	ser.write(chr(255))
        	ser.write(chr(servo))
        	ser.write(chr(angle))
    	else:
        	print "Servo angle must be an integer between 0 and 10.\n"







