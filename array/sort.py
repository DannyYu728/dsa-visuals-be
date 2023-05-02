def bubble_sort(arr):
    """
    Sort an array using bubble sort.
    Time complexity: O(n^2), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    n = len(arr)
    # Iterate through the array.
    for i in range(n):
        # Flag to check if any elements were swapped during the inner loop.
        swapped = False
        # Iterate through the remaining unsorted elements.
        for j in range(0, n - i - 1):
            # Compare the current element with the next element.
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True to indicate a swap occurred.
                swapped = True
        # If no elements were swapped during the inner loop, the array is already sorted.
        if not swapped:
            break

def selection_sort(arr):
    """
    Sort an array using selection sort.
    Time complexity: O(n^2), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    n = len(arr)
    # Iterate through the array.
    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part of the array.
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the element at the current position.
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
def insertion_sort(arr):
    """
    Sort an array using insertion sort.
    Time complexity: O(n^2), where n is the number of elements in the array.
    Space complexity: O(1), no additional space is used.
    """
    n = len(arr)
    # Iterate through the array starting from the second element.
    for i in range(1, n):
        # Store the current element and its index.
        key = arr[i]
        j = i - 1
        # Move elements of the sorted part of the array that are greater than the key to one position ahead.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at its correct position in the sorted part of the array.
        arr[j + 1] = key
        
def merge_sort(arr):
    """
    Sort an array using merge sort.
    Time complexity: O(n log n), where n is the number of elements in the array.
    Space complexity: O(n), additional space for the auxiliary array is used.
    """
    def merge(left, right):
        """
        Merge two sorted arrays.
        """
        result = []
        i = j = 0

        # Merge elements from both arrays by comparing and appending the smaller element.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append the remaining elements from the left array, if any.
        result.extend(left[i:])
        # Append the remaining elements from the right array, if any.
        result.extend(right[j:])
        
        return result

    # Base case: return the array if its length is less than or equal to 1.
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves.
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted left and right halves and return the result.
    return merge(left, right)

def quick_sort(arr):
    """
    Sort an array using quick sort.
    Time complexity: O(n log n) average case, O(n^2) worst case, where n is the number of elements in the array.
    Space complexity: O(log n), due to recursive call stack.
    """
    def partition(low, high):
        """
        Partition the array using the pivot.
        """
        pivot = arr[high]
        i = low - 1

        # Iterate through the elements in the range [low, high].
        for j in range(low, high):
            # If the current element is smaller than or equal to the pivot, increment i and swap arr[i] with arr[j].
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Swap the pivot with the element at index i + 1.
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort(low, high):
        """
        Recursive function for quick sort.
        """
        if low < high:
            # Find the partition index.
            pi = partition(low, high)

            # Recursively sort the elements before and after the partition index.
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    # Call the recursive quick sort function with the initial low and high indices.
    _quick_sort(0, len(arr) - 1)
                           
# Example usage:
example_array = [64, 34, 25, 12, 22, 11, 90]

print("Bubble sort:")
bubble_sort(example_array)
print(example_array)

print("\nSelection sort:")
example_array = [64, 34, 25, 12, 22, 11, 90]
selection_sort(example_array)
print(example_array)

print("\nInsertion sort:")
example_array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(example_array)
print(example_array)

print("\nMerge sort:")
example_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = merge_sort(example_array)
print(sorted_array)

print("\nQuick sort:")
example_array = [64, 34, 25, 12, 22, 11, 90]
quick_sort(example_array)
print(example_array)
