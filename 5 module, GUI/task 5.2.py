import turtle

def draw_square(x,y):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(20)
        turtle.right(90)

def draw_triangle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for _ in range(3):
        turtle.forward(20)
        turtle.right(120)

def draw_circle(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(20)

turtle.onscreenclick(draw_square)
turtle.onscreenclick(draw_triangle,3)
turtle.onscreenclick(draw_circle,1,add=True)
turtle.mainloop()