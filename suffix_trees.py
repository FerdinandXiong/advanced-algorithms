class TrieNode:
    def __init__(self):
        self.children = {}  # Stores character → TrieNode or TrieLeaf
        self.leaf = None  # Holds a reference to a leaf node if it's the end of a word

    def generate_trie(self, suffix, index):
        """Recursively inserts a suffix into the trie."""
        character_node = self.children.get(suffix[index])

        if character_node is None:  # Case 1: Create new nodes for this suffix
            current_node = self
            while index < len(suffix) - 1:
                current_node.children[suffix[index]] = TrieNode()
                current_node = current_node.children[suffix[index]]
                index += 1
            current_node.children[suffix[index]] = TrieLeaf(suffix)  # Attach leaf node
        elif isinstance(character_node, TrieLeaf):  # Case 2: Conflict with a leaf node
            existing_suffix = character_node.key
            new_internal_node = TrieNode()

            # Determine the first mismatch position in the existing suffix
            mismatch_index = index
            while mismatch_index < len(existing_suffix) and mismatch_index < len(suffix) and \
                    existing_suffix[mismatch_index] == suffix[mismatch_index]:
                new_internal_node.children[suffix[mismatch_index]] = TrieNode()
                new_internal_node = new_internal_node.children[suffix[mismatch_index]]
                mismatch_index += 1

            # Add the existing leaf and new suffix as children
            new_internal_node.children[existing_suffix[mismatch_index]] = character_node  # Old leaf
            new_internal_node.children[suffix[mismatch_index]] = TrieLeaf(suffix)  # New suffix

            # Replace the old leaf with the new internal node
            self.children[suffix[index]] = new_internal_node
        else:  # Case 3: Continue traversal
            character_node.generate_trie(suffix, index + 1)


class TrieLeaf:
    def __init__(self, suffix):
        self.key = suffix  # Store the full suffix


import graphviz
import os

class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()

    def generate_trie(self, character_list):
        """Generates a suffix trie from a given character list."""
        for i in range(len(character_list)):
            current_suffix = character_list[i:]  # Extract the suffix
            self.root.generate_trie(current_suffix, 0)

    def _add_edges(self, dot, node, parent_id=None, edge_label=""):
        """Recursively adds edges to Graphviz DOT object."""
        node_id = str(id(node))  # Unique identifier

        if isinstance(node, TrieLeaf):
            dot.node(node_id, label=f"Leaf: {node.key}", shape="box", style="filled", fillcolor="lightgray")
        else:
            dot.node(node_id, label="Internal")

        if parent_id:
            dot.edge(parent_id, node_id, label=edge_label)

        if isinstance(node, TrieNode):  # Only recurse if it's an internal node
            for char, child in node.children.items():
                self._add_edges(dot, child, node_id, edge_label=char)

    def print_graph(self, filename="suffix_tree"):
        """Generates and saves a visualization of the suffix tree using Graphviz."""
        dot = graphviz.Digraph(format="png")
        self._add_edges(dot, self.root)

        # Ensure output directory exists
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Save Graphviz visualization
        filepath = os.path.join(output_dir, filename)
        dot.render(filepath)
        print(f"Suffix tree saved to {filepath}.png")


                