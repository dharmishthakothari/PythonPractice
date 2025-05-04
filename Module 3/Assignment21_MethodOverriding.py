# W.A.P to show Method overriding.
class Base:
    def show(self):
        print("in Base class")
class Derived(Base):
    def show(self):
        print("in Derived class")
class AnotherDerived(Base):
    pass

objBase=Base()
objBase.show()
objDerived=Derived()
objDerived.show()
objADerived=AnotherDerived()
objADerived.show()