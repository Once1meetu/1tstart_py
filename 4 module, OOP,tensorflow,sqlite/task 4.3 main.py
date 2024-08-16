import task_4_3_module as my


a = my.Draw()
a.create_circle(20)

a.t.penup()
a.t.goto(100,100)
a.t.pendown()
a.create_square(100)

a.t.penup()
a.t.goto(-100,-100)
a.t.pendown()
a.what_to_drow()

my.turtle.done()