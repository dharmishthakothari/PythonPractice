# W.A.P to using super() in inheritance. 
class Vehical:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayDetails(self):
        print(f"{self.name} have {self.model} Model")
class Bike(Vehical):
    def __init__(self,name,model,price,tyre):
        super().__init__(name,model)
        self.price=price
        self.tyre=tyre
    def displayDetails(self):
        super().displayDetails()
        print(f"And this Bike having {self.tyre} tyre and selling value is {self.price} Rs.")
class Car(Vehical):
    def __init__(self,name,model,price,tyre):
        super().__init__(name,model)
        self.price=price
        self.tyre=tyre
    def displayDetails(self):
        super().displayDetails()
        print(f"And this Car having {self.tyre} tyre and selling value is {self.price} Rs.")
objBike=Bike("Honda","Shine",200000,2)
objBike.displayDetails()
objCar=Car("Kia","Seltos",2000000,4)
objCar.displayDetails()