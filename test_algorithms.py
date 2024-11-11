import unittest
from divide_and_conquer_algorithms import max_sum_array, SubarrayResult  # Import from the main file

class TestMaxSumArray(unittest.TestCase):
    
    def test_max_sum(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = max_sum_array(array, 0, len(array) - 1)
        self.assertEqual(result.max_sum, 6)
        self.assertEqual(result.start, 3)
        self.assertEqual(result.end, 6)

if __name__ == "__main__":
    unittest.main()  # Run all tests
