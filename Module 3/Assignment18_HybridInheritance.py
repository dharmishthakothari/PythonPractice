# W.A.P to show Hybrid inheritance. 
class Vehical:
    def __init__(self,name,model):
        print(name,model)
class Bike(Vehical):
    def details(self,price,tyre):
        print(f"having {tyre} tyre and is of {price} price")
class Car(Vehical):
    def details(self,price,tyre):
        print(f"having {tyre} tyre and is of {price} price")
objBike=Bike("Honda","Shine")
objBike.details(200000,2)
objCar=Car("Kia","Seltos")
objCar.details(2000000,4)