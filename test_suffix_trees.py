from suffix_trees import SuffixTrie
def random_trie_generation():
    t = SuffixTrie()
    t.generate_trie(['a', 'b', 'a', 'b', 'c'])
    t.print_graph("trie")
    # t.visualize()

if __name__ == "__main__":
    random_trie_generation()