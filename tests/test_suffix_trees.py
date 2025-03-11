import sys
import os

# Add the algorithms directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.suffix_trees import SuffixTrie

def random_trie_generation():
    t = SuffixTrie()
    t.generate_trie(['a', 'b', 'a', 'b', 'c'])
    t.print_graph("trie")
    # t.visualize()

if __name__ == "__main__":
    random_trie_generation()