from trees import binary_search_tree as b

# # creating a few nodes
# n1 = trees.Node("root node")
# n2 = trees.Node("left child node")
# n3 = trees.Node("right child node")
# n4 = trees.Node("left grandchild node")
#
# # connect the nodes to each other
# n1.left_child = n2
# n1.right_child = n3
# n2.left_child = n4
#
# # traverse
# current = n1
# while current:
#     print(current.data)
#     current = current.left_child

tree = b.BST()
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(10)

tree.remove(6)

print("searching for 0", tree.search(0))
print("searching for 2", tree.search(2))
print("searching for 5", tree.search(1))

print("going to print the tree (inorder):")
print(tree.inorder(tree.root_node))

print("going to print the tree (pre-order):")
print(tree.preorder(tree.root_node))

print("going to print the tree(post-order):")
print(tree.preorder(tree.root_node))

print("going to print the tree(breadth first traversal):")
print(tree.breadth_first_traversal())

res = tree.get_node_with_parent(1)

