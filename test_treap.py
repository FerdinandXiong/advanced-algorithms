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
    treap_node.clear_snapshots()
    t241.insert(treap_node(4, 3))
    t241.insert(treap_node(5, 10))
    t241.insert(treap_node(2, 1))
    t241.insert(treap_node(1, 4))
    print(t241.find(2))
    t241.delete(4)
    t241.visualize()

def generate_exam_tree_WS2324():
    tws2324 = treap(treap_node(8, 3))
    treap_node.clear_snapshots()
    tws2324.insert(treap_node(2, 6))
    tws2324.insert(treap_node(11, 7))
    tws2324.insert(treap_node(1, 9))
    tws2324.insert(treap_node(5, 8))
    # tws2324.insert(treap_node(4, 4))
    tws2324.delete(8)
    tws2324.visualize()

if __name__ == "__main__":
    generate_exam_tree_WS2324()