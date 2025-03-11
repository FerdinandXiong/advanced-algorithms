import random
import glob
import os
from graphviz import Digraph  # Importing Graphviz for visualization

class TreapNode():
    def __init__(self, key, prio=None, treap=None):
        self.key = key
        self.prio = prio if prio is not None else random.randint(1, 100)
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.treap = treap  # Reference to the parent treap
        
        print(f"Created node with key {self.key} and prio {self.prio}")
        
    def insert(self, TreapNode):
        TreapNode.treap = self.treap  # Ensure the treap reference is propagated
        if TreapNode.key < self.key:
            if self.left_child is None:
                self.left_child = TreapNode
                TreapNode.parent = self
                TreapNode.restore_heap_property()
            else:
                self.left_child.insert(TreapNode)
        else:
            if self.right_child is None:
                self.right_child = TreapNode
                TreapNode.parent = self
                TreapNode.restore_heap_property()
            else:
                self.right_child.insert(TreapNode)
                    
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
        self.treap.capture_snapshot("After rotate right")
        
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
        self.treap.capture_snapshot("After rotate left")
        
    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left_child.find(key) if self.left_child else None
        else:
            return self.right_child.find(key) if self.right_child else None
    
    def delete(self):
        print(f"Delete {self.key} called")
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

class Treap():
    def __init__(self, root=None):
        self.root = root
        self.snapshot_counter = 0  # Instance-level counter for snapshots
        if root:
            root.treap = self
        
    def insert(self, TreapNode):
        print(f"Inserting node with key {TreapNode.key} and prio {TreapNode.prio}")
        TreapNode.treap = self  # Set the treap reference
        if self.root is None:
            self.root = TreapNode
        else:
            self.root.insert(TreapNode)
            if TreapNode.prio < self.root.prio:
                self.root = TreapNode  # Update root if necessary
        self.capture_snapshot(f"After insert {TreapNode.key}")
    
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
        self.capture_snapshot(f"After delete {key}")
        return elem_to_delete

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
        if self.root is None:
            return

        directory = 'output'
        graph = self.root.to_dot()
        filename = f"{directory}/treap_step_{self.snapshot_counter:02d}"
        graph.render(filename=filename, format="png", cleanup=True)
        print(f"Captured snapshot: {filename} - {description}")
        self.snapshot_counter += 1