class Car:

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand


class Brand:

    def __init__(self, model, cars):
        self.model = model
        self.cars = cars

    def change(self, car):
        if car.brand == self.model:
            self.cars.append(car.model)

    def info(self):
        print('Brand:' + str(self.model) + '; cars:' + str(self.cars))

first_car = Car("Corolla", "Toyota")
second_car = Car("Supra", "Toyota")
third_car = Car("Nissan", "Sunny")
some_brand = Brand("Toyota", [])

some_brand.info()
some_brand.change(first_car)
some_brand.info()
some_brand.change(second_car)
some_brand.info()
some_brand.change(third_car)
some_brand.info()

