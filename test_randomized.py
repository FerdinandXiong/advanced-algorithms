import unittest
from randomized_algorithms import quicksort, naive_is_prime, simple_primality_test

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        quicksort(array, 0, len(array) - 1)
        self.assertEqual(array, [-5, -3, -2, -1, 1, 1, 2, 4, 4])
        
class TestNaivePrime(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(naive_is_prime(7), True)
        self.assertEqual(naive_is_prime(7919), True)
        self.assertEqual(naive_is_prime(122), False)
        self.assertEqual(naive_is_prime(49), False)
        self.assertEqual(naive_is_prime(341), False)
        
class TestSimplePrime(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(simple_primality_test(7), True)
        self.assertEqual(simple_primality_test(7919), True)
        self.assertEqual(simple_primality_test(122), False)
        self.assertEqual(simple_primality_test(49), False)
        # special test: base 2 pseudoprime number: 341
        # though composite, should not be detected by simple primality test
        self.assertEqual(simple_primality_test(341), False)
              
if __name__ == "__main__":
    unittest.main()  # Run all tests