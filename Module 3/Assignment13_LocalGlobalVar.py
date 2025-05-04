# W.A.P to create local variable and global variable. 
class A:
    b=100
    def displayAB(self):
        a=10
        print("a =",a)
        print("b = ",self.b)
        global b
        b=1000
        print("b= ",b)
    def displayB(self):
        print("b = ",b)
objA = A()
print(objA.b)
objA.displayAB()
objA.displayB()