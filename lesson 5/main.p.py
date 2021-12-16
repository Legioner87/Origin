# lesson5

class Base:
    def mowe(self):
        print("Класс Base")


class VehicleBase(Base):
    def __init__(self, ves):
        self.ves = ves
    def mowe(self):
        print("Класс VehicleBase")
    def __str__(self):
        return ( f"вес={self.ves}")

vb= VehicleBase(10)
print(vb)
vb.mowe()

class Ship(VehicleBase):
    def __init__(self, ves, maxves):
        self.ves = ves
        self.maxves = maxves
    def met(self):
        print("Добавлен метод")
    def mowe(self):
        print("Класс Ship")
    def __str__(self):
        return ( f"вес={self.ves}"
                 f" максимальный вес={self.maxves}"
                 )

ship= Ship(10,100)
print(ship)
ship.met()
ship.mowe()

class Plane(Ship):
    def __init__(self, ves, maxves, cargo):
        super().__init__(ves, maxves)
        self.cargo = cargo

    def add_cargo(cargo):
        cargo = [3, 6, 9, 12, 15]

        for num in cargo:
            quotient = num + 5
            print(Plane)
            print(f"{num} + 5, = {int(quotient)}.")

    def mowe(self):
        print("Класс Plane")


plane= Plane(10,100,1000)
print(plane)

plane.mowe()
plane.add_cargo()