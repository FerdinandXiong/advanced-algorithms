import graphviz
import os

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None  # Used in McCreight's Algorithm
        self.leaf = None

class SuffixTreeLeaf:
    def __init__(self, suffix):
        self.suffix = suffix

class SuffixTree:
    def __init__(self, text):
        self.text = text + "$"  # Append sentinel character
        # should actually start with a Leaf with the suffix as the root
        self.root = None
        self.build_tree()

    def build_tree(self):
        """Implements McCreight's algorithm for suffix tree construction with scan and rescan."""
        n = len(self.text)
        active_node = self.root # we need something with root = leaf as start
        last_created_internal = None
        
        for i in range(n):  # Iterate through suffixes
            suffix = self.text[i:]
            print(f"suffix {i} = {suffix}")
            
            current_node = active_node
            
            # we need to compute the head 
            head_index = 0
            # for T0, head is empty
            char = suffix[0]
            # iterate through the nodes for the suffix
            while hasattr(current_node, "children") and char in current_node.children:
                # look                    
                current_node = current_node.children[char]
            
            # set head for suffix and the rest as Leaf
            head = suffix[:head_index]
            print(f"head {i} = {head}")
            leaf_suffix = suffix[head_index:]
            current_node.children[char] = SuffixTreeNode(leaf_suffix)
            print(f"leaf has been created with suffix {leaf_suffix}")
            
            current_node.leaf = i  # Mark leaf with suffix index
            
            if last_created_internal:
                last_created_internal.suffix_link = current_node
            
            last_created_internal = self.rescan_and_scan(active_node)
            self.capture_snapshot(f"Step {i}")  # Generate Graphviz snapshot
    
    def capture_snapshot(self, description=""):
        """Generate Graphviz visualization at a given step."""
        dot = graphviz.Digraph(format="png")
        self._add_edges(dot, self.root)
        self._add_suffix_links(dot, self.root)
        
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"suffix_tree_{description}")
        dot.render(filename=filename, format="png", cleanup=True)
        print(f"Captured snapshot: {filename}.png - {description}")

    def _add_edges(self, dot, node, parent_id=None, edge_label=""):
        node_id = str(id(node))
        label = "Internal" if node.leaf is None else f"Leaf: {node.leaf}"
        dot.node(node_id, label=label, shape="box" if node.leaf is not None else "ellipse")
        
        if parent_id:
            dot.edge(parent_id, node_id, label=edge_label)
        
        for char, child in node.children.items():
            self._add_edges(dot, child, node_id, edge_label=char)
    
    def _add_suffix_links(self, dot, node):
        node_id = str(id(node))
        if node.suffix_link:
            suffix_id = str(id(node.suffix_link))
            label = f"{self._get_suffix_link_label(node)}"
            dot.edge(node_id, suffix_id, style="dotted", color="blue", label=label)
        
        for child in node.children.values():
            self._add_suffix_links(dot, child)
    
    def _get_suffix_link_label(self, node):
        """Generate label for suffix link based on x? notation."""
        for char, child in node.children.items():
            if child.suffix_link:
                return f"{char}? -> ?"
        return "?"




