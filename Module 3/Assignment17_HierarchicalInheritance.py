# W.A.P to show Hierarchical inheritance. . 
class Bird:
    def __init__(self,name):
        print("Bird : ",name)
class Parrot(Bird):
    def fly(self):
        print("Bird can Fly!!!")
class Penguin(Bird):
    def fly(self):
        print("Bird can not fly!!!")
objParrot=Parrot("Parrot")
objParrot.fly()
objPenguin=Penguin("Penguin")
objPenguin.fly()