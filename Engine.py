class Engine:
    def __init__(self, cc):
        self.cc = cc
    def start(self):
        return f"Engine {self.cc}cc started"

class Car:
    def __init__(self, brand, cc):
        self.brand = brand
        self.engine = Engine(cc)   # composition (HAS-A)
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = value

    def drive(self):
        return f"{self.brand} driving at {self._speed} km/h"

    def __repr__(self):
        return f"Car(brand={self.brand!r}, speed={self._speed})"

c = Car("Tesla", 2000)
print(c.engine.start())
c.speed = 60
print(c.drive())
print("Object:", c)
