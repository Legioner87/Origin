#lesson 6
#weight (int, вес автомобиля),
#started (bool, состояние “заведён” или нет),
#fuel (int, условное количество оставшегося топлива),
#fuel_consumption (int, условное значение, сколько единиц топлива расходуется на единицу расстояния)

class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

class Car:

    def __init__(self,weight,started,fuel,fuel_consump):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consump = fuel_consump

    def start(self):
        try:
            if not(self.started):
                if self.fuel > 0:
                    self.started = 1
                    print("Drive")
                else:
                    raise LowFuelError
        except(LowFuelError):
            print("Исключение: Fuel empty")
        else:
            print("Drive. Fuel: ",self.fuel, "liters")

    def move(self,distance):
        try:
            if self.fuel < self.fuel_consump * distance:
                raise NotEnoughFuel
        except(NotEnoughFuel):
            self.fuel -= self.fuel_consump * distance
            print("Исключение: Fuel empty",self.fuel,", need ",self.fuel_consump * distance, "liter's" )
        else:
            self.fuel -= self.fuel_consump * distance
            print("Fuel to: ",self.fuel, "km")

print("Пример 1: если топлива было 50, а расход 5, то проехав 10 у нас остаётся топлива на 0 км. ")
car = Car(weight=100,started=0,fuel=50,fuel_consump=5)
car.start()
car.move(10) # дистанция
print("")
print("Пример 2: если топлива было 10, расход 3, мы хотим проехать 2, топлива должно остаться на 4 км. ")
car = Car(weight=1000,started=0,fuel=10,fuel_consump=3)
car.start()
car.move(2)