class triangle :
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_wide(self):
        return 0.5 * self.base * self.height

triangle1 = triangle(5, 20)
triangle2 = triangle(4, 30)

print('wide of triangle 1 is:', triangle1.get_wide())
print('wide of triangle 2 is:', triangle2.get_wide())

