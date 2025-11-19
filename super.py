# Demonstration of super() to call parent class method
class Person:
    def show(self):
        print("Parent show()")

class Student(Person):
    def show(self, value=None):
        # Call parent version logic
        super().show()      # calls the next 'show()' method in the inheritance chain
        # Then child version logic
        if value:
            print("Child show():", value)

p1 = Student()
p1.show()           # Parent show()
p1.show("Hello")    # Parent show() + Child show(): Hello


# Another example with additional logic before and after calling parent method
# we can call super at any point in the method
class Person:
    def show(self):
        print("Parent show()")

class Student(Person):
    def show(self, value=None):
        print("Before calling parent")   # like pre-decorator logic -> but it's not a decorator
        super().show()                    # call parent method
        print("After calling parent")    # like post-decorator logic -> but it's not a decorator
        if value:
            print("Child show():", value)