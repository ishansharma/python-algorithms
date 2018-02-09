# Python Data Structures and Algorithms
# http://proquest.safaribooksonline.com.libproxy.utdallas.edu/book/programming/python/9781786467355/binary-trees/24fa378d_24f1_4e8f_bff2_cc1cdad5e10a_xhtml?uicode=utdallas
from collections import deque


class Node:
    """
    Node is just a container for data.
    It hols references for other nodes. We are using binary tree node, so only left and right children
    """
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class BST:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        """
        Since min is always te left most leaf node, keep traversing left children until we get a leaf

        Takes O(h) time where h is height of the tree
        :return: Node
        """
        current = self.root_node
        while current.left_child:
            current = current.left_child

        return current

    def find_max(self):
        """
        Max is the rightmost leaf node, we traver right children until we get to a leaf

        Takes O(h) time
        :return: Node
        """
        current = self.root_node
        while current.right_child:
            current = current.right_child

        return current

    def insert(self, data):
        """
        Insert the number into our tree
        :param data: int value we want to insert
        :return:
        """
        node = Node(data)

        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self, data):
        """
        Since we don't store the parent for a node, this function helps us find the parent.
        Useful when removing nodes

        :param data: int
        :return: tuple
        """
        parent = None
        current = self.root_node
        if current is None:
            return parent, None
        while True:
            if current.data == data:
                return parent, current
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

    def remove(self, data):
        """
        Remove the node with given data. O(h) complexity
        :param data: int
        :return:
        """
        parent, node = self.get_node_with_parent(data) # first, get the parent and current node

        if parent is None and node is None:
            return False

        # count the children
        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        # handle different conditions
        # if no children, we just remove the node.
        # if 1 child, we just replace node with its child
        # if 2 children, we have to do traversal and find smallest child in right subtree
        if children_count == 0:
            if parent:
                # node has no children (leaf node), we detect its position relative to parent and set that to None
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            # only one child, replace with child
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = None
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        """
        Search for data in the tree. If found, return it. Else return None
        :param data: int
        :return: int
        """
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def inorder(self, root_node):
        """
        Do in order traversal starting at a node
        :param root_node: Node
        :return: None
        """
        current = root_node
        if current is None:
            return

        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        """
        Pre-order traversal
        :param root_node: Node
        :return: None
        """
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)

    def postorder(self, root_node):
        """
        Post-order traversal
        :param root_node: Node
        :return: None
        """
        current = root_node
        if current is None:
            return

        self.postorder(current.left_child)
        self.postorder(current.right_child)
        print(current.data)

    def breadth_first_traversal(self):
        """
        Do a breadth first traversal. We push nodes to explore to a queue and go level by level
        :return: List
        """
        list_of_nodes = []
        traversal_queue = deque([self.root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)

            if node.right_child:
                traversal_queue.append(node.right_child)

        return list_of_nodes
