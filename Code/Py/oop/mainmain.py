class Hero : #template
    # class variable
    jumlah = 0  
    def __init__(self, inputName, inputHealth, inputAtack,inputDefense) :\
        # instance variable artinya variabel dibawah ini hanya dimiliki oleh class Hero saja
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAtack
        self.defense = inputDefense

        # method tanpa return dan tanpa argumen
    def dare(self):
        print("My name is " + self.name)

        # method dengan argumen tanpa return
    def healthUp(self, up):
        self.health += up
         
        # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Fuxy", 175, 90, 50)
hero2 = Hero("Yuri", 150, 100, 25)
hero3 = Hero("Welsy", 100, 120, 10)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

hero1.dare()
hero1.healthUp(2)
print(hero1.getHealth())

# hero1 = Hero() # object atau instance                   
# hero2 = Hero()
# hero3 = Hero()


# hero1.nama = "Fuxy" # atribut
# hero1.health = 250

# hero2.name = "Yuri"
# hero2.health = 200

# hero3.name = "Welsy"
# hero3.health = 175


# print(hero1.__dict__)    