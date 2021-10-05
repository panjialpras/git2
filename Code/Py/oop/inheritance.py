import os
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
class Hero_agility(Hero):
     pass
class Hero_intelligent(Hero):
    pass
kuro = Hero('Kuro', 150)
yoda = Hero_agility('Yoda', 70)
mikoto = Hero_intelligent('Mikoto', 90)

print(kuro.name)
print(yoda.name)
print(mikoto.name)