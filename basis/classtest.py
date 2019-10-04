#!python3
#学习python类特性
class Docter():

    intx=0
    inty=0

    def set(self,intx,inty):
        self.intx=intx
        self.inty=inty

    def add(self):
        return self.intx+self.inty

    def multiplication(self):
        return self.intx*self.inty


myclass=Docter()

print(myclass.set(3,5))
print(myclass.add())
print(myclass.__dict__)
print(Docter.__dict__)
print(myclass.multiplication())

