import loadall
import eartest

def happy():
	#loadall.lear.up()
	#loadall.rear.up()
        eartest.ear_simul_up(80)
	loadall.eyeapp.mid()
	loadall.mouth.open()

def sad():
	#loadall.lear.down()
	#loadall.rear.down()
        eartest.ear_simul_down(80)
	loadall.eyeapp.mdown()
	loadall.mouth.close()

def exclaim():
	loadall.lear.mid()
	loadall.rear.mid()
	loadall.eyeapp.mup()

def confuse():
	loadall.lear.up()
	loadall.rear.down()
	loadall.eyeapp.mid()
	loadall.mouth.smile()

