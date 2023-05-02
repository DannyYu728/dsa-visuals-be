def linear_traversal(arr):
    """
    Linearly traverse an array from the first element to the last.
    Time complexity: O(n), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    # Iterate through the array using the enumerate function, which returns both the index and the value at that index.
    for index, value in enumerate(arr):
        # Print the current index and value.
        print(f"Index: {index}, Value: {value}")


def reverse_traversal(arr):
    """
    Traverse an array in reverse order, from the last element to the first.
    Time complexity: O(n), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    # Calculate the length of the array.
    length = len(arr)

    # Iterate through the array from the last index to the first index (in reverse order).
    for index in range(length - 1, -1, -1):
        # Get the value at the current index.
        value = arr[index]
        # Print the current index and value.
        print(f"Index: {index}, Value: {value}")


# Example usage:
example_array = [10, 20, 30, 40, 50]

print("Linear traversal:")
linear_traversal(example_array)

print("\nReverse traversal:")
reverse_traversal(example_array)
