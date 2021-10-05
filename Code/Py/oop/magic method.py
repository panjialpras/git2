import os
class Ruin:
# magic method
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power # langsung dieksekusi saat pembuatan class

    def __repr__(self):
        return "D E B U G - Ruin: {} with health: {} and power: {}".format(self.name, self.health, self.power)
    def __str__(self):
        return "Udah jadi - Ruin: {} with health: {} and power: {}".format(self.name, self.health, self.power)
    def __add__(self, obyek):
        # Dipake kalo buat aritmatika
        return self.power + guard.power
    @property
    def __dict__(self):
        return 'objek ini punya nama, darah, dan kekuatan'

guard = Ruin('Ruin Guard', 100000, 2300)
guard2 = Ruin('Ruin Hunter', 120000, 2500)

os.system('cls')
print(repr(guard))
print(guard)
print(guard.power + guard2.power)
print(guard2.__dict__)

