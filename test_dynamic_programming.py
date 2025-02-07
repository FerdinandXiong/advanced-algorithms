import unittest
from dynamic_programming import max_money, path_max_money, weight_sum_possible

class TestQuicksort(unittest.TestCase):
    def test_money(self):
        input = [
            [5, 3, 2, 1],
            [1, 2, 10, 4],
            [4, 3, 2, 20],
            [2, 1, 3, 1]
        ]
        print(path_max_money(input))
    
    def test_weight(self):
        weights = {1, 3, 6, 8}
        target = 13
        print (weight_sum_possible(weights, target))
        
if __name__ == "__main__":
    unittest.main()