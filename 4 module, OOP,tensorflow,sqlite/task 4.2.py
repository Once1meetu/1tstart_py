class Square:
    def __init__(self,a=10):#конструктор скрыт сам по себе
        self.__a=a#поле реализовано как свойство
    @property
    def side(self):
        return self.__a
    @side.setter
    def side(self,a):
        self.__a = a
    def area(self):
        return self.__a**2
    def perimeter(self):
        return self.__a*4
    def __str__(self):
        return str(self.__a)
a=Square()
b=Square(100)
a.side=50
d_a=a.area()**0.5
d_b=b.area()**0.5
if a.side>b.side:
    print(f"В квадрат {a}x{a} вмещается ", a.area()/b.area(),f"квадрата {b}x{b}")
else:
    print(f"В квадрат {b}x{b} вмещается ", b.area() / a.area(), f"квадрата {a}x{a}")