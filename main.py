from turtle import *

timmy = Turtle()
timmy.color("black")
timmy.pensize(6)
timmy.pencolor("white")
timmy.speed(100)

global moving
def moving():
    ''' Moves Turtle in between objects.'''
    timmy.penup()
    timmy.forward(20)
    timmy.left(90)
    timmy.pendown()

sc = Screen()
sc.screensize(1000,1000)
sc.bgcolor("black")

# Letter H
timmy.left(90)
timmy.forward(100)
timmy.back(50)
timmy.right(90)
timmy.forward(50)
timmy.left(90)
timmy.forward(50)
timmy.back(100)

# Moving
timmy.penup()
timmy.right(90)
timmy.forward(20)
timmy.left(90)
timmy.pendown()

# Letter E
timmy.forward(100)

for i in range(2):
    timmy.right(90)
    timmy.forward(50)
    timmy.back(50)
    timmy.left(90)
    timmy.back(50)
timmy.right(90)
timmy.forward(50)

# Letter L
for i in range(2):
    # Moving
    moving()

    timmy.forward(100)
    timmy.backward(100)
    timmy.right(90)
    timmy.forward(50)

# Letter O

# Moving
moving()

for i in range(2):
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)

timmy.hideturtle()
sc.mainloop()

