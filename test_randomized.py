import unittest
from randomized_algorithms import quicksort

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        quicksort(array, 0, len(array) - 1)
        self.assertEqual(array, [-5, -3, -2, -1, 1, 1, 2, 4, 4])
        
if __name__ == "__main__":
    unittest.main()  # Run all tests