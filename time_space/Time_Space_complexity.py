####  Big O notation is a method for determining how fast an algorithm is.

###     Constant Time :  No matter how many elements, it will always take x operations to perform.
###     Logarithmic Time :  A logarithmic algorithm halves the list every time it’s run.
###     Linear Time  :  Linear time algorithms mean that every single element from the input is visited exactly once, O(n) times.
###     Polynomial Time :  For each loop, we go over the list once. For each item in that list, we go over the entire list once.
###                        A polynomial function looks like n2 or n3 and so on.
###     Exponential Time  : Exponential time is 2n, where 2 depends on the permutations involved.



"""
This function runs in O(1) time (or "constant time") relative to its input.
The input list could be 1 item or 1,000 items, but this function would still just require one "step."
"""


def print_first_item(items):
    print(items[0])


"""
This function runs in O(n) time (or "linear time"), where n is the number of items in the list. 
If the list has 10 items, we have to print 10 times. 
If it has 1,000 items, we have to print 1,000 times.
"""


def print_all_items(items):
    for item in items:
        print(item)


"""
Thus this function runs in O(n^2) time (or "quadratic time"). 
If the list has 10 items, we have to print 100 times. 
"""


def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)


"""
This is O(2n), which we just call O(n).
When you're calculating the big O complexity of something, you just throw out the constants.
"""


def print_all_items_twice(items):
    for item in items:
        print(item)

    # Again
    for item in items:
        print(item)


"""
This is O(1 + n/2 + 100), which we just call O(n).
for big O notation we're looking at what happens as n gets arbitrarily large. 
As n gets really big, adding 100 or dividing by 2 has a decreasingly significant effect.
"""


def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items) // 2
    index = 0
    while index < middle_index:
        print(items[index])
        index += 1

    for time in range(100):
        print("hi")


##########################################################

"""
We are going to solve one problem in 3 different ways to see how Time-Space complexity is affected. 

TASK: Find first duplicate value
--------------------------------

Given an array of int between 1 and n, where n is the length of array, write a function that returns
the first int that appears more than once (when we read array left to right)
If no integer appears more than once, then we return -1.

Example 1
---------
input = [2,1,5,2,3,3,4]
output = 2

2 is the first integer that appears more than once. 3 also appears more than once, but 
second 3 appears after second 2. 


Example 2
---------
input = [2,1,5,3,3,2,4]
output = 3

3 is the first integer that appears more than once. 2 also appears more than once, but 
second 2 appears after second 3. 

"""


# SOLUTION 1

# O(n^2) time | O(1) spae --> n is the length of input array

def first_dupe_value1(array):
    min_second_idx = len(array)

    for i in range(len(array)):
        value = array[i]
        for j in range(i + 1, len(array)):
            val_to_compare = array[j]
            if value == val_to_compare:
                min_second_idx = min(min_second_idx, j)

    if min_second_idx == len(array):
        return -1

    return array[min_second_idx]

# TEST CASES
# print(first_dupe_value1([2,1,5,3,3,2,4]))
# print(first_dupe_value1([2,1,5,2,3,3,4]))
