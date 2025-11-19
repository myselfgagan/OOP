# Function Overloading is not directly supported in Python.
# However, we can achieve similar behavior using default arguments or *args and **kwargs.
class Person: 
    def __init__(self,name,age): 
        self.name=name 
        self.age=age 

    def show(self): 
        print(f"Name: {self.name}, Age: {self.age}") 
        
    def show(self, value):      # This will redifine the previous show method not overload it
        print(f"value: {value}")

p1=Person("Alice",30) 
p1.show("Hello") 
p1.show() # This will raise an error because show() without arguments is not defined


# To achieve function overloading behavior, we can use default arguments
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self, value=None):
        if value is None:
            print(f"Name: {self.name}, Age: {self.age}")
        else:
            print(f"value: {value}")

p1 = Person("Alice", 30)
p1.show("Hello")   # value: Hello
p1.show()          # Name: Alice, Age: 30


# Using *args to achieve function overloading behavior
class Person:
    def show(self, *args):
        if len(args) == 0:
            print("No value")
        elif len(args) == 1:
            print("Value:", args[0])
        else:
            print("Multiple values:", args)

p1 = Person()
p1.show()                # No value
p1.show("Hello")         # Value: Hello
p1.show(1, 2, 3)         # Multiple values: (1, 2, 3)


# Method Overriding Example
class Person:
    def show(self):
        print("Parent show()")

class Student(Person):  
    def show(self):     # This will override the show method of Person class
        print("Child show()")

s1 = Student()
s1.show()  # This will call the show method of Student class