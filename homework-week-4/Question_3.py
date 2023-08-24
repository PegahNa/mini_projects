'''
Question 3 is an opportunity for some creative programming to prove your knowledge 
on classes, abstraction and method assignment.

Below is an example solution.
'''

# Import statements are expected...
# math will handle some calculations for us to spare us reinventing the wheel
import math
# abstractmethod will allow us to define a Shape, which all classes going..
# ..forward will conform to.
from abc import abstractmethod

# The definition of the Abstract Class. This alone does nothing,
# rather it is a template for all future classes.
class Shape:
    @abstractmethod
    def calc_perimeter(self):
        pass
    
    @abstractmethod
    def calc_area(self):
        pass


'''
    The Square class is expecting the following OOP measures to be
    in place:
    - Derived from Shape, noted by the argument passed to the class declaration
    - A declaration for side A. Since all sides are equal, no need to any more.
    - the calc_perimeter function returns the length of the side multiplied by 4
    - the calc_area to return the the length of the side multiplied by 2
'''
class Square(Shape):
    def __init__(self, a):
        self.a = a
    
    def calc_perimeter(self):
        return self.a * 4
    
    def calc_area(self):
        return self.a * 2

'''
    Much like the Square, the similiar is expected here of the Rectangle Class.
    - Derived from Shape
    - A declaration for side A and side B.
    - the calc_perimeter function returns the length of opposing sides multiplied by 2, 
        then added together. Remember your BODMAS/BIDMAS for this! 
    - the calc_area to return the the length of the two different sides multiplied by
        each other
'''
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calc_perimeter(self):
        return (self.a * 2) + (self.b * 2)
    
    def calc_area(self):
        return self.a * self.b


'''
    Triangle here is a little trickier and unless you recall the maths from school,
    will likely have required a little research.
    - The height of a triangle and the base length will be needed. Consider a right angle
        triangle a rectangle/square cut in two diagonally. Just like the correct way to cut 
        a sandwich. (I'll die on that hill.)
    With the above values, we can perform the calculations for perimeter and area.
    - The perimeter is calculated by take the length of the base and the height, but then
        you need to find the distance between the tips of the base and length.
        To do this, you take the height^2 + the base^2 and find the square root of that
        value. Why? Because Maths. If you struggle with any level of Maths, take this,
        it's dangerous to go alone: https://www.wolframalpha.com/
    - Finally, to calculate the area, it's essentially half the value of a rectangles area,
        as mentioned above in reference to cutting a sandwich. So the length of the base 
        multipled by the height divided by 2, or multiplied by 0.5.
'''
class RightAngledTriangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    
    def calc_perimeter(self):
        return self.height + self.base + math.sqrt(self.height**2 + self.base**2)
    
    def calc_area(self):
        return 0.5 * self.height * self.base
    

# In order to ascertain you've written code that works, you'd usually manually check it.
# below are a few examples to play around with to ensure the above code is understood.
s = Square(6)
print(s.calc_perimeter())
# should get 24
print(s.calc_area())
# should get 12
r = Rectangle(6, 4)
print(r.calc_perimeter())
# should get 20
print(r.calc_area())
# should get 24
t = RightAngledTriangle(9,12)
print(t.calc_perimeter())
# should get 36
print(t.calc_area())
# should get 54