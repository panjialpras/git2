import os
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} \n\t with health: {}".format(
            self.name,
            self.health
            )
            )

class Hero_agility(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 120)
        super().__init__(name, 120)
    
    def showInfo(self):
        # override
        print("{} \n\t Type: Agility \n\t Health: {}".format(self.name, self.health)
        )

class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 85)

    def showInfo(self):
        # override
        print("{} \n\t Type: Intelligent \n\t Health: {}".format(self.name, self.health)
        )


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 190)

    def showInfo(self):
        # override
        print("{} \n\t Type: Strength \n\t Health: {}".format(self.name, self.health)
        )

os.system('cls')
lindy = Hero_intelligent("Lindy")
ryo = Hero_strength("Ryokage")
tor = Hero_agility("Tor")

lindy.showInfo()
ryo.showInfo()
tor.showInfo()