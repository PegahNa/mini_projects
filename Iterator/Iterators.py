# nums = [2, 4, 1, 9, 6]

# nums_iter = iter(nums)
# print(nums_iter)

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))

# what happens next when our list comes to an end?
# uncomment and try

# print(next(nums_iter))

# ALTERNATIVELY  - traversing

# nums_iter = iter({1, 2, 3, 4, 5})
# print(nums_iter.__next__())
# print(nums_iter.__next__())
# print(nums_iter.__next__())
# print(nums_iter.__next__())
# print(nums_iter.__next__())
#
# # this one will throw an error
# #print(nums_iter.__next__())


###########################
'''
The dir() function can be used to see the list of available methods on the iterable object.
'''
# from pprint import pprint as pp
# #
# pp(dir(nums_iter))


###########################

#
# # Create our own ITERATOR
#
# class EvenNumbers:

#     def __iter__(self):
#         self.num = 0
#         return self

#     def __next__(self):

#         self.num += 2
#         return self.num

#
# # run code
#
# evens = EvenNumbers()
# even_iter = iter(evens)
#
#
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))


# First example can dangerously run in infinite loop.
# Let's create a new object with an appropriate condition.

# class EvenNumbers2:
#
#     def __iter__(self):
#         self.num = 0
#         return self
#
#     def __next__(self):
#
#         if self.num < 10:
#
#             self.num += 2
#             return self.num
#         else:
#             raise StopIteration
#
#
# evens = EvenNumbers2()
# even_iter = iter(evens)
# for n in even_iter:
#     print(n)

"""
Create a new CircleSequence class. 
It should accept an iterable, which represents our data source 
and a number, which tells us how many items should be produced.

For example 

c = CircleSequence('xyz', 5)
print(list(c))        # prints x, y, z, x, y

c2 = CircleSequence([1,2], 5)
print(list(c2))        # prints 1,2,1,2,1
"""

