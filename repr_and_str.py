# Demonstration of __repr__ and __str__ methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"  # Debug/Developer

    def __str__(self):
        return f"{self.name} ({self.age} years old)"  # User-friendly

p1 = Person("Alice", 30)

print(p1)         # Calls __str__
print(str(p1))    # Calls __str__
print(repr(p1))   # Calls __repr__

# Output:
# Alice (30 years old)
# Alice (30 years old)
# Person(name='Alice', age=30)

# __repr__ is used for debugging and development -> Person(name='Alice', age=30)
# __str__ is for end-user display -> Alice (30 years old)


# If __str__ is not defined, Python falls back to __repr__
class Demo:
    def __repr__(self):
        return "Demo()"

d = Demo()
print(d)      # Falls back to __repr__
