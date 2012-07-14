#import commands
import festival
import aiml
k=aiml.Kernel()
k.loadBrain("alice.brn")
#k.learn("startup.xml")
#k.respond("load aiml b")
#commands.getoutput("espeak -k20 -s150 -ven+15 Hello User")
while True : 
	len0=k.respond(raw_input("Me:>"))
	#len1="espeak -k20 -s150 -ven+10"
	#len0 = " \""+len0+"\""
	#len2=len1+len0
	#commands.getoutput(len2)
	festival.open().say(len0)	
	print len0
