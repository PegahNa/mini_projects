
# NAMED TUPLE

from collections import namedtuple


Person = namedtuple('Person', ['age', 'height', 'name'])

# alternatively

Person1 = namedtuple('Person', 'age height name')

anna = Person(30, 165, 'Anna')
marie_liz = Person1(age=25, height=178, name='Marie Elizabeth')

print(anna.age)
print(anna.name)

'''
The first argument to the namedtuple constructor (in our example 'Person') is the typename. 
It is typical to use the same word for the constructor and the typename, but they can be different:
'''

Human = namedtuple('Person',  'age, height, name')
sophie = Human(40, 175, 'Sophie')
print(sophie)