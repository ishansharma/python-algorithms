from trees import trees_basics as trees

# creating a few nodes
n1 = trees.Node("root node")
n2 = trees.Node("left child node")
n3 = trees.Node("right child node")
n4 = trees.Node("left grandchild node")

# connect the nodes to each other
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

# traverse
current = n1
while current:
    print(current.data)
    current = current.left_child
