class Car:
    def __init__(self, model,  price, speed):
        self.model = model
        self._price = price
        self.__speed = speed


some_car = Car("Subaru Impreza", 400000, 220)
print(some_car.model)
print(some_car._price)
print(some_car.__speed)