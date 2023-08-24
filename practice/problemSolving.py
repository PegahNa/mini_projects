# Define a function that checks if the second array is a subsequence of the first array
def is_subsequence(main_array, sub_array):
    # Initialize indices for tracking positions in the main and sub arrays
    main_index = 0
    sub_index = 0
    
    # Iterate through the main array and sub array
    while main_index < len(main_array) and sub_index < len(sub_array):
        # Compare the current element of main array with the current element of sub array
        if main_array[main_index] == sub_array[sub_index]:
            # If a match is found, move to the next element in the sub array
            sub_index += 1
        # Move to the next element in the main array
        main_index += 1
        
    # Check if all elements in the sub array were found in the main array
    return sub_index == len(sub_array)

# Example usage
main_array = [1, 2, 3, 4, 5, 6, 7]
sub_array1 = [1, 3, 5]
sub_array2 = [2, 4, 6]
sub_array3 = [0, 1, 2, 3, 4]

# Check if sub arrays are valid subsequences and print the results
print(is_subsequence(main_array, sub_array1))  # True
print(is_subsequence(main_array, sub_array2))  # True
print(is_subsequence(main_array, sub_array3))  # False