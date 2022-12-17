# This is a Python trial program for classes
# Qianbo Yin



# Second trial class - Point
class Point:
    # class string literal - __docstring__
    """This is a class representing a point in the Cartesian coordinate"""

    # initializer method / constructor
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def print_coordinate(self):
        print("(", self.x, ",", self.y, ")")

class Student:
    """This is a class representing a university student"""

    def __init__(self, name_in):
        self.name = name_in

    def __str__(self):
        return "Hahaha"


a = Student("Grayson")
print(a)
# Execution of the program
second_point = Point(2, 3)
second_point.print_coordinate()
