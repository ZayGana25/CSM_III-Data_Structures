
# Isaiah Lugo
# CSM III - Data Structures
# Date: 11/09/24
# Sorting Assignment: Sorts the list in-place in descending order using selection sort.

def selection_sort(numbers):
   
    n = len(numbers)
    for i in range(n - 1):
        # Assume the current position holds the maximum
        max_idx = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        # Swap if max is not at the current position
        if max_idx != i:
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
        # Print the list after each outer loop iteration
        print(numbers)

# Test cases to verify the implementation
if __name__ == "__main__":
    test_cases = [
        [20, 10, 30, 40], # e.g.
        [7, 8, 3], # e.g.
        [1, 2, 3, 4], # e.g.
        [7, 0, 7], # Extra test cases 
        [-5, 10, -1, 7]  # Extra test cases
    ]
    
    for case in test_cases:
        print(f"Sorting:\n{case}\nThe Output is:")
        selection_sort(case)
        print()  # Blank line for separation between test cases
