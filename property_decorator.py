# Using @property, @<var>.setter, and @<var>.deleter
class Student:
    def __init__(self, name, marks):
        self.__name = name      # private variable
        self.__marks = marks    # private variable

    # --------------------
    # Getter (for name)
    @property
    def name(self):
        print("Getting name...")
        return self.__name

    # Setter (for name)
    @name.setter
    def name(self, new_name):
        print("Setting name...")
        if len(new_name) > 1:
            self.__name = new_name
        else:
            print("Name too short! Ignored.")

    # Deleter (for name)
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self.__name

    # --------------------
    # Getter for marks (read-only)
    @property
    def marks(self):
        return self.__marks

s1 = Student("Alice", 85)

print(s1.name)        # calls getter
s1.name = "Bob"       # calls setter
print(s1.name)

s1.name = "A"         # rejected by setter condition

del s1.name           # calls deleter

print(s1.marks)       # read-only property (no setter)

# Output:
# Getting name...
# Alice
# Setting name...
# Getting name...
# Bob
# Setting name...
# Name too short! Ignored.
# Deleting name...
# 85




# Parent has a property → Child overrides it
class Parent:
    @property
    def value(self):
        return "Parent value"


class Child(Parent):
    @property
    def value(self):
        return "Child value"

c = Child()
print(c.value)  # Output: Child value




# Child extends Parent’s property (using parent logic + adds extra)
class Parent:
    @property
    def data(self):
        return "Parent Data"


class Child(Parent):
    @property
    def data(self):
        parent_value = super().data     # call parent property
        return parent_value + " + Child Data"

c = Child()
print(c.value)  # Output: Parent Data + Child Data




# Parent has full property (getter + setter) → Child overrides setter only
class Parent:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

class Child(Parent):
    @Parent.age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        else:
            print("Setting age from child")
            super(Child, Child).age.fset(self, value)   # or equivalently: Parent.age.fset(self, value)
            # super(Child, Child) -> This gives us access to the parent property from the child class definition
            # super(Child, Child).age -> gives you the parent property object    
            # Every property object internally has:
            # fget → getter function
            # fset → setter function
            # fdel → deleter function

c = Child()
c.age = 10   # uses child's setter
print(c.age) # uses parent's getter




# Parent has a read-only property → Child can make it writable
class Parent:
    @property
    def x(self):
        return 10


class Child(Parent):
    @Parent.x.setter
    def x(self, value):
        print("Child setting x (parent was read-only)")
        self._x = value

c = Child()
c.x = 50     # now writable



# Override only the getter (keep parent's setter)
class Parent:
    def __init__(self):
        self.__age = 20

    @property
    def age(self):
        print("Parent getter")
        return self.__age

    @age.setter
    def age(self, v):
        print("Parent setter")
        self.__age = v


class Child(Parent):
    @Parent.age.getter
    def age(self):
        # call parent's getter, then extend/modify result
        parent_val = super(Child, Child).age.fget(self)
        print("Child getter modifying value")
        return parent_val + 5


c = Child()
print(c.age)    # uses Child getter (which calls Parent getter internally)
c.age = 30      # uses Parent.setter (unchanged)
print(c.age)

# Output:
# Parent getter
# Child getter modifying value
# 25
# Parent setter
# Parent getter
# Child getter modifying value
# 35





# Override only the deleter (keep getter/setter)
class Parent:
    def __init__(self):
        self.__data = "secret"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, v):
        self.__data = v

    @data.deleter
    def data(self):
        print("Parent deleter called")
        del self.__data


class Child(Parent):
    @Parent.data.deleter
    def data(self):
        print("Child: pre-delete cleanup")
        # call parent's deleter
        super(Child, Child).data.fdel(self)
        print("Child: post-delete steps")


ch = Child()
print(ch.data)
del ch.data

# Output:
# secret
# Child: pre-delete cleanup
# Parent deleter called
# Child: post-delete steps
