# W.A.P to show Multiple inheritance. 
class Mother:
    def cooking(self):
        print("Mother cooks well")
class Father:
    def singing(self):
        print("Father sings well")
class Child(Mother,Father):
    def playing(self):
        print("Child plays well")
objChild=Child()
objChild.cooking()
objChild.singing()
objChild.playing()