import turtle
import random

class Figure:
    who_are_you=[]#1-circle,2-triangle,3-square
    what_size=[]
    x = []
    y = []
    num=-1#number of figure in list
    def go(self):
        x = random.randrange(200)
        y = random.randrange(200)
        self.x.append(x)
        self.y.append(y)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

class Draw(Figure):
    def create_circle(self,r):
        self.go()
        turtle.circle(r)
        self.who_are_you.append(1)
        self.what_size.append(r)
        self.num+=1
    def create_triangle(self,a):
        self.go()
        self.who_are_you.append(2)
        self.what_size.append(a)
        self.num += 1
        for _ in range(3):
            turtle.forward(a)
            turtle.right(120)
    def create_square(self,a):
        self.go()
        self.who_are_you.append(3)
        self.what_size.append(a)
        self.num += 1
        for _ in range(4):
            turtle.forward(a)
            turtle.right(90)
    def what_to_drow(self):
        c=random.randrange(1,4)#type
        a = random.randrange(10,50)# type
        if c==1:
            self.create_circle(a)
        elif c==2:
            self.create_triangle(a)
        elif c==3:
            self.create_square(a)

class Cringe(Draw):
    def Did_u_click_on_circle(self, x, y):# method to perform action
        for i in range(len(self.who_are_you)):
            if self.who_are_you[i]==1:
                if pow(self.x[i]-x,2)+pow(self.y[i]+self.what_size[i]-y,2)<=pow(self.what_size[i],2):
                    #print(str(x)+","+str(y))
                    turtle.Screen().clear()


# screen object

cringe=Cringe()
for _ in range(10):
    cringe.what_to_drow()

# onclick action
turtle.Screen().onclick(cringe.Did_u_click_on_circle)
turtle.Screen().mainloop()