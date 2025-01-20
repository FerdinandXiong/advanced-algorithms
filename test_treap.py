from treap import treap, treap_node

def random_tree_generation():
    t = treap(treap_node(70))
    t.insert(treap_node(65))
    t.insert(treap_node(46))
    t.insert(treap_node(37))
    t.insert(treap_node(22))
    t.visualize()

# generates the tree for exercise 1 of sheet 5, 
# but uses numbers for letters, e.g. 1 for a, 2 for b,...
def generate_tree_24_1():
    t241 = treap(treap_node(3, 7))
    t241.root.clear_snapshots()
    t241.insert(treap_node(4, 3))
    t241.insert(treap_node(5, 10))
    t241.insert(treap_node(2, 1))
    t241.insert(treap_node(1, 4))
    t241.visualize()
    print(t241.find(2))
    t241.delete(4)
    t241.visualize()

if __name__ == "__main__":
    generate_tree_24_1()