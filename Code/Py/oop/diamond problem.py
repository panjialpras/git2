# dimaond problem
class A:
    def show(self):
        print('ini adalah show A')
class B(A):
    def show(self):
        print('ini adalah show B')
class C(A):
    def show(self):
        print('ini adalah show C')

class Y(B, C):
    # def show(self):
    #     print('ini adalah show Y')
    pass

objek = Y()
objek.show()
help(objek)