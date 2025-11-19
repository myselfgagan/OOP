# Example demonstrating instance, class, and static methods in Python
class Demo:
    class_var = "I am Class Variable"   # Class variable

    def __init__(self, name):
        self.name = name               # Instance variable

    # Instance Method
    def instance_method(self):
        print("\n[Instance Method]")
        print("Access class var:", Demo.class_var)   # via class
        print("Access class var (via self):", self.class_var)  # also works
        print("Access instance var:", self.name)     # only self works

    # Class Method
    @classmethod
    def class_method(cls):
        print("\n[Class Method]")
        print("Access class var:", cls.class_var)    # works (via cls)
        # print(cls.name)  # Error — instance var not accessible

    # Static Method
    @staticmethod
    def static_method():
        print("\n[Static Method]")
        print("Access class var:", Demo.class_var)   # via class
        # print(self.name)  # Not allowed — no self or cls here
        # print(cls.class_var)  # Not allowed — no cls here

obj = Demo("Alice")

obj.instance_method()
Demo.class_method()
Demo.static_method()


# Output:
# [Instance Method]
# Access class var: I am Class Variable
# Access class var (via self): I am Class Variable
# Access instance var: Alice

# [Class Method]
# Access class var: I am Class Variable

# [Static Method]
# Access class var: I am Class Variable



# Modify Class & Instance Variables
class Demo:
    class_var = 0   # class variable shared by all objects

    def __init__(self, name):
        self.name = name      # instance variable unique to each object

    # Instance Method → modifies instance variable
    def update_instance(self, new_name):
        print(f"\n[Instance Method] Before: {self.name}")
        self.name = new_name
        print(f"[Instance Method] After: {self.name}")

    # Class Method → modifies class variable
    @classmethod
    def update_class(cls, new_value):
        print(f"\n[Class Method] Before: {cls.class_var}")
        cls.class_var = new_value
        print(f"[Class Method] After: {cls.class_var}")

    # Static Method → can access but not auto-bound to cls/self
    @staticmethod
    def show_info():
        print(f"\n[Static Method] Class var: {Demo.class_var}")
        print("Static method cannot modify instance or class vars directly")

a = Demo("Alice")
b = Demo("Bob")

# Show initial values
print(f"Initial -> a.name: {a.name}, b.name: {b.name}, class_var: {Demo.class_var}")

# Instance method modifies only that object’s variable
a.update_instance("Alicia")

# Class method modifies class variable for all
Demo.update_class(100)

# Static method just displays info
Demo.show_info()

# Final check
print(f"\nFinal -> a.name: {a.name}, b.name: {b.name}, class_var: {Demo.class_var}")


# Output:
# Initial -> a.name: Alice, b.name: Bob, class_var: 0

# [Instance Method] Before: Alice
# [Instance Method] After: Alicia

# [Class Method] Before: 0
# [Class Method] After: 100

# [Static Method] Class var: 100
# Static method cannot modify instance or class vars directly

# Final -> a.name: Alicia, b.name: Bob, class_var: 100
