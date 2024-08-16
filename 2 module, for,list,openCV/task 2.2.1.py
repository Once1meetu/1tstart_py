import turtle

import math

a = 150

b = 90

dx = turtle.xcor()

dy = turtle.ycor()

for deg in range(361):
    rad = math.radians(deg)

    x = a * math.sin(rad) + dx

    y = -b * math.cos(rad) + b + dy

    turtle.goto(x, y)
turtle.done()