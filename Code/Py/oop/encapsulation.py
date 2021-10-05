class Hero:
    def __init__(self,name, health, power) :
        self.__name = name
        self.__health = health
        self.__attpower = power
    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health
    
    # setter
    def gotAttack(self, fight_power):
        self.__health -= fight_power



# game start
earthmage = Hero("Earth Mage", 75, 5)
# game on
print(earthmage.getName())
print(earthmage.getHealth())
earthmage.gotAttack(10)
print(earthmage.getHealth())