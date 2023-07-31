# COUNTER

from collections import Counter

a_list = [1, 2, 2, 3, 4, 4, 4, 10]
a_string = 'CodeFirstGirls'
a_dict = {'a': 5, 'b': 3, 'c': 5, 'd': 5, 'e': 1}

# counting objects

c_list = Counter(a_list)
c_string = Counter(a_string)
c_dict = Counter(a_dict.values())
c1_dict = Counter(a_dict.keys())
print(c_list)
print(c_string)
print(c_dict)
print(c1_dict)