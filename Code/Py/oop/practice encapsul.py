class Hero:

    # private class variable
    __jml = 0
    def __init__(self, name, health, attack, armor) :
        self.__name = name
        self.__healthBase = health
        self.__attackBase = attack
        self.__armorBase  = armor
        self.__level = 1
        self.__exp = 0 

        self.__healthMax = self.__healthBase * self.__level
        self.__attackStandard = self.__attackBase  * self.__level
        self.__armorStandard  = self.__armorBase * self.__level

        self.__health = self.__healthMax

        Hero.__jml += 1
    
    @property
    def info(self) :
        return "{} level {}: \n\tHealth = {}/{} \n\t Attack = {} \n\t Armor = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attackStandard, self.__armorStandard)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, upExp) :
        self.__exp =+ upExp
        if(self.__exp >= 100) :
            print(self.__name, 'Level Up!')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attackStandard = self.__attackBase  * self.__level
            self.__armorStandard  = self.__armorBase * self.__level
    def fight(self, opponent):
        self.gainExp = 90

kuro = Hero("Kuro", 1500, 25, 15)
lindy = Hero("Lindy", 3254, 50, 5)
print(kuro.info)

kuro.fight(lindy)
kuro.fight(lindy)
print(kuro.info)




