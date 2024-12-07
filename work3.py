# инкапсуляция - абстракция
class Hero :
    def __init__(self, name , hp,lvl ):
        self.name=name
        self.hp=hp
        self.lvl=lvl
    def greetings(self):
        return print(f"привет,{self.name }! \ мой уровень{self.lvl}")

        