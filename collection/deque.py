# DEQUE
# NB: this can be done in console


from collections import deque
d = deque('CodeFirst')

for elem in d:
    print(elem.upper())

d.append('!')
d.appendleft('*')

print(d)

print ("Pop : ")
d.pop()
print(d)

print ("Popleft : ")
d.popleft()
print(d)

print ("Extend : ")
d.extend('123')
print(d)

print ("Rotate : ")
d.rotate(1)
print(d)

d.rotate(-1)
print(d)

d.clear()

# this will throw error as we cannot pop from empty deque
# d.pop()

print ("New list: ")
d.extendleft('abc')
print(d)