import unittest
from divide_and_conquer_algorithms import max_sum, max_sum2  # Import from the main file
from fft import fft, fft2, multiply_polynomials, setAddition # Import fft from the correct file

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
    def test_polinomial_multiplication(self):
        
        coefficient_polynom_1 = [3, 6, 0, 0]
        coefficient_polynom_2 = [-1, 5, 0, 0]

        multiply_polynomials(coefficient_polynom_1, coefficient_polynom_2)
        
class TestFFT2examWS2324(unittest.TestCase):
    # def test_fft2_simple(self):       
    #     coefficient_polynom_1 = [-1, 2, -4, 7]
    #     fft2(coefficient_polynom_1)
    
    def test_set_sum(self):
        A = {0, 2, 3}
        B = {2, 3}
        
        print(setAddition(A, B, 8))

        
if __name__ == "__main__":
    # Create a test suite for only the TestFFT2result class
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFFT2examWS2324)
    
    # Run the test suite
    unittest.TextTestRunner().run(suite)

