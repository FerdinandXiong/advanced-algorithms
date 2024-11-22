import unittest
from divide_and_conquer_algorithms import max_sum, max_sum2  # Import from the main file
from fft import fft, fft2 # Import fft from the correct file
from sympy import I, pi, exp, symbols
from sympy import simplify

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

class TestFFT(unittest.TestCase):
    def test_fft_simple(self):
        input_array = [3, 6, 0, 0]
        output = fft(input_array)
        # Test the length of the output
        self.assertEqual(len(output), len(input_array))
        # Test the DC component (sum of input values)
        self.assertAlmostEqual(output[0].real, sum(input_array), places=6)
        self.assertAlmostEqual(output[0].imag, 0.0, places=6)
        
class TestFFT2result(unittest.TestCase):
    def test_fft_simple(self):
        from sympy import simplify

        input_array = [3, 6, 0, 0]
        output = fft2(input_array)

        # Test the length of the output
        self.assertEqual(len(output), len(input_array))

        # Test the DC component (sum of input values)
        expected_dc = sum(input_array)  # Sum of all inputs
        output_real, output_imag = output[0].as_real_imag()  # Get real and imaginary parts symbolically

        # Assert that real part matches expected DC value, and imaginary part is zero
        self.assertTrue(simplify(output_real - expected_dc) == 0)  # Symbolic check
        self.assertTrue(simplify(output_imag) == 0)  # Imaginary part should be 0

if __name__ == "__main__":
    unittest.main()  # Run all tests

