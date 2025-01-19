from treap import treap, treap_node

if __name__ == "__main__":
    t = treap(treap_node(70))
    t.insert(treap_node(65))
    #t.visualize()
    t.insert(treap_node(46))
    #t.visualize()
    t.insert(treap_node(37))
    #t.visualize()
    t.insert(treap_node(22))
    print("\nTree structure:")
    t.visualize()
    print("finished")