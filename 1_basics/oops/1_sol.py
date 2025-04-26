class Car: 
    total_car=0

    def __init__(self,brand, model):                 # constructor
        self.__brand = brand                         # making private  to brand using __ (Encaplusation)
        self.__model = model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand +"!"                     # getter method 

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model


class Electric_car(Car):                             # inheretance
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"    

# my_tesla= Electric_car("Tesla","Model S","85kWh")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,Electric_car))




# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())


# my_car = Car("Toyota","Corolla")
# my_car.model="city"

# print(my_car.brand)                                   # this will give error because brand is private 
# print(my_car.model )
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(my_car.total_car)
# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)                               # this will give error because brand is private 
# print(my_new_car.model)
# print(Car.total_car)
# print(my_car.general_description())
# print(Car.general_description())



class Battery:                                         # multiple inheretance
    def battery_info(self):
        return "this is battery "


class Engine:
    def enginne_info(self):
        return "this is engine "



class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla =ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.enginne_info())
print(my_new_tesla.battery_info())