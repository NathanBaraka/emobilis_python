class Car:
    def __init__(self,brand,colour):
        self.brand = brand
        self.colour = colour

    def start(self):
        print(f"{self.brand} car is starting")
my_car = Car("BMW","blue")
my_car.start()