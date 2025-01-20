import random
import glob
import os
from graphviz import Digraph  # Importing Graphviz for visualization

class treap_node():
    snapshot_counter = 0  # Class-level counter for snapshots
    
    def __init__(self, key, prio=None, treap=None):
        self.key = key
        self.prio = prio if prio is not None else random.randint(1, 100)
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.treap = treap  # Reference to the parent treap
        
        print(f"Created node with key {self.key} and prio {self.prio}")
        
    def insert(self, treap_node):
        treap_node.treap = self.treap  # Ensure the treap reference is propagated
        if treap_node.key < self.key:
            if self.left_child is None:
                self.left_child = treap_node
                treap_node.parent = self
                treap_node.restore_heap_property()                    
                self.treap.visualize()  # Visualize after insert         
                self.capture_snapshot("After insert")
            else:
                self.left_child.insert(treap_node)
        else:
            if self.right_child is None:
                self.right_child = treap_node
                treap_node.parent = self
                treap_node.restore_heap_property()
                self.treap.visualize()  # Visualize after insert         
                self.capture_snapshot("After insert")                
            else:
                self.right_child.insert(treap_node)
                    
    def restore_heap_property(self):
        print("Restoring heap property")
        if self.parent is not None:
            if self.parent.prio > self.prio:
                if self.parent.key > self.key:
                    self.rotate_right()
                else:
                    self.rotate_left()
                self.restore_heap_property()
                
    def rotate_right(self):
        print(f"Rotating right {self.key}")
        parent = self.parent
        treap = self.treap
        
        # Update pointers for rotation
        parent.left_child = self.right_child
        if self.right_child:
            self.right_child.parent = parent
        self.right_child = parent
        self.parent = parent.parent
        
        if self.parent:
            if self.parent.left_child == parent:
                self.parent.left_child = self
            else:
                self.parent.right_child = self
        else:
            treap.root = self  # Update the root of the treap
        
        parent.parent = self
        treap.visualize()  # Visualize after rotation        
        self.capture_snapshot("After rotate right")
        
    def rotate_left(self):
        print(f"Rotating left {self.key}")
        parent = self.parent
        treap = self.treap
        
        # Update pointers for rotation
        parent.right_child = self.left_child
        if self.left_child:
            self.left_child.parent = parent
        self.left_child = parent
        self.parent = parent.parent
        
        if self.parent:
            if self.parent.left_child == parent:
                self.parent.left_child = self
            else:
                self.parent.right_child = self
        else:
            treap.root = self  # Update the root of the treap
        
        parent.parent = self
        treap.visualize()  # Visualize after rotation        
        self.capture_snapshot("After rotate left")
        
    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left_child.find(key) if self.left_child else None
        else:
            return self.right_child.find(key) if self.right_child else None
    
    def delete(self):
        print("Delete called")
        if self.left_child is None:
            if self.right_child is None:
                if self == self.parent.left_child:
                    self.parent.left_child = None
                else:
                    self.parent.right_child = None
            else:
                self.right_child.rotate_left()
                self.delete()
        else:
            if self.right_child is None:
                self.left_child.rotate_right()
                self.delete()
            else:
                if self.left_child.prio < self.right_child.prio:
                    self.left_child.rotate_right()
                    self.delete()
                else:
                    self.right_child.rotate_left()
                    self.delete()
            
    def to_dot(self, graph=None):
        """Generates a dot string representation of the treap, including None nodes."""
        if graph is None:
            graph = Digraph('Treap', node_attr={'shape': 'circle', 'fontsize': '12'},
                            graph_attr={'ranksep': '0.5', 'nodesep': '0.5', 'rankdir': 'TB'})

        # Add the current node
        graph.node(str(self.key), label=f'{self.key}\n{self.prio}')

        # Add edges for children, including None placeholders
        if self.left_child:
            graph.edge(str(self.key), str(self.left_child.key))
            self.left_child.to_dot(graph)
        else:
            null_left = f'null_L_{self.key}'
            graph.node(null_left, label='None', shape='plaintext', fontsize='10')
            graph.edge(str(self.key), null_left)

        if self.right_child:
            graph.edge(str(self.key), str(self.right_child.key))
            self.right_child.to_dot(graph)
        else:
            null_right = f'null_R_{self.key}'
            graph.node(null_right, label='None', shape='plaintext', fontsize='10')
            graph.edge(str(self.key), null_right)

        return graph
    
    @staticmethod
    def clear_snapshots(directory='output', extension='png'):
        """Clear all existing snapshots."""
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            for file in glob.glob(f"{directory}/*.{extension}"):
                os.remove(file)
                
    def capture_snapshot(self, description=""):
        """Capture a snapshot of the current treap structure."""
        if self.treap is None or self.treap.root is None:
            return

        directory = 'output'
        graph = self.treap.root.to_dot()
        filename = f"{directory}/treap_step_{treap_node.snapshot_counter:02d}"
        graph.render(filename=filename, format="png", cleanup=True)
        print(f"Captured snapshot: {filename} - {description}")
        treap_node.snapshot_counter += 1

class treap():
    def __init__(self, root=None):
        self.root = root
        if root:
            root.treap = self
        
    def insert(self, treap_node):
        print(f"Inserting node with key {treap_node.key} and prio {treap_node.prio}")
        treap_node.treap = self  # Set the treap reference
        if self.root is None:
            self.root = treap_node
        else:
            self.root.insert(treap_node)
            if treap_node.prio < self.root.prio:
                self.root = treap_node  # Update root if necessary
    
    def find(self, key):
        print(f"Finding node with key {key}")
        return self.root.find(key) if self.root else None
        
    def delete(self, key):
        print(f"Deleting node with key {key}")
        elem_to_delete = self.find(key)
        if elem_to_delete is None:
            print(f"No node with key {key}, no deletion possible")
            return None
        if elem_to_delete == self.root:
            if not elem_to_delete.left_child and not elem_to_delete.right_child:
                self.root = None
            elif not elem_to_delete.left_child:
                self.root = elem_to_delete.right_child
                elem_to_delete.delete()
            elif not elem_to_delete.right_child:
                self.root = elem_to_delete.left_child
                elem_to_delete.delete()
            else:
                if elem_to_delete.left_child.prio < elem_to_delete.right_child.prio:
                    self.root = elem_to_delete.left_child
                else:
                    self.root = elem_to_delete.right_child
                elem_to_delete.delete()
        else:
            elem_to_delete.delete()
        return elem_to_delete
    
    def visualize(self):
        if self.root is None:
            print("The tree is empty.")
        else:
            graph = self.root.to_dot()
            graph.render('treap', format='png', cleanup=True)
