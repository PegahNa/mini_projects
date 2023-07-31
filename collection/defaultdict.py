### Example 1

# Python program to demonstrate
# dictionary


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Dictionary:")
print(Dict)
print(Dict[1])

# Uncommenting this
#print(Dict[4])
# will raise a KeyError as the
# 4 is not present in the dictionary

##### Sometimes, when the KeyError is raised, it might become a problem.
# To overcome this Python introduces another dictionary like container known as Defaultdict
# which is present inside the collections module.

# Python program to demonstrate
# defaultdict
#
#
# from collections import defaultdict
#
#
# # Function to return a default
# # values for keys that is not
# # present
# def def_value():
#     return "Not Present"
#
#
# # Defining the dict
# d = defaultdict(def_value)
# d["a"] = 1
# d["b"] = 2
#
# print(d["a"])
# print(d["b"])
# print(d["c"])



#### Example 2
# DEFAULTDICT

# string example
# from collections import defaultdict
#
# state_capitals = defaultdict(str)
# print(state_capitals)
#
# state_capitals['Alaska']
# print(state_capitals)
#
# # list example
#
# basket = [('Fruit', 'Pear'), ('Vegetable', 'Tomato'), ('Fruit', 'Peach')]
# dd = defaultdict(list)
#
# for k, v in basket:
#     dd[k].append(v)
#
# print(dd)