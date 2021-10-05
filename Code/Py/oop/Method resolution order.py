# 
class A:
    def show(self):
        print("ini adalah huruf A")
class B:
    def show(self):
        print("inn adalah huruf B")
class C(B, A):
    pass

objec = C()
objec.show()
