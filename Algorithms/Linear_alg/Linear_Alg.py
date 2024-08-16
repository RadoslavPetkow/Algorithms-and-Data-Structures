def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Examples
examples = [
    ([1, 2, 3, 4, 5], 3),            # Example 1: target found in the middle
    ([10, 20, 30, 40, 50], 10),      # Example 2: target found at the beginning
    ([100, 200, 300, 400, 500], 500),# Example 3: target found at the end
    ([5, 10, 15, 20, 25], 7),        # Example 4: target not found
    ([7, 7, 7, 7, 7], 7),            # Example 5: all elements are the target
    ([3, 1, 4, 1, 5, 9], 4),         # Example 6: target found in the middle with unsorted list
    ([], 1),                         # Example 7: empty list
    ([2], 2),                        # Example 8: single element list, target found
    ([1, 3, 5, 7, 9], 8),            # Example 9: odd number list, target not found
    (['a', 'b', 'c', 'd'], 'c')      # Example 10: list of strings, target found
]

for i, (arr, target) in enumerate(examples, 1):
    result = linear_search(arr, target)
    if result != -1:
        print(f"Example {i}: Target '{target}' found at index {result} in list {arr}.")
    else:
        print(f"Example {i}: Target '{target}' not found in list {arr}.")