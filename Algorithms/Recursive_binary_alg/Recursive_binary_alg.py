def recursive_binary_search(arr, target, left, right):
    if right >= left:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid
        # If the target is greater, search the right half
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, mid + 1, right)
        # If the target is smaller, search the left half
        else:
            return recursive_binary_search(arr, target, left, mid - 1)

    # Target was not present in the array
    return -1


# Wrapper function for the recursive binary search
def binary_search(arr, target):
    return recursive_binary_search(arr, target, 0, len(arr) - 1)


# Examples
examples = [
    ([1, 2, 3, 4, 5], 3),  # Example 1: target found in the middle
    ([10, 20, 30, 40, 50], 10),  # Example 2: target found at the beginning
    ([100, 200, 300, 400, 500], 500),  # Example 3: target found at the end
    ([5, 10, 15, 20, 25], 7),  # Example 4: target not found
    ([7, 7, 7, 7, 7], 7),  # Example 5: all elements are the target (first occurrence)
    ([3, 4, 5, 6, 7], 4),  # Example 6: target found near the start
    ([], 1),  # Example 7: empty list
    ([2], 2),  # Example 8: single element list, target found
    ([1, 3, 5, 7, 9], 8),  # Example 9: target not found in odd numbered list
    (['a', 'b', 'c', 'd'], 'c')  # Example 10: list of strings, target found
]

for i, (arr, target) in enumerate(examples, 1):
    result = binary_search(arr, target)
    if result != -1:
        print(f"Example {i}: Target '{target}' found at index {result} in list {arr}.")
    else:
        print(f"Example {i}: Target '{target}' not found in list {arr}.")