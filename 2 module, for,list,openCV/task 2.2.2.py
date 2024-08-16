import turtle
import random

for i in range(100):
    x=random.randrange(100)
    y=random.randrange(100)
    r=random.randrange(1,100)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)
turtle.done()