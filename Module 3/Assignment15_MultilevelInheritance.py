# W.A.P to show Multilevel inheritance. 
class Base:
    def greet(self):
        print("Good Morning!!!")
class Derived(Base):
    pass
class AnotherDerived(Derived):
    pass
obj1 = AnotherDerived()
obj1.greet()
obj2 = Derived()
obj2.greet()
obj3 = Base()
obj3.greet()