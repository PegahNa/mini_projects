# This line imports the abc module from the Python standard library. The abc module stands for Abstract Base Classes and is used to define abstract base classes (ABCs) and abstract methods.
import abc  

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod   #This is a decorator from the abc module, and it is used to define abstract methods. 
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented:", perim)
        return perim

# Create instances of the classes and call calc_perimeter method
triangle_instance = Triangle(3, 4, 5)
triangle_instance.calc_perimeter()

# shape_instance = Shape()  # This will raise an error