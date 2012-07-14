import servo
import time
import threading
class sAction(threading.Thread):
        def __init__(self):
	    threading.Thread.__init__(self,None)
	    self.MOUTH_SERVO=1
            self.MOUTH_INIT_POS=5
            self.MOV_CONST=6
            self.MAX_ANGLE=48
            self.SERVO_DELAY=.3
            self.stmt=["hello"]
            self.speak=False
            self.stop=0
            servo.move(self.MOUTH_SERVO,self.MOUTH_INIT_POS)
            self.start()
		
	def run(self):
                while True:
                    if self.speak==True:
                        for i in self.stmt.split():
                            servo.move(self.MOUTH_SERVO,self.MOUTH_INIT_POS)
                            s=len(i)
                            angle=s*self.MOV_CONST
                            if(angle>self.MAX_ANGLE):
                                angle=self.MAX_ANGLE
                            print i
                            servo.move(self.MOUTH_SERVO,angle)
                            time.sleep(self.SERVO_DELAY)
                            servo.move(self.MOUTH_SERVO,self.MOUTH_INIT_POS)
                        self.speak=False
                    if self.stop==1:
                        break
