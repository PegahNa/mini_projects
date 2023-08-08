'''
    THE THEORY OF COLLISION!

    We already looked at pushing tuples into a simplified Hash Table concept.
    Let's have a play around and see if we can devise a way of handling the 
    collision concept ourselves.

    If each entry in our simple hash table was a list, perhaps we could store more values 
    than one in each slot..?

    Using this concept, try to create your own version of collision management.

    There is some starter code below that pushes multiple entries into a simple hash table.
    Expand this so each slot can handle multiple entries.
'''

class Flavour:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        id = 0
        for char in self.name:
            id += ord(char) 
        return id

    def __eq__(self, other):
        return self.__hash__(self.name) == self.__hash__(other.name)
    
list_of_flavours = [
    Flavour('grape'),
    Flavour('mixedberry'),
    Flavour('blackberry'),
    Flavour('strawberry'),
    Flavour('apple'),
    Flavour('banana'),
    Flavour('nabaan')
]


###########################
## Expand this function! ##
###########################
def create_hash_table_from_list(list):
    hash_table = {}
    for val in list:
        print('Collision Management and updating Hash Table goes here...')
    return hash_table


###########################
##  Check your results!  ##
###########################

print(create_hash_table_from_list(list_of_flavours))