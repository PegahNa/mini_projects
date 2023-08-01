
# GENERATOR

# The generator has the following syntax in Python:
    # def function_name():
#             yield statement



# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

    # x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))


# A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
#
# g = my_gen()
# next(g)
# next(g)
# next(g)

# this will throw an error
# next(g)


# GENERATOR EXPRESSION
#
# my_list = [1, 3, 6, 10]
#
# # NOTE: we square each term using list comprehension
# new_list = [x ** 2 for x in my_list]
#
# # NOTE: same thing can be done using a generator expression
# # generator expressions are surrounded by parenthesis () !
# generator = (x ** 2 for x in my_list)
#
# print(new_list)
# print(generator)
#
#
#
# # use next() or for loop to get items from generator
#
# for i in generator:
#     print(i)

###########################################

"""
Generators are easier to implement. 
Rule of thumb: iterators to create classes, generators to create functions. 
Compare example below. 
"""


# ITERATOR

#
# class PowerThreeSequence:
#
#     def __init__(self, max_items=0):
#         self.n = 0
#         self.max = max_items
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n >= self.max:
#             raise StopIteration
#
#         result = 3 ** self.n
#         self.n += 1
#         return result

# my_iter = PowerThreeSequence(5)
# for i in my_iter:
#     print(i)
#
#
# # GENERATOR
#
def power_three_sequence(max_items=0):
    n = 0
    while n < max_items:
        yield 3 ** n
        n += 1

my_generator = power_three_sequence(5)
for i in my_generator:
    print(i)
