###############################################

# QUEUE

"""
Queue Implementation using a List
"""


class MyQueue:

    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to the front element in the queue
        self.rear = -1  # rear points to the last element in the queue
        self.count = 0  # current size of the queue

    def pop(self):
        if self.is_empty():
            print("Queue Underflow!! Terminating process.")
            exit(1)

        print("Removing element…", self.q[self.front])

        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def append(self, value):
        if self.is_full():
            print("Queue is full! Terminating process.")
            exit(1)

        print("Inserting element…", value)

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def peek(self):
        if self.is_empty():
            print("Queue is empty!! Terminating process.")
            exit(1)

        return self.q[self.front]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

# RUN QUEUE



q = MyQueue(5)

q.append(1)
q.append(2)
q.append(3)

print("The queue size is", q.size())
print("The front element is", q.peek())
q.pop()
print("The front element is", q.peek())

q.pop()
q.pop()

if q.is_empty():
    print("The queue is empty")
else:
    print("The queue is not empty")


"""
Queue implementation using deque class in Python
"""

# NB: module deque alredy has useful methods, so we don't need to re-implement them

from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("The front element is", queue[0])  # 1

queue.popleft()  # removing the front element (1)
queue.popleft()  # removing the front element (2)

# Print front item of the queue
print("The front element is", queue[0])  # 3

print("The queue size is", len(queue))  # 2

# check whether the queue is empty
if len(queue) == 0:
    print("The queue is empty")
else:
    print("The queue is not empty")