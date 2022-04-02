import turtle
playrAscore=0
playBscore=0

window.Turtle()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddlee
rightpaddle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball

ball.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating pen for scorecard update

pen.Turtle
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="Center",font=('Arial',24,'normal'))



#moving the leftpaddle
def leftpaddleup():
	y.leftpaddle.ycor()
	y=y+90
	leftpaddle.sety(y)



def rightpaddleup():
	y=rightpaddler.ycor()
	y=y-90
	rightpaddle.sety(y)




win.mainloop()


