import turtle
import random
class Draw():
    t = turtle.Turtle()
    def create_circle(self,r):
        self.t.circle(r)
    def create_triangle(self,a):
        for _ in range(3):
            self.t.forward(a)
            self.t.right(120)
    def create_square(self,a):
        for _ in range(4):
            self.t.forward(a)
            self.t.right(90)
    def what_to_drow(self):
        c = random.randrange(1,4)#type
        a = random.randrange(10,50)# type
        if c==1:
            self.create_circle(a)
        elif c==2:
            self.create_triangle(a)
        elif c==3:
            self.create_square(a)
