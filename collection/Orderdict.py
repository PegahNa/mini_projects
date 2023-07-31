# ORDEREDDICT

from collections import OrderedDict

d = OrderedDict([('apple', 5), ('orange', 6)])
#d = OrderedDict([('app', 1),('apple', 5), ('orange', 6)])
print(d)

d['mango'] = 9
print(d)

d['kiwi'] = 7
print(d)

d['melon'] = 8
print(d)



# create empty OrderedDict and populate

o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)