###################################################################
#1. Add strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.

num1 = '257'
num2 = '2754'

#Expected Output = 3011



###################################################################
# 2. Move zeros

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]  # --> should be [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  # --> should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]


##################################################################
# 3. Prime numbers array

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.

"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

interval_num = 44

# Expected Output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]