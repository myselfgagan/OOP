# Demonstration of encapsulation with public, protected, and private attributes
class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self._age = age           # protected
        self.__salary = 50000     # private

    def show(self):
        print(self.name, self._age, self.__salary)

p = Person("Alice", 30)
p.show()

print(p.name)       # accessible
print(p._age)       # accessible but not recommended
print(p.__salary)   # error (private)

# Public attribute can be accessed and modified from outside the class
print(p.name)  # Direct access
p.name = "Bob"  # Can modify
print(p.name)


# Protected attribute (convention: single underscore) can be accessed but should not be modified from outside the class
class Student:
    def __init__(self):
        self._marks = 85  # protected

class Derived(Student):
    def show_marks(self):
        print("Marks:", self._marks)  # accessible in subclass

s = Student()
print(s._marks)  # technically allowed, but avoid
# Can be accessed outside the class, but it’s discouraged (by convention, not restriction)


# Private attribute (convention: double underscore) cannot be accessed directly from outside the class
# Accessed inside class as self.__var, but outside you must use _ClassName__var
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1000)
acc.show_balance()
acc.deposit(500)
acc.show_balance()

# print(acc.__balance) -> Error
print(acc._BankAccount__balance)  # name-mangling access (not recommended)


# Use case for private attributes with methods to control access
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    # Access via methods (getter/setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount")

    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.__balance}")

acc = BankAccount("Alice", 1000)
acc.show_balance()

acc.deposit(500)
acc.show_balance()

# Direct access (not allowed)
# print(acc.__balance)  # AttributeError

# Access via name mangling (for debugging only)
print(acc._BankAccount__balance)  # works, but not recommended


# Subclasses cannot directly access the parent’s private variable, even though it’s inherited
# If really needed, must use the parent’s getter method or _ParentClassName__var syntax


# A parent class with a private variable (__balance)
# A child class that also defines a variable with the same name (__balance)
# In Parent → it becomes _Parent__balance
# In Child → it becomes _Child__balance


# Class variable vs Instance variable
class Student:
    school_name = "ABC Public School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(Student.school_name)  # Access via class
print(s1.school_name)       # Access via object (shared)
print(s2.school_name)       # Same value

# Modify class variable using class name
Student.school_name = "XYZ International School"
print(s1.school_name)  # reflects in all
print(s2.school_name)  # reflects in all

# Class variables → shared by all instances.
# Instance variables → unique to each object


# Public class variable
class Demo:
    data = 10   # public class variable

print(Demo.data)     # accessible
obj = Demo()
print(obj.data)      # accessible


# Protected class variable
class Demo:
    _count = 5   # protected class variable

class Child(Demo):
    def show(self):
        print(self._count)   # accessible in child

obj = Child()
print(obj._count)   # technically works, but not recommended



# Private class variable
class Demo:
    __secret = 99   # private class variable

    def show(self):
        print(Demo.__secret)   # accessible inside class

class Child(Demo):
    def test(self):
        # print(self.__secret)  # Error: not accessible
        print(self._Demo__secret)  # via name mangling (not recommended)

Demo().show()
print(Demo._Demo__secret) # works (name mangling)
print(Demo.__secret)  # Error: not accessible -> in backend __secret is changed to _Demo__secret



# the same concept applies to methods exactly like it does for variables
class Parent:
    # Public Method
    def show_public(self):
        print("Parent: Public method")

    # Protected Method
    def _show_protected(self):
        print("Parent: Protected method")

    # Private Method
    def __show_private(self):
        print("Parent: Private method")

    # Helper to show internal call to private method
    def call_private(self):
        self.__show_private()  # ✅ Allowed inside class


# Child class inheriting from Parent
class Child(Parent):
    def access_methods(self):
        print("\nInside Child class:")

        # ✅ Public method - freely accessible
        self.show_public()

        # ⚠️ Protected method - accessible, but use only within class or subclass
        self._show_protected()

        # ❌ Private method - not directly accessible (will cause error if uncommented)
        # self.__show_private()

        # ✅ Access private via name mangling (not recommended in practice)
        self._Parent__show_private()


# Create objects
p = Parent()
c = Child()

print("Accessing from Parent object:")
p.show_public()         # ✅ Allowed
p._show_protected()     # ⚠️ Works, but not recommended
# p.__show_private()    # ❌ Not allowed
p.call_private()        # ✅ Access private internally through helper

print("\nAccessing from Child object:")
c.show_public()         # ✅ Allowed (inherited)
c._show_protected()     # ⚠️ Allowed (protected, inherited)
# c.__show_private()    # ❌ Not allowed
c._Parent__show_private()  # ✅ Works via name mangling (not recommended)

c.access_methods()      # ✅ Shows internal access inside subclass

# Summary:
# Public methods/variables: accessible everywhere
# Protected methods/variables: accessible within class and subclasses (by convention)
# Private methods/variables: accessible only within the defining class
# Name mangling allows access but is discouraged outside the class
