# Define a function to calculate the n'th Fibonacci number
def fibonacci(n):
    # Base case: Fibonacci number at index 0 is 0
    if n <= 0:
        return 0
    # Base case: Fibonacci number at index 1 is 1
    elif n == 1:
        return 1
    else:
        # Recursive case: Sum of the previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Define a function to calculate the sum of even Fibonacci values within a limit
def sum_even_fibonacci(limit):
    # Generate a list of Fibonacci values up to the limit index
    fibonacci_values = [fibonacci(i) for i in range(limit)]
    # Filter the even Fibonacci values from the list
    even_fibonacci_values = [val for val in fibonacci_values if val % 2 == 0]
    # Calculate the sum of the even Fibonacci values
    sum_even_values = sum(even_fibonacci_values)
    return sum_even_values

# Example usage
# Set the limit to 10
limit = 10
# Call the sum_even_fibonacci function to get the result
result = sum_even_fibonacci(limit)
# Print the result
print("Sum of even Fibonacci values within the limit:", result)