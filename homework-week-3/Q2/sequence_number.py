def num_in_seq(n):
    # Calculate the nth term of the sequence using the formula: nth_term = first_term + (n - 1) * common_difference
    nth_term = 8 + (n - 1) * 7
    return nth_term

# Test the function
print(num_in_seq(1))   # Output: 8
print(num_in_seq(5))   # Output: 36
print(num_in_seq(10))  # Output: 71
