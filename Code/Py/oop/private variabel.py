class Hero:

    # class variable
    jumlah = 0 #nempel sama Hero

    def __init__(self, name, health) :
        self.name = name
        self.health = health
    # variabel instance nempel sama object(private variable)
        self.__private = "private"
    # variabel instance protected
        self._protected = "protected"
exuq = Hero('Exuq', 100)
print(exuq.__dict__)
exuq._protected = "test"
print(exuq._protected)
