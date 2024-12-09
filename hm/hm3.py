from abc import ABC, abstractmethod
import random


class Hero(ABC):

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #Защищенный атрибут
        self._luck = random.randint(0, 100)
        #Приватный атрибут
        self.__crit_dmg = random.randint(0, 100)

    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f'Привет, {self.name}! \n Мой уровень: {self.lvl}')

    def status(self):
        return print(f'LVL: {self.lvl} \n HP: {self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} критический удар!')
        else:
            return print(f"{self.name} базовый удар!")

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} Успешно защищается!")
        else:
            return print(f"{self.name} не смог защититься!")

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} одыхает и востанавливает здорвье. Новое здоровьне: {self.hp}')

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass
    @abstractmethod
    def action (self):
        pass
    def __random_action(self):
        return random.randint(1,2,3)


class Jester (Hero):
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #Защищенный атрибут
        self._luck = random.randint(0, 100)
        #Приватный атрибут
        self.__crit_dmg = random.randint(0, 100)
        self.__random_action = random.randint(1,3)
    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f'Привет, {self.name}! \n Мой уровень: {self.lvl}')

    def status(self):
        return print(f'LVL: {self.lvl} \n HP: {self.hp}')

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f'{self.name} критический удар!')
        else:
            return print(f"{self.name} базовый удар!")

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} Успешно защищается!")
        else:
            return print(f"{self.name} не смог защититься!")

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} одыхает и востанавливает здорвье. Новое здоровьне: {self.hp}')
    def unique_attack(self):
        if self.lvl>=4:
            print(f"{self.name}ултра мега атака")
        else:
            print("не повезло не фортануло")

    def unique_scream(self):
        if self.hp >=10:
            print(f"{self.name } вы обосрались")
        else:
            print("вы не обосралисЬ")
    
    def action (self):
        if self.__random_action== 1:
            return print(f"{self.name}:{self.attack}")
        if self.__random_action==2:
            return print(f"{self.name}:{self.protection}")
        else:
            return print(f"{self.name},:{self.rest}")
joker=Jester("marry",23,5)
joker.unique_attack()
joker.unique_scream()
joker.action()
