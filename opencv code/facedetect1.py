#!/usr/bin/python
"""
This program is demonstration for face and object detection using haar-like features.
The program finds faces in a camera image or video stream and displays a red box around them.

Original C implementation by:  ?
Python implementation by: Roman Stanchak, James Bowman
"""
import sys
import cv
from optparse import OptionParser
import urllib2
import time
from math import cos, sin
import cv
import led
import socket
import emotion
import bottom
# Parameters for haar detection
# From the API:
# The default parameters (scale_factor=2, min_neighbors=3, flags=0) are tuned 
# for accurate yet slow object detection. For a faster operation on real video 
# images the settings are: 
# scale_factor=1.2, min_neighbors=2, flags=CV_HAAR_DO_CANNY_PRUNING, 
# min_size=<minimum possible face size

min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0
CLOCKS_PER_SEC = 1.0
MHI_DURATION = 1
MAX_TIME_DELTA = 0.5
MIN_TIME_DELTA = 0.05
N = 4
buf = range(10) 
last = 0
mhi = None # MHI
orient = None # orientation
mask = None # valid orientation mask
segmask = None # motion segmentation map
storage = None # temporary storage
var1 =0
var2 =0
	

def update_mhi(img, dst, diff_threshold):
    global last
    global mhi
    global storage
    global mask
    global orient
    global segmask
    timestamp = time.clock() / CLOCKS_PER_SEC # get current time in seconds
    size = cv.GetSize(img) # get current frame size
    idx1 = last
    global var1
    if not mhi or cv.GetSize(mhi) != size:
        for i in range(N):
            buf[i] = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
            cv.Zero(buf[i])
        mhi = cv.CreateImage(size,cv. IPL_DEPTH_32F, 1)
        cv.Zero(mhi) # clear MHI at the beginning
        orient = cv.CreateImage(size,cv. IPL_DEPTH_32F, 1)
        segmask = cv.CreateImage(size,cv. IPL_DEPTH_32F, 1)
        mask = cv.CreateImage(size,cv. IPL_DEPTH_8U, 1)
    
    cv.CvtColor(img, buf[last], cv.CV_BGR2GRAY) # convert frame to grayscale
    idx2 = (last + 1) % N # index of (last - (N-1))th frame
    last = idx2
    silh = buf[idx2]
    cv.AbsDiff(buf[idx1], buf[idx2], silh) # get difference between frames
    cv.Threshold(silh, silh, diff_threshold, 1, cv.CV_THRESH_BINARY) # and threshold it
    cv.UpdateMotionHistory(silh, mhi, timestamp, MHI_DURATION) # update MHI
    cv.CvtScale(mhi, mask, 255./MHI_DURATION,
                (MHI_DURATION - timestamp)*255./MHI_DURATION)
    cv.Zero(dst)
    cv.Merge(mask, None, None, None, dst)
    cv.CalcMotionGradient(mhi, mask, orient, MAX_TIME_DELTA, MIN_TIME_DELTA, 3)
    if not storage:
        storage = cv.CreateMemStorage(0)
    seq = cv.SegmentMotion(mhi, segmask, storage, timestamp, MAX_TIME_DELTA)
    for (area, value, comp_rect) in seq:
        if comp_rect[2] + comp_rect[3] > 250: # reject very small components
            color = cv.CV_RGB(255, 0,0)
            silh_roi = cv.GetSubRect(silh, comp_rect)
            mhi_roi = cv.GetSubRect(mhi, comp_rect)
            orient_roi = cv.GetSubRect(orient, comp_rect)
            mask_roi = cv.GetSubRect(mask, comp_rect)
            angle = 360 - cv.CalcGlobalOrientation(orient_roi, mask_roi, mhi_roi, timestamp, MHI_DURATION)
	    print angle
            count = cv.Norm(silh_roi, None, cv.CV_L1, None) # calculate number of points within silhouette ROI
            if count < (comp_rect[2] * comp_rect[3] * 0.05):
                continue

            magnitude = 80.
            center = ((comp_rect[0] + comp_rect[2] / 2), (comp_rect[1] + comp_rect[3] / 2))
            cv.Circle(dst, center, cv.Round(magnitude*1.2), color, 10, cv.CV_AA, 0)
            print "motion detected at",center[1]
	    
	    if (center[1] > 320):
		
	    	
		bottom.mright3()
	    if (center[1] <320):
		
	    	
		bottom.mleft4()
	    var1=var1+1
	    if (var1==40):
	    	led.motion()
	    	var1=0
		if (center[1] > 320):
	#		print "hai"
	    		
	                bottom.mright3()
       	        if (center[1] <320):
			

        	        bottom.mleft4()
			print "hai"
	    	emotion.exclaim()
	    cv.Line(dst,
                    center,
                    (cv.Round(center[0] + magnitude * cos(angle * cv.CV_PI / 180)),
                     cv.Round(center[1] - magnitude * sin(angle * cv.CV_PI / 180))),
                    color,
                    3,
                    cv.CV_AA,
                    0)
	   

def detect_and_draw(img, cascade):
    # allocate temporary images
    global var2
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
			       cv.Round (img.height / image_scale)), 8, 1)

    # convert color input image to grayscale
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

    # scale input image for faster processing
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)

    cv.EqualizeHist(small_img, small_img)

    if(cascade):
        t = cv.GetTickCount()
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)
        t = cv.GetTickCount() - t
#        print "detection time = %gms" % (t/(cv.GetTickFrequency()*1000.))
        if faces:
            for ((x, y, w, h), n) in faces:
                # the input to cv.HaarDetectObjects was resized, so scale the 
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * image_scale), int(y * image_scale))
                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
		print pt1	
		var2=var2+1
		if (var2==10):
			led.face()
			var2=0		
			emotion.happy()
    cv.ShowImage("result", img)

if __name__ == '__main__':
    motion = 0
    parser = OptionParser(usage = "usage: %prog [options] [filename|camera_index]")
    parser.add_option("-c", "--cascade", action="store", dest="cascade", type="str", help="Haar cascade file, default %default", default = "../data/haarcascades/haarcascade_frontalface_alt.xml")
    (options, args) = parser.parse_args()

    cascade = cv.Load(options.cascade)
    
    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    input_name = args[0]
    if input_name.isdigit():
        capture = cv.CreateCameraCapture(int(input_name))
    else:
        capture = None

    cv.NamedWindow("result", 1)
    cv.NamedWindow("Motion", 1)
    if capture:
        frame_copy = None
        while True:
            frame = cv.QueryFrame(capture)
            if(frame):
            	if(not motion):
                	    motion = cv.CreateImage((frame.width, frame.height), 8, 3)
                	    cv.Zero(motion)
                    #motion.origin = image.origin
            	update_mhi(frame, motion, 30)
            	cv.ShowImage("Motion", motion)
	    if not frame:
                cv.WaitKey(0)
                break
            if not frame_copy:
                frame_copy = cv.CreateImage((frame.width,frame.height),
                                            cv.IPL_DEPTH_8U, frame.nChannels)
            if frame.origin == cv.IPL_ORIGIN_TL:
                cv.Copy(frame, frame_copy)
            else:
                cv.Flip(frame, frame_copy, 0)
            
            detect_and_draw(frame_copy, cascade)

            if cv.WaitKey(10) >= 0:
                break
    else:
        image = cv.LoadImage(input_name, 1)
        detect_and_draw(image, cascade)
        cv.WaitKey(0)

    cv.DestroyWindow("result")
