class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car is Starting....")

    @staticmethod
    def Stop():
        print("Car Stopped!")

class lenovo(Car):
    def __init__(self,brand,type):
        self.brand = brand
        super().__init__(type)
        super().start()

car1 = lenovo("Toyota","electric")
print(car1.start())
print(car1.type)
