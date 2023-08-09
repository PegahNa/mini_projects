# SIMPLE RECURSIVE FUNCTION

def print_pattern(num):
    if num < 1:
        return
    else:
        print(num, end=" ")
        print_pattern(num - 1)
        print(num, end=" ")
        return

# Driver Code
my_number = 5
print_pattern(my_number)


#
# ########################################
#
# # FACTORIAL
#
# """
# E.g. factorial of 6 (6!) is 1*2*3*4*5*6 = 720
# """
#
#
# def get_factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * get_factorial(x - 1)
#
#
# num = 6
# print("The factorial of", num, "is", get_factorial(num))
# #
#

# ###########################################
#
# # FIBONACCI
# """
# Fibonacci series of 5 is : 0 1 1 2 3
#
# """
#
#
# def fib(n):

#     if n == 0:
#         return 0


#     if n == 1 or n == 2:
#         return 1


#     else:
#         return fib(n - 1) + fib(n - 2)

# n = 6
# print("The fibonacci of", n, "is", fib(n))

#
# #######################################################
#  QUESTION
# """
# Return all possible combinations of strings of given length,
# which can be formed from a set of supplied characters.
#
# Input:
# char_set = {'a', 'b'}, length = 3
#
# Output:
# aaa
# aab
# aba
# abb
# baa
# bab
# bba
# bbb
#
# NB: we cannot use itertools product or permutations functions.
# """
#