import unittest
import sys
import os

# Add the algorithms directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.randomized_algorithms import quicksort, naive_is_prime, simple_probably_prime_test, randomized_primality_test, fast_exponent, fast_exponent_mod, miller_rabin_test

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
        self.assertEqual(simple_probably_prime_test(7), True)
        self.assertEqual(simple_probably_prime_test(7919), True)
        self.assertEqual(simple_probably_prime_test(122), False)
        self.assertEqual(simple_probably_prime_test(49), False)
        # special test: base 2 pseudoprime number: 341
        # though composite, should not be detected by simple primality test
        # => false positive
        self.assertEqual(simple_probably_prime_test(341), True)
        
class TestRandomizedPrime(unittest.TestCase):
    def test_randomized(self):
        self.assertEqual(randomized_primality_test(7), True)
        self.assertEqual(randomized_primality_test(7919), True)
        self.assertEqual(randomized_primality_test(122), False)
        self.assertEqual(randomized_primality_test(49), False)
        # special test: charmichael number: 561
        # though composite, will not always be detected 
        # => should create false positive
        self.assertEqual(randomized_primality_test(561), True)
        
class TestFastExponent(unittest.TestCase):
    def test_fast_exponent(self):
        self.assertEqual(fast_exponent(4, 7), 4**7)
        
    def test_fast_exponent_mod(self):
        self.assertEqual(fast_exponent_mod(4, 7, 5), pow(4, 7, 5))

class TestMillerRabin(unittest.TestCase):
    def test_miller_rabin(self):
        self.assertEqual(miller_rabin_test(7), True)
        self.assertEqual(miller_rabin_test(7919), True)
        self.assertEqual(miller_rabin_test(122), False)
        self.assertEqual(miller_rabin_test(49), False)
        # special test: charmichael number: 561
        # though composite, should be detected 
        # => should not create false positive
        self.assertEqual(miller_rabin_test(561), False)
              
if __name__ == "__main__":
    unittest.main()  # Run all tests