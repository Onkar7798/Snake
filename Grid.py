# import package and making objects 
import turtle 


sc=turtle.Screen() 
trtl=turtle.Turtle() 

# method to draw y-axis lines 
def drawy(val): 
	
	# line 
	trtl.forward(300) 
	
	# set position 
	trtl.up() 
	trtl.setpos(val,300) 
	trtl.down() 
	
	# another line 
	trtl.backward(300) 
	
	# set position again 
	trtl.up() 
	trtl.setpos(val+10,0) 
	trtl.down() 
	
# method to draw y-axis lines 
def drawx(val): 
	
	# line 
	trtl.forward(300) 
	
	# set position 
	trtl.up() 
	trtl.setpos(300,val) 
	trtl.down() 
	
	# another line 
	trtl.backward(300) 
	
	# set position again 
	trtl.up() 
	trtl.setpos(0,val+10) 
	trtl.down() 
	

	

# Main Section 
# set screen 
sc.setup(800,800)	 

# set turtle features 
trtl.speed(100) 
trtl.left(90) 
trtl.color('lightgreen') 

# y lines 
for i in range(30): 
	drawy(10*(i+1)) 

# set position for x lines 
trtl.right(90) 
trtl.up() 
trtl.setpos(0,0) 
trtl.down() 

# x lines 
for i in range(30): 
	drawx(10*(i+1)) 

# hide the trtle 
trtl.hideturtle()
