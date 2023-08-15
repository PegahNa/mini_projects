###################################################################
# 1. Monotonic Array

# Given an array of integers, determine whether the array is monotonic or not.

"""
An array is monotonic if and only if it is monotone increasing, or monotone decreasing
"""

A = [100, 6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7, 11, 22]

# Expected Output =  True   False   True


##################################################################
# 2. Matched  / Mismatched words

# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'CFG Nano has engineering and data science streams'
sentence2 = 'As part of engineering we are learning about algorithms and data structures'

# Expected Output = (['As', 'CFG', 'Nano', 'about', 'algorithms', 'are', 'has', 'learning', 'of', 'part', 'science', 'streams', 'structures', 'we'], ['and', 'data', 'engineering'])



##################################################################
# 3. Prime numbers array

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.

"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

interval_num = 44

# Expected Output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]