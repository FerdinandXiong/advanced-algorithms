import unittest
import sys
import os

# Add the algorithms directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.fibonacci_heap import FibonacciHeap

class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        """Setup a new Fibonacci Heap before each test."""
        self.fib_heap = FibonacciHeap()

    def test_sheet_10(self):
        """Test extract-min operation."""
        self.fib_heap.insert(13)
        self.fib_heap.insert(40)
        self.fib_heap.insert(8)
        self.fib_heap.insert(15)
        self.fib_heap.insert(22)        
        self.fib_heap.insert(37)
        self.fib_heap.insert(19)
        self.fib_heap.insert(5)
        self.fib_heap.insert(45)
        self.fib_heap.insert(27)
        self.fib_heap.delete_min()       
        self.fib_heap.decrease_key(self.fib_heap.min_node.right, 7)        
        self.fib_heap.decrease_key(self.fib_heap.min_node.child.right.child, 16)       
        self.fib_heap.delete_min()
        
    # def test_meld(self):
    #     """Test meld operation between two heaps."""
    #     heap1 = FibonacciHeap()
    #     heap1.insert(10)
    #     heap1.insert(20)
    #     heap1.insert(5)

    #     heap2 = FibonacciHeap()
    #     heap2.insert(15)
    #     heap2.insert(25)

    #     heap1.meld(heap2)
    #     self.assertEqual(heap1.min(), 5)

    # def test_empty_extract_min(self):
    #     """Test extracting min from an empty heap."""
    #     min_node = self.fib_heap.delete_min()
    #     self.assertIsNone(min_node)

if __name__ == "__main__":
    unittest.main()