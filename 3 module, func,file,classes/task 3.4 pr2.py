class Human:
    def __init__(self, name="Noname", hp=100, lvl=1, max_hp=100):
        self.name=name
        self.hp=hp
        self.lvl=lvl
        self.max_hp=max_hp
    def die(self):
        self.hp=0
        print(f"{self.name} is dead")
    def lvl_up(self):
        self.lvl_+=1
        self.max_hp+=10
        print(f"{self.name} is lvl_upped to {self.lvl}")
    def harm(self,damage):
        self.hp-=damage
        print(f"{self.name} is damaged {damage}, hp {self.hp}")

class Doc(Human):
    def __init__(self, name="Noname", hp=100, lvl=1, max_hp=100,med=0,perk=5):
        super().__init__(name,hp,lvl,max_hp)
        self.med=med
        self.perk=perk
    def cure(self,sicked):
        self.med-=1
        sicked.hp+=self.perk
        print(f"{self.name} cured {sicked.name} {self.perk} up, it's hp {sicked.hp}")
    def lvl_up(self):
        self.lvl+=1
        self.max_hp+=15
        self.perk+=5
        print(f"{self.name} is lvl_upped to {self.lvl}")

class Cook(Human):
    def __init__(self, name="Noname", hp=100, lvl=1, max_hp=100,food=0,perk=2):
        super().__init__(name,hp,lvl,max_hp)
        self.food=food
        self.perk=perk
    def feed(self,hungry_guy):
        self.food-=1
        hungry_guy.hp+=self.perk
        print(f"{self.name} fed {hungry_guy.name} {self.perk} up, it's hp {hungry_guy.hp}")
    def lvl_up(self):
        self.lvl+=1
        self.perk+=2
        print(f"{self.name} is lvl_upped to {self.lvl}")

pers_01 = Human("Saanyaaa")
pers_02 = Doc(name="Mashka", lvl=100, med=2, hp=2, max_hp=250, perk=105)
pers_03 = Cook("Tyotya Tanya", food=10000)
pers_01.harm(50)
pers_03.feed(pers_01)
pers_03.lvl_up()
pers_01.harm(50)
pers_02.cure(pers_01)
pers_02.lvl_up()
pers_01.harm(110)
pers_01.die()

