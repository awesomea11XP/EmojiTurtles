import turtle

chell = turtle.Turtle()
glados = turtle.Turtle()
wheatly = turtle.Turtle()
ratman = turtle.Turtle()

def blush():
    for i in range(3):
        chell.forward(50)
        chell.right(90)
        chell.forward(50)
        chell.right(270)


chell.color("yellow")
chell.begin_fill()
chell.circle(200)
chell.end_fill()

glados.pensize(10)
glados.color("yellow")
glados.right(270)
glados.forward(250)
glados.right(270)
glados.forward(50)
glados.right(90)
glados.color("black")
glados.forward(75)
glados.pensize(8)
glados.right(180)
glados.forward(10)
glados.color("white")
glados.forward(10)

wheatly.pensize(10)
wheatly.color("yellow")
wheatly.right(270)
wheatly.forward(250)
wheatly.right(90)
wheatly.forward(50)
wheatly.right(270)
wheatly.color("black")
wheatly.forward(75)
wheatly.pensize(8)
wheatly.right(180)
wheatly.forward(10)
wheatly.color("white")
wheatly.forward(10)

chell.right(225)
chell.forward(250)
chell.right(45)
chell.right(90)
chell.forward(75)
chell.color("red")
chell.right(315)
blush()
chell.color("yellow")

ratman.color("yellow")
ratman.right(270)
ratman.forward(100)
ratman.color("black")
ratman.right(90)
ratman.forward(50)
ratman.color("yellow")
ratman.home()
ratman.right(270)
ratman.forward(100)
ratman.color("black")
ratman.right(270)
ratman.forward(50)
ratman.color("yellow")



turtle.exitonclick()
