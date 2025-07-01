# test_sort.py
# Unit tests for insertion_sort_desc from insertion_sort.py

import unittest
from insertion_sort import insertion_sort_desc

class TestInsertionSortDescending(unittest.TestCase):
    
    def test_already_sorted(self):
        """Test list already in descending order"""
        self.assertEqual(insertion_sort_desc([9, 7, 5, 3, 1]), [9, 7, 5, 3, 1])

    def test_ascending_input(self):
        """Test list in ascending order"""
        self.assertEqual(insertion_sort_desc([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_random_order(self):
        """Test list with random values"""
        self.assertEqual(insertion_sort_desc([4, 2, 9, 1, 6]), [9, 6, 4, 2, 1])

    def test_with_duplicates(self):
        """Test list with duplicate values"""
        self.assertEqual(insertion_sort_desc([5, 3, 5, 2, 5]), [5, 5, 5, 3, 2])

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(insertion_sort_desc([42]), [42])

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(insertion_sort_desc([]), [])

    def test_negative_numbers(self):
        """Test list with negative values"""
        self.assertEqual(insertion_sort_desc([-1, -3, -2, 0]), [0, -1, -2, -3])

if __name__ == '__main__':
    unittest.main()