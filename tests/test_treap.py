import unittest
import sys
import os

# Add the algorithms directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.treap import Treap, TreapNode

class TestTreap(unittest.TestCase):
    def test_random_tree_generation(self):
        t = Treap(TreapNode(70))
        Treap.clear_snapshots()
        t.insert(TreapNode(65))
        t.insert(TreapNode(46))
        t.insert(TreapNode(37))
        t.insert(TreapNode(22))
        # Add assertions to verify the structure of the tree
        self.assertIsNotNone(t.root)

    def test_generate_tree_24_1(self):
        t241 = Treap(TreapNode(3, 7))
        Treap.clear_snapshots()
        t241.insert(TreapNode(4, 3))
        t241.insert(TreapNode(5, 10))
        t241.insert(TreapNode(2, 1))
        t241.insert(TreapNode(1, 4))
        node = t241.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 2)
        t241.delete(4)

    def test_generate_exam_tree_WS2324(self):
        tws2324 = Treap(TreapNode(8, 3))
        Treap.clear_snapshots()
        tws2324.insert(TreapNode(2, 6))
        tws2324.insert(TreapNode(11, 7))
        tws2324.insert(TreapNode(1, 9))
        tws2324.insert(TreapNode(5, 8))
        tws2324.delete(8)

if __name__ == "__main__":
    unittest.main()