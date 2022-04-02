import turtle
turtlePen = turtle.Turtle
t = turtle.Pen()
turtle.bgcolor("Black")
sides = 6
colors = ["red", "blue", "orange",
         "green", "purple", "yellow"]
for x in range(360):
	t.speed(10)
	t.pencolor(colors[x % sides])
	t.forward(x * 3/sides + x)
	t.left(360/sides + 1)
t.width(x * 0.03)

