import random
from graphviz import Digraph  # Importing Graphviz for visualization

class treap_node():
    def __init__(self, key, prio=None):
        self.key = key
        self.prio = prio if prio is not None else random.randint(1, 100)
        self.left_child = None
        self.right_child = None
        self.parent = None
        
        print(f"Created node with key {self.key} and prio {self.prio}")
        
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
            if self.parent.prio > self.prio:
                if self.parent.key > self.key:
                # implement rotations
                    self.rotate_right()
                else:
                    self.rotate_left()
                self.restore_heap_property()                   
                
    def rotate_right(self):
        print(f"rotating right {self.key}")
        self.parent.left_child = self.right_child
        if self.right_child: 
            self.right_child.parent = self.parent
        self.right_child = self.parent
        self.parent = self.parent.parent
        if self.parent:
            self.parent.left_child = self
        else: 
            treap.root = self
        self.right_child.parent = self

        
    def rotate_left(self):
        print(f"rotating left {self.key}")
        self.parent.right_child = self.left_child
        if self.left_child:
            self.left_child.parent = self.parent
        self.left_child = self.parent
        self.parent = self.parent.parent
        if self.parent:
            self.parent.left_child = self
        else: 
            treap.root = self
        self.left_child.parent = self
        
    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.left_child:
                return self.left_child.find(key)
            else:
                return None
        else:
            if self.right_child:
                return self.right_child.find(key)
            else:
                return None
    
    def delete(self):
        print("delete called")
        # if self is leaf, delete it, self always has parent because this method
        # is only called when treap has more than one element
        if self.left_child is None:
            if self.right_child is None:
                print("removing reference")
                if self == self.parent.left_child:
                    print("remove self as left child")
                    print(self.parent.key)
                    print(self.parent.left_child.key)
                    self.parent.left_child = None
                    print("removal finished")
                else:
                    print("remove self as left child")
                    self.parent.right_child = None
            # rotate right and delete
            else:
                self.right_child.rotate_left()
                self.delete()
        else:
            # rotate right and delete
            if self.right_child is None:
                self.left_child.rotate_right()
                self.delete()
            # rotate right and delete
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
            # Add a placeholder for None left child
            null_left = f'null_L_{self.key}'
            graph.node(null_left, label='None', shape='plaintext', fontsize='10')
            graph.edge(str(self.key), null_left)

        if self.right_child:
            graph.edge(str(self.key), str(self.right_child.key))
            self.right_child.to_dot(graph)
        else:
            # Add a placeholder for None right child
            null_right = f'null_R_{self.key}'
            graph.node(null_right, label='None', shape='plaintext', fontsize='10')
            graph.edge(str(self.key), null_right)

        return graph

    
class treap():
    def __init__(self, root):
        self.root = root
        
    def insert(self, treap_node):
        print(f"insert node with key {treap_node.key} and prio {treap_node.prio}")
        if self.root is None:
            self.root = treap_node
        else:
            self.root.insert(treap_node)
            if(treap_node.prio < self.root.prio):
                print("update root")
                self.root = treap_node
    
    def find(self, key):
        print(f"find node with key {key}")
        if self.root is None:
            return None
        else:
            return self.root.find(key)
        
    def delete(self, key):
        print(f"delete node with key {key}")
        elem_to_delete = self.find(key)
        if elem_to_delete is None:
            print(f"no node with key {key}, no deletion possible")
            return None
        else:
            if elem_to_delete == self.root:
                if not elem_to_delete.left_child:
                    # if root node is deleted as only element, tree is empty
                    if not elem_to_delete.right_child:
                        print("Deleting the last node (root), setting root to None.")
                        self.root = None
                    # if root node only has right child, it will be new root
                    else:
                        print("root node only has right child, it will be new root")
                        self.root = elem_to_delete.right_child
                        elem_to_delete.delete()
                else:
                    # if root node only has left child, it will be new root
                    if not elem_to_delete.right_child:
                        print("root node only has left child, it will be new root")
                        self.root = elem_to_delete.left_child
                        elem_to_delete.delete()
                    # if root node has 2 children, lower prio will be new root
                    else:
                        print("root node has 2 children, lower prio will be new root")
                        if elem_to_delete.left_child.prio < elem_to_delete.right_child.prio:
                            self.root = elem_to_delete.left_child
                            elem_to_delete.delete()
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
            graph = self.root.to_dot()  # Generate the dot graph from the root
            graph.render('treap', format='png', cleanup=True)  # Renders and saves the image