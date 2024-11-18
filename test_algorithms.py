import unittest
from divide_and_conquer_algorithms import max_sum, SubarrayResult, max_sum2, SubarrayResult2 # Import from the main file

class TestMaxSumArray(unittest.TestCase):
    
    def test_max_sum(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        result = max_sum(array, 0, len(array) - 1)
        self.assertEqual(result.max_sum_value, 6)
        self.assertEqual(result.start, 3)
        self.assertEqual(result.end, 6)
        result = max_sum2(array, 0, len(array) - 1)
        self.assertEqual(result.max_sum_value, 6)
        self.assertEqual(result.start, 3)
        self.assertEqual(result.end, 6)

if __name__ == "__main__":
    unittest.main()  # Run all tests
