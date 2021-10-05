import os

class Hero:
    def __init__(self,name, health, power, defense) :
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
    
    def attack(self, opponent):
        print(self.name + ' attacking ' + opponent.name)
        opponent.gotAttack(self, self.power)
   
    def gotAttack(self, opponent, power_opponent):
        print(self.name + ' got attack by ' + opponent.name)
        attack= power_opponent/self.defense
        print( ' got attack : ' + str(attack) )
        self.health -= attack
        print( 'Hp ' + self.name + ' left ' + str(self.health))

gord = Hero('Gord', 90, 4, 10)
okhlama = Hero("Okhlama", 100, 14, 5)

os.system("cls")

gord.attack(okhlama)
print("\n")
okhlama.attack(gord)

