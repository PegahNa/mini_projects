# # STACK
#
#
# class StackList:
#     """
#     Stack Implementation using a List
#     """
#
#     def __init__(self, size):
#         self.container = [None] * size
#         self.capacity = size
#         self.top = -1
#
#     def push(self, x):
#         """
#         Method to add an element `x` to the stack
#         """
#         if self.is_full():
#             print("Stack is full! Calling exit()…")
#             exit(1)
#
#         print("Inserting", x, "into the stack…")
#         self.top = self.top + 1
#         self.container[self.top] = x
#
#     def pop(self):
#         """
#         Method to pop a top element from the stack
#         """
#         if self.is_empty():
#             print("Stack is empty! Calling exit()…")
#             exit(1)
#
#         print("Removing", self.peek(), "from the stack")
#
#         # decrease stack size by 1 and (optionally) return the popped element
#         top = self.container[self.top]
#         self.top = self.top - 1
#         return top
#
#     def peek(self):
#         """
#         Method to return the top element of the stack
#         """
#         if self.is_empty():
#             exit(1)
#         return self.container[self.top]
#
#     def size(self):
#         """
#         Method to return the size of the stack
#         """
#         return self.top + 1
#
#     def is_empty(self):
#         return self.size() == 0
#
#     def is_full(self):
#         return self.size() == self.capacity
#
#
# # SHOW EXAMPLES BELOW, then encourage students to try out different methods.
# stack = StackList(3)
#
# stack.push(1)
# stack.push(2)
#
# stack.pop()
# stack.pop()
#
# stack.push(3)
#
# print("Top element is", stack.peek())
# print("The stack size is", stack.size())
#
# stack.pop()
#
# if stack.is_empty():
#     print("The stack is empty")
# else:
#     print("The stack is not empty")


#####################################################
#
# """
# Stack implementation using deque class in Python
# """
#
from collections import deque

# NB: module deque alredy has useful methods, so we don't need to re-implement them
stack = deque()


stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4')
print(stack)

print("Top element is", stack[-1])  # prints the stack's top (4)

print("Removing", stack.pop(), "from the stack")  # removing the top element (4)
print("Removing", stack.pop(), "from the stack")  # removing the next top (3)

# returns the total number of elements present in the stack
print("Stack size is", len(stack))

print("Removing", stack.pop(), "from the stack")  # removing the top element (2)
print("Removing", stack.pop(), "from the stack")  # removing the next top (1)

# check if the stack is empty
if len(stack) == 0:
    print("The stack is empty")
else:
    print("The stack is not empty")
