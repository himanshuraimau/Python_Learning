class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand   #using __ to make it private
        self.__model = model   #using __ to make it private
        Car.total_car += 1

    def get_brand(self):   #getter
        return self.__brand + " !"  

    def full_name(self):   #getter
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):   #getter
        return "Petrol or Diesel"
    
    @staticmethod   #decorator
    def general_description():   #static method
        return "Cars are means of transport"
    
    @property   #decorator
    def model(self):   #getter
        return self.__model
    


class ElectricCar(Car):  #inheritance
    def __init__(self, brand, model, battery_size):  #overriding
        super().__init__(brand, model)   #calling parent class constructor
        self.battery_size = battery_size

    def fuel_type():   #overriding
        return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")


# print(my_car.general_description())
# print(my_car.model)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)



class Battery:  #composition
    def battery_info(self):  #getter
        return "this is battery"

class Engine:   #composition
    def engine_info(self):  #getter
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):  #multiple inheritance
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())