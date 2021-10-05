class Hero:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        # self.__info = "Name {} : \n\tHealth: {}".format(self.__name, self.__health)
    # getter & setter
    @property
    def info(self):
        return "Name {} : \n\tHealth: {}".format(self.name, self.__health)

    @property
    def defense(self):
        pass
    @defense.getter
    def defense(self):
        return self.__defense
    @defense.setter
    def defense(self, input):
        self.__defense = input
    @defense.deleter
    def defense(self):
        print('defense dihapus!')
        self.__defense = None

    # @property
    # def info(self):
    #     return self.__info


kuro = Hero("Kuro", 100, 50, 10)

print("rubah info")
print(kuro.info)
kuro.name = "Lindy"
print(kuro.info)


print("get set __defense")
print(kuro.defense)
kuro.defense = 123
print(kuro.defense)
print('hapus armor')
del kuro.defense
print(kuro.__dict__)