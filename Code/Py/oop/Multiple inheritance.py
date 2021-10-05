class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Typehero:
    def setType(self, type):
        self.type = type

    def showType(self):
        print(self.type)

class Hero(Team, Typehero):
    def __init__ (self, name, health):
        self.name = name
        self.health = health

jiro = Hero('Jiro', 250)
jiro.setTeam ("Rebelion")
jiro.setType("Front end")

jiro.showTeam()
jiro.showType()