# W.A.P to show single inheritance. 
class Base:
    def greet(self):
        print("Good Morning!!!")
class Derived(Base):
    pass
objDerived = Derived()
objDerived.greet()
objBase = Base()
objBase.greet()
