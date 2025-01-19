import random
from graphviz import Digraph  # Importing Graphviz for visualization

class treap_node():
    def __init__(self, key):
        self.key = key
        self.value = random.randint(1, 100)
        self.left_child = None
        self.right_child = None
        self.parent = None
        
        print(f"Created node with key {self.key} and value {self.value}")
        
    def insert(self, treap_node):
        if treap_node.key < self.key:
            if self.left_child is None:
                self.left_child = treap_node
                treap_node.parent = self
                treap_node.restore_heap_property()
            else:
                self.left_child.insert(treap_node)
        # implement right child logic
        else:
            if self.right_child is None:
                self.right_child = treap_node
                treap_node.parent = self
                treap_node.restore_heap_property()
            else:
                self.right_child.insert(treap_node)
                    
    def restore_heap_property(self):
        print("restoring heap property")
        #implement logic
        if self.parent != None:
            if self.parent.value > self.value:
                if self.parent.key > self.key:
                # implement rotations
                    self.rotate_right()
                else:
                    self.rotate_left()
                self.restore_heap_property()
                    
                
    def rotate_right(self):
        print("rotating right")
        self.parent.left_child = self.right_child
        if self.right_child: 
            self.right_child.parent = self.parent
        self.right_child = self.parent
        self.parent = self.parent.parent
        if self.parent:
            self.parent.left_child = self
        self.right_child.parent = self
        
    def rotate_left(self):
        print("rotating left")
        self.parent.right_child = self.left_child
        if self.left_child:
            self.left_child.parent = self.parent
        self.left_child = self.parent
        self.parent = self.parent.parent
        if self.parent:
            self.parent.left_child = self
        self.left_child.parent = self
    
def to_dot(self, graph=None):
    """Generates a dot string representation of the treap (to be used in Graphviz)."""
    if graph is None:
        graph = Digraph('Treap', node_attr={'shape': 'circle'}, graph_attr={'rankdir': 'TB'})
    
    # Add the current node
    graph.node(str(self.key), label=f'{self.key}\n{self.value}')
    
    # Add edges for children, adding invisible nodes for better alignment
    if self.left_child:
        graph.edge(str(self.key), str(self.left_child.key))
        self.left_child.to_dot(graph)
    elif self.right_child:  # Add an invisible left child to balance the node
        invisible_node = f"invisible_{self.key}_L"
        graph.node(invisible_node, style='invisible')  # Invisible node
        graph.edge(str(self.key), invisible_node, style='invisible')  # Invisible edge
    
    if self.right_child:
        graph.edge(str(self.key), str(self.right_child.key))
        self.right_child.to_dot(graph)
    elif self.left_child:  # Add an invisible right child to balance the node
        invisible_node = f"invisible_{self.key}_R"
        graph.node(invisible_node, style='invisible')  # Invisible node
        graph.edge(str(self.key), invisible_node, style='invisible')  # Invisible edge
    
    return graph

    
class treap():
    def __init__(self, root):
        self.root = root
        
    def insert(self, treap_node):
        print(f"insert node with key {treap_node.key} and value {treap_node.value}")
        if self.root is None:
            self.root = treap_node
        else:
            self.root.insert(treap_node)
            if(treap_node.value < self.root.value):
                print("update root")
                self.root = treap_node
    
    def visualize(self):
        if self.root is None:
            print("The tree is empty.")
        else:
            graph = self.root.to_dot()  # Generate the dot graph from the root
            graph.render('treap', format='png', cleanup=True)  # Renders and saves the image