class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("car stopped..")


class Mercidies(Car):
    def __init__(self , name):
        self.name = name

car1 = Mercidies("Mahindra")
car2 = Mercidies("Lenovo")

print(car1.start())

