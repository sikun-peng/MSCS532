# insertion_sort.py
# MSCS532 - Week 1 Assignment
# Implements the insertion sort algorithm in Python for sorting in decreasing order

def insertion_sort_desc(arr):
    """
    Sorts the input list in-place in decreasing (monotonically descending) order using insertion sort.

    Parameters:
    arr (List[int]): A list of integers to be sorted.

    Returns:
    List[int]: The same list, sorted in decreasing order.
    """
    # Traverse the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]      # Current element to insert into the sorted part of the list
        j = i - 1         # Index of the last element in the sorted portion

        # Shift elements of the sorted portion that are less than the key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shift the element one position to the right
            j -= 1               # Move backward in the sorted portion

        # Insert the key at the correct position
        arr[j + 1] = key

    return arr  # Return the sorted list (descending order)

# Run this code only if the script is executed directly
if __name__ == "__main__":
    # Sample input list of integers
    data = [9, 2, 44, 21, 1, 5]

    # Print the original list
    print("Original array:", data)

    # Sort the list in decreasing order
    sorted_data = insertion_sort_desc(data)

    # Print the sorted list
    print("Sorted array (descending):", sorted_data)