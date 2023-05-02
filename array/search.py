def linear_search(arr, target):
    """
    Search for the target value in the array using linear search.
    Time complexity: O(n), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    # Iterate through the array using the enumerate function, which returns both the index and the value at that index.
    for index, value in enumerate(arr):
        # Check if the current value is equal to the target value.
        if value == target:
            # If the target value is found, return its index.
            return index

    # If the target value is not found, return -1.
    return -1


def binary_search(arr, target):
    """
    Search for the target value in a sorted array using binary search.
    Time complexity: O(log n), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    # Set the initial left and right boundaries of the search interval.
    left, right = 0, len(arr) - 1

    # Continue searching while the search interval is not empty.
    while left <= right:
        # Calculate the middle index of the current search interval.
        mid = (left + right) // 2

        # Check if the middle value is equal to the target value.
        if arr[mid] == target:
            # If the target value is found, return its index.
            return mid
        # Check if the middle value is less than the target value.
        elif arr[mid] < target:
            # If so, update the left boundary to the index after the middle index.
            left = mid + 1
        else:
            # Otherwise, update the right boundary to the index before the middle index.
            right = mid - 1

    # If the target value is not found, return -1.
    return -1


# Example usage:
example_array = [10, 20, 30, 40, 50]
target = 30

print("Linear search:")
index = linear_search(example_array, target)
print(f"Index of target value {target}: {index}")

print("\nBinary search (sorted array required):")
index = binary_search(example_array, target)
print(f"Index of target value {target}: {index}")
