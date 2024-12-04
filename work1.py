#наследование полиморфизм 
class hero :
    def __init__(self,  name , hp):
        self.name=name 
        self.hp=hp
        


    def rest (self):
        self.hp+=10
        return f"{self.name}, востановление {self.hp}"
    

    def action (self):
        return F"{self.name } футболл"

hero=hero('лох', 100)

print(hero.rest())
print(hero)

class wariors (hero):
    def attack(self):
        return f"{self.name} панч"
    
    
    