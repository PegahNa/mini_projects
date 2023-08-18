from collections import deque

def process_queue(input_filename):  # Use a valid parameter name
    queue = deque()

    with open(input_filename, 'r') as f:
        for line in f:
            command, name = line.strip().split()
            if command == 'JUMP':
                queue.appendleft(name)
            elif command == 'JOIN':
                queue.append(name)

    return list(queue)

def main():
    input_filename = 'input.txt'  # Change this to the actual path if needed
    final_order = process_queue(input_filename)  # Use the correct parameter name

    print("Final order of the queue:")
    for person in final_order:
        print(person)

if __name__ == "__main__":
    main()

    # Time Complexity: O(n), where n is the number of lines in the input file.
# - Reading the input file takes O(n) time.
# - The loop that processes each line takes O(n) time.
# - Appending to the left of a deque (`appendleft`) or appending to the right (`append`) takes O(1) time.
# Hence, overall time complexity is O(n).

# Space Complexity: O(n)
# - The `queue` deque holds the names of people, and its size could be at most n.
# - The `final_order` list also stores the names of people, taking O(n) space.
# Hence, overall space complexity is O(n).

# Assumptions:
# - The input file format is as described in the task, with lines starting with either "JUMP" or "JOIN" followed by a name.
# - There are no constraints on the length of the names.