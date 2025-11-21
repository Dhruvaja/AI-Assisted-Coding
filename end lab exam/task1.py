import unittest

# ----------------------
# Basic Bubble Sort
# ----------------------
def bubble_sort(arr):
    """
    Sort a list of integers in ascending order using Bubble Sort.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    list: Sorted list in ascending order.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# ----------------------
# Bubble Sort with Swap Counting
# ----------------------
def bubble_sort_with_swaps(arr):
    """
    Sort a list of integers in ascending order using Bubble Sort
    and count the number of swaps performed.

    Parameters:
    arr (list): List of integers to sort.

    Returns:
    tuple: (sorted list, number of swaps performed)
    """
    n = len(arr)
    swap_count = 0  # Initialize swap counter
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements and increment swap counter
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return arr, swap_count

# ----------------------
# Unit Tests
# ----------------------
class TestBubbleSort(unittest.TestCase):
    def test_basic_bubble_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]),
                         [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]),
                         [1, 2, 4, 5, 8])
        self.assertEqual(bubble_sort([3, 3, 2, 1, 0]),
                         [0, 1, 2, 3, 3])

    def test_bubble_sort_with_swaps(self):
        sorted_arr, swaps = bubble_sort_with_swaps([64, 34, 25, 12, 22, 11, 90])
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 34, 64, 90])
        self.assertIsInstance(swaps, int)
        
        sorted_arr, swaps = bubble_sort_with_swaps([5, 1, 4, 2, 8])
        self.assertEqual(sorted_arr, [1, 2, 4, 5, 8])
        self.assertIsInstance(swaps, int)

        sorted_arr, swaps = bubble_sort_with_swaps([3, 3, 2, 1, 0])
        self.assertEqual(sorted_arr, [0, 1, 2, 3, 3])
        self.assertIsInstance(swaps, int)

    def test_edge_cases(self):
        # Empty list
        self.assertEqual(bubble_sort([]), [])
        sorted_arr, swaps = bubble_sort_with_swaps([])
        self.assertEqual(sorted_arr, [])
        self.assertEqual(swaps, 0)

        # Single element
        self.assertEqual(bubble_sort([42]), [42])
        sorted_arr, swaps = bubble_sort_with_swaps([42])
        self.assertEqual(sorted_arr, [42])
        self.assertEqual(swaps, 0)

# ----------------------
# Run Unit Tests
# ----------------------
if __name__ == "__main__":
    unittest.main()