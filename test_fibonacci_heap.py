import unittest
from fibonacci_heap import FibonacciHeap

class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        """Setup a new Fibonacci Heap before each test."""
        self.fib_heap = FibonacciHeap()

    def test_insert(self):
        """Test insertion of elements and check min."""
        self.fib_heap.insert(10)
        self.assertEqual(self.fib_heap.min(), 10)
        self.fib_heap.insert(20)
        self.assertEqual(self.fib_heap.min(), 10)
        self.fib_heap.insert(5)
        self.assertEqual(self.fib_heap.min(), 5)
        self.fib_heap.insert(2)
        self.assertEqual(self.fib_heap.min(), 2)

    def test_extract_min(self):
        """Test extract-min operation."""
        self.fib_heap.insert(10)
        self.fib_heap.insert(20)
        self.fib_heap.insert(5)
        self.fib_heap.insert(2)

        min_node = self.fib_heap.delete_min()
        self.assertEqual(min_node.key, 2)
        self.assertEqual(self.fib_heap.min(), 5)

        min_node = self.fib_heap.delete_min()
        self.assertEqual(min_node.key, 5)
        self.assertEqual(self.fib_heap.min(), 10)

    def test_meld(self):
        """Test meld operation between two heaps."""
        heap1 = FibonacciHeap()
        heap1.insert(10)
        heap1.insert(20)
        heap1.insert(5)

        heap2 = FibonacciHeap()
        heap2.insert(15)
        heap2.insert(25)

        heap1.meld(heap2)
        self.assertEqual(heap1.min(), 5)

    def test_empty_extract_min(self):
        """Test extracting min from an empty heap."""
        min_node = self.fib_heap.delete_min()
        self.assertIsNone(min_node)

    def test_visualize(self):
        """Test visualization of the heap structure."""
        # Insert elements into the heap
        self.fib_heap.insert(10)
        self.fib_heap.insert(20)
        self.fib_heap.insert(5)
        self.fib_heap.insert(2)

        # Before consolidation, count root nodes
        root_nodes_before_consolidation = [x for x in self._iterate(self.fib_heap.min_node)]
        print(f"Root nodes before consolidation: {len(root_nodes_before_consolidation)}")

        # Consolidate the heap (this will merge trees of the same degree)
        self.fib_heap._consolidate()

        # After consolidation, count root nodes
        root_nodes_after_consolidation = [x for x in self._iterate(self.fib_heap.min_node)]
        print(f"Root nodes after consolidation: {len(root_nodes_after_consolidation)}")
        
        # Check expected number of root nodes after consolidation
        self.assertEqual(len(root_nodes_after_consolidation), 1)  # Should be 2 after consolidation


    def _iterate(self, start_node):
        """Helper method to iterate through the root list."""
        node = start_node
        while True:
            yield node
            node = node.right
            if node == start_node:
                break

if __name__ == "__main__":
    unittest.main()

