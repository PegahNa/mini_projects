# CHAIN MAP

from collections import  ChainMap

# define two dictionaries with at least some keys overlapping.
dict1 = {'apple': 1, 'banana': 5, 'nuts':3 }

dict2 = {'coconut': 2, 'date': 1, 'apple': 3,  'banana': 2, 'nuts':10}

# create two ChainMaps with different ordering of those dicts.
combined_dict = ChainMap(dict1, dict2)
reverse_ordered_dict = ChainMap(dict2, dict1)

print(combined_dict)

for k, v in combined_dict.items():
    print(k, v)


print(reverse_ordered_dict)

for k, v in reverse_ordered_dict.items():
    print(k, v)