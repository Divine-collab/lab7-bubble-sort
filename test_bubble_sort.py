"""
Test suite for bubble sort implementation using unittest.
Tests cover normal cases, edge cases, and various input scenarios.
"""

import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test cases for the bubble_sort function."""
    
    def test_random_unsorted_list(self):
        """Test 1: Sorting a random unsorted list."""
        input_list = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(input_list), expected)
    
    def test_already_sorted_list(self):
        """Test 2: An already sorted list remains sorted."""
        input_list = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(input_list), expected)
    
    def test_reverse_sorted_list(self):
        """Test 3: Sorting a reverse-sorted list (worst case)."""
        input_list = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(input_list), expected)
    
    def test_list_with_duplicates(self):
        """Test 4: Sorting a list with duplicate values."""
        input_list = [3, 1, 3, 2, 1, 3]
        expected = [1, 1, 2, 3, 3, 3]
        self.assertEqual(bubble_sort(input_list), expected)
    
    def test_edge_cases(self):
        """Test 5: Edge cases - empty list, single element, two elements."""
        # Empty list
        self.assertEqual(bubble_sort([]), [])
        
        # Single element
        self.assertEqual(bubble_sort([42]), [42])
        
        # Two elements
        self.assertEqual(bubble_sort([2, 1]), [1, 2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
