# W.A.P to create a class and access the property of class using object. 
class A:
    a=10
    def displayA(self):
        print(self.a)
objA = A()
print(objA.a)
objA.displayA()