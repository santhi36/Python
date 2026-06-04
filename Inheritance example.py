class Character:
    def __init__(self,name,hp,attack,buff=0.2):
        self.name=name
        self.hp=hp
        self.attack=attack
        self.buff=buff
    def __str__(self):
        return f"name:{self.name}\n hp:{self.hp}\n attack:{self.attack}\n buff:{self.buff}"
class Mage (Character):
    pass
class Warrior(Character):
    pass
m1=Mage("karishma",100,1,0.3)
m2=Warrior("santhi",101,4,0.4)
print(m1.__str__())
print(m2.__str__())