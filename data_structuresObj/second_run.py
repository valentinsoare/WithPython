#!/usr/bin/python

#from binTree import BinaryTree
from searchTree import BinarySearchTree


def main():
    #null_node = BinaryTree()

    #a = BinaryTree()
    #b = BinaryTree()
    #c = BinaryTree()
    #d = BinaryTree()
    #e = BinaryTree()
    #f = BinaryTree()
    #g = BinaryTree()
    #h = BinaryTree()
    #i = BinaryTree()
    #j = BinaryTree()
    #k = BinaryTree()
    #m = BinaryTree()

    #n = BinaryTree()

    #a.make_tree(33, null_node, null_node)
    #b.make_tree(39, null_node, null_node)
    #c.make_tree(37, a, b)
    #d.make_tree(25, null_node, null_node)
    #e.make_tree(65, null_node, null_node)
    #f.make_tree(72, null_node, null_node)
    #g.make_tree(31, d, c)
    #h.make_tree(68, e, f)
    #i.make_tree(49, null_node, null_node)
    #j.make_tree(55, null_node, null_node)
    #k.make_tree(40, g, i)
    #m.make_tree(60, j, h)

    #n.make_tree(50, k, m)

    #print(n)
    #ax = k.successor(k.root)
    #print(ax)

    #---------------------------------------

    zero_node = BinarySearchTree(None, None, None)

    a = BinarySearchTree(1, zero_node, zero_node)
    b = BinarySearchTree(4, zero_node, zero_node)
    c = BinarySearchTree(3, a, b)  # subtree root

    d = BinarySearchTree(6, zero_node, zero_node)
    e = BinarySearchTree(9, zero_node, zero_node)
    f = BinarySearchTree(8, d, e)  # sbutree root

    g = BinarySearchTree(5, c, f)

    #if g.iterative_search(3):
    #    print(f'nebunie boss')

    #ax = g.recursive_search(, g.root)
    #print(ax)

    #ax = list(f.iterative_traverse_binary_search_tree())
    #print(ax)

    ay = list(g.recursive_traverse_binary_search_tree(g.root, []))
    print(ay)



if __name__ == "__main__":
    main()
