#!/usr/bin/python

#from binTree import BinaryTree
import searchTree


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
    fst = searchTree.BinarySearchTree()
   
    given_list = [50, 25, 20, 15, 23, 75, 80, 76, 85, 70, 65, 72]
    
    for i in given_list: 
        fst.insert_iterative(fst.root, i)
    
    print()
    print(f' - > Array in sorted order with search tree: {fst}')
    print(f' - > Number of elements in the tree: {fst.count(fst.root)}')
    print(f' - > Height of the tree: {fst.height(fst.root)}')
    print(f' - > Largest element in the tree: {fst.largest_element(fst.root)}')
    print(f' - > Smallest element in the tree: {fst.smallest_element(fst.root)}')
    print(f' - > Successor of 15 is {fst.successor(15)}')
    print(f' - > Predecessor of 50 is {fst.predecessor(50)}')

    fst.insert_after(50, 55)
    print(f' - > Treee after insertion {fst}')
    print()


if __name__ == "__main__":
    main()
