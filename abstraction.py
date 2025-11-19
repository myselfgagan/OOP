# Demonstration of abstraction using ABC module
# An abstract class cannot be instantiated and may contain abstract methods that must be implemented by subclasses
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # No implementation here (just a rule)

class Car(Vehicle):
    def start(self):
        print("Car started")

c = Car()
c.start()

# If a subclass does not implement all abstract methods, it cannot be instantiated
class Bike(Vehicle):
    pass

b = Bike()  # This will raise an error because Bike does not implement start()