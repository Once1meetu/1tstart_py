class human:
    def __init__(self, name="Noname", surname="Nosername"):
        self.__name=name
        self.__surname=surname
        self.__chiken = int(input("how much chiken do u have?\n"))
        self.__grilled_chiken=int(input("how much grilled chiken do u have?\n"))
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, s):
        self.__name=s
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, s):
        self.__surname = s
    def cook_chiken(self, n):
        if self.__chiken>=n:
            self.__grilled_chiken += n
            self.__chiken -= n
        else:
            print("U want too much. U haven\'t enough chiken, u have only ",self.__chiken)
    def eat_chiken(self, n):
        if self.__grilled_chiken>=n:
            self.__grilled_chiken -= n
        else:
            print("U want too much. U haven\'t enough grilled chiken, u have only",self.__grilled_chiken)
    def buy_chiken(self, n):
        self.__chiken += n
        print("U bought",n,"chicken")

def to_live(a):
    while (1):
        a1=int(input("how much grilled chiken do u want to eat?\n"))
        a.eat_chiken(a1)
        a2=input("wanna cook chiken?(y/n)")
        if a2=='y':
            a22 = int(input("How much chiken do u want to cook?\n"))
            a.cook_chiken(a22)
        a3=input("wanna buy chiken?(y/n)")
        if a3=='y':
            a33 = int(input("How much chiken do u want to buy?\n"))
            a.buy_chiken(a33)

person=human()
person.eat_chiken(int(input("how much chiken do u want to eat?\n")))

guy_name=input("name?\n")
guy_surname=input("surname?\n")
guy=human(guy_name, guy_surname)
to_live(guy)
