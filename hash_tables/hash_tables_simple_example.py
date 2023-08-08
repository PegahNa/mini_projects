# # hash for integer unchanged
# print('Hash for 100 is:', hash(100))
# # hash for decimal
# print('Hash for 100.55 is:', hash(100.55))
# # hash for string
# print('Hash for CFG is:', hash('CFG'))
# # hash for tuple
# word = ('g', 'i', 'r', 'l', 's')
# print('The hash is:', hash(word))


'''
    Let's take a look at a class based implementation of creating a student that can generate a hash value.
'''

# class CFGStudent:

#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name

#     def __hash__(self):
#         return hash((self.age, self.name))


# person = CFGStudent(30, 'Nina')
# person_2 = CFGStudent(30, 'Nina')
# print(hash(person))

# print(hash(person))
# print(person.__hash__())
# print(person.__hash__() == hash(person))
# print(person.__eq__(person_2))
# print((30, 'Nina') == (30, 'Nina'))


'''
    Now lets look at a super simplified Hash function.
'''

# my_hash_table = {}
# my_hash_table = HashTable
# print("Initialised Hash Table:", my_hash_table)

# # Let's create an ID from our Tuple that we can use to store a value and..
# # retrieve it again...
# def super_simple_hashing_function(age, name):
#     id = 0
#     for char in name:
#         id += ord(char) # Ord() gives us the ascii value of the character
#     return age + id

# Nina = (30, 'Nina')
# Inna = (30, 'Inna')
# John = (13, 'John')

# ninas_simple_hash = super_simple_hashing_function(*Nina)
# innas_simple_hash = super_simple_hashing_function(*Inna)
# johns_simple_hash = super_simple_hashing_function(*John)

# print("Nina's Simple Hash Value:", ninas_simple_hash)
# my_hash_table[ninas_simple_hash] = Nina
# my_hash_table[innas_simple_hash] = Inna
# my_hash_table[johns_simple_hash] = John

# print("Hash Table after assignment:", my_hash_table)

