class Hero:
    def __init__(self, name="John Doe", hp=100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp += 10
        return f"{self.name}, восстанавливает здоровье на +10 HP^{self.hp}"
    def status_info(self):
        return(f"имя: {self.name}"
        f"\nздоровье: {self.hp}")
   
    def action(self):
        return f"{self.name} делает базовое действие"


hero = Hero("Kirtito")
hero_actions=(f"{hero.rest()},f\n{hero.action()}")
if isinstance(hero, Hero):
    print("Hero является экземпляром класса Hero")
else:
    print("Hero не является экземпляром класса Hero")
    

print(hero.status_info())
print(hero_actions)

# Наследование
class Warrior(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 10
            return f"{self.name} Превращается в Алмаза"
        else:
            return f"{self.name} стамина меньше 10"
    def status_info(self):
        return (f"имя: {self.name   }" f"\nздоровье: {self.hp}" f"\nвыносливость{self.st}")
    def charge(self):
        self.st-20
        self.hp+50
        return (f"{self.name}улиление выносливость {self.st -20} здоровье {self.hp+50}")
hero_warrior = Warrior("Ben-10", 1000, 100)

if isinstance(hero_warrior, Hero):
    print("wariors является экземпляром класса Hero")
else:
    print("wariors не является экземпляром класса Hero")
    
# print(hero_warrior.rest())
print(hero_warrior.status_info())
print(hero_warrior.charge())
class Mage(Hero):

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp
    def teleport(self):
        if self.mp >= 30:
            return f"{self.name} перемешение"
        else:
            return f"{self.name} Мана меньше 10"

    def rest(self):
        return f"{self.name} , восстанавливает  ману на +10 MP^{self.mp}"
    def status_info(self):
        return (f"имя: {self.name   }" f"\nздоровье: {self.hp}" f"\n мана{self.mp}")
    def attack(self):
        if self.mp >= 10:
            self.mp -= 10
            return f"{self.name} Колдует в Огненый щар"
        else:
            return f"{self.name} Мана меньше 10"

    def action(self):
        old_action = super().action()
        attack = self.attack()

        return f"{old_action}  {attack}"

    
mage=Mage ("megumi",100,35)
print(mage.status_info())
if isinstance(mage, Hero):
    print("mage является экземпляром класса Hero")
else:
    print("mage не является экземпляром класса Hero")
print(mage.teleport())
class Archer(Hero):

    def __init__(self, name, arrows, precision):
        super().__init__(name, arrows)
        self.arrows = arrows
        self.precision = precision

    def rest(self):
        return f"{self.name} , восстанавливает  стрелы  на +5 {self.arrows}"

    def attack(self):
        if self.precision >=10:
            self.arrows -1 
            return f"{self.name} попал"
        else:
            return f"{self.name} не попал"   
    def status_info(self):
        return (f"имя: {self.name   }" f"\n количество стрел: {self.arrows}" f"\n точность {self.precision}")
    def action(self):
        old_action = super().action()
        attack = self.attack()

        return f"{old_action}  {attack}"
archer=Archer("robin good",9,10)
if isinstance(archer, Hero):
    print("archer является экземпляром класса Hero")
else:
    print("archer не является экземпляром класса Hero")
print(archer.status_info())

hero=Hero("spider-man",10000000)
hero_warrior=Warrior("Kratos",1000000,1000000)
mage=Mage("Harry Poter", 100,500000)
archer=Archer("Jack ",100,23300)
hero_actions=(f"{hero.rest()},f\n{hero.action()}")
hero_actions1=(f"{hero_warrior.rest()},f\n{hero_warrior.action()}")
hero_actions2=(f"{mage.rest()},f\n{mage.action()}")
hero_actions3=(f"{archer.rest()},f\n{archer.action()}")
print(hero_actions)
print(hero_actions1)
print(hero_actions2)
print(hero_actions3)
