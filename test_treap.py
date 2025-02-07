from treap import Treap, TreapNode
def random_tree_generation():
    t = Treap(TreapNode(70))
    t.insert(TreapNode(65))
    t.insert(TreapNode(46))
    t.insert(TreapNode(37))
    t.insert(TreapNode(22))
    t.visualize()

# generates the tree for exercise 1 of sheet 5, 
# but uses numbers for letters, e.g. 1 for a, 2 for b,...
def generate_tree_24_1():
    t241 = Treap(TreapNode(3, 7))
    TreapNode.clear_snapshots()
    t241.insert(TreapNode(4, 3))
    t241.insert(TreapNode(5, 10))
    t241.insert(TreapNode(2, 1))
    t241.insert(TreapNode(1, 4))
    print(t241.find(2))
    t241.delete(4)
    t241.visualize()

def generate_exam_tree_WS2324():
    tws2324 = Treap(TreapNode(8, 3))
    TreapNode.clear_snapshots()
    tws2324.insert(TreapNode(2, 6))
    tws2324.insert(TreapNode(11, 7))
    tws2324.insert(TreapNode(1, 9))
    tws2324.insert(TreapNode(5, 8))
    # tws2324.insert(TreapNode(4, 4))
    tws2324.delete(8)
    tws2324.visualize()

if __name__ == "__main__":
    generate_exam_tree_WS2324()