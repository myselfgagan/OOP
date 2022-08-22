from this import d
from traceback import StackSummary
from unicodedata import name


class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()    # creating object for the inner class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class Laptop:
        
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Gagan", 3)
s2 = Student("piddi", 6)

s1.show()

s1.lap.brand

lap1 = s1.lap    # accessing the object created in the outer class
lap2 = s2.lap

lap3 = Student.Laptop()  # creating the object for the inner class, outside of the class