class FibNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0  # Number of children
        self.parent = None
        self.child = None
        self.mark = False  # Used in decrease-key operation
        self.left = self
        self.right = self  # Circular doubly linked list

class FibonacciHeap:
    def __init__(self):
        self.min_node = None  # Root list's min node
        self.num_nodes = 0  # Total number of nodes

    def insert(self, key):
        node = FibNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            self._add_to_root_list(node)
            if key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1
        return node  # Return node for testing purposes

    def _add_to_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
            node.left = node
            node.right = node
        else:
            node.right = self.min_node.right
            node.left = self.min_node
            self.min_node.right.left = node
            self.min_node.right = node

    def min(self):
        return self.min_node.key if self.min_node else None

    def meld(self, fib_heap):
        if fib_heap.min_node is None:
            return
        if self.min_node is None:
            self.min_node = fib_heap.min_node
        else:
            min1, min2 = self.min_node, fib_heap.min_node
            min1_right, min2_left = min1.right, min2.left
            
            min1.right = min2
            min2.left = min1
            min1_right.left = min2_left
            min2_left.right = min1_right
            
            if min2.key < min1.key:
                self.min_node = min2
        self.num_nodes += fib_heap.num_nodes

    def _iterate(self, start):
        if start is None:
            return
        node = start
        while True:
            yield node
            node = node.right
            if node == start:
                break

    def delete_min(self):
        z = self.min_node
        if z:
            if z.child:
                children = [x for x in self._iterate(z.child)]
                for child in children:
                    self._add_to_root_list(child)
                    child.parent = None
            self._remove_from_sibling_list(z)
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.num_nodes -= 1
        return z

    def _consolidate(self):
        degree_table = {}
        root_nodes = [x for x in self._iterate(self.min_node)]
        for node in root_nodes:
            degree = node.degree
            while degree in degree_table:
                other = degree_table[degree]
                if other.key < node.key:
                    node, other = other, node
                self._link(other, node)
                del degree_table[degree]
                degree += 1
            degree_table[degree] = node
        self.min_node = min(degree_table.values(), key=lambda x: x.key)

    def _link(self, y, x):
        self._remove_from_sibling_list(y)
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.right = x.child.right
            y.left = x.child
            x.child.right.left = y
            x.child.right = y
        x.degree += 1
        y.mark = False

    def _remove_from_sibling_list(self, node):
        if node.right == node:
            return None
        node.left.right = node.right
        node.right.left = node.left
        return node.right

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key must be smaller than current key")
        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node, parent):
        if parent.child == node:
            parent.child = node.right if node.right != node else None
        parent.degree -= 1
        self._remove_from_sibling_list(node)
        self._add_to_root_list(node)
        node.parent = None
        node.mark = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent: # root nodes are not marked, only mark if node has parent
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.delete_min()
