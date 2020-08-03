import turtle

pen = turtle.Turtle()
pen.color("green")
sc = turtle.getscreen()
sc.bgcolor("black")
sc.screensize(200,200)
pen.up()
pen.setpos(-400,300)
pen.down()
for i in range(0,2):
	pen.forward(200)
	pen.penup()
	pen.right(90)
	pen.forward(50)
	pen.right(90)
	pen.pendown()
	pen.forward(200)
	pen.penup()
	pen.left(90)
	pen.forward(50)
	pen.left(90)
	pen.pendown()



turtle.done()