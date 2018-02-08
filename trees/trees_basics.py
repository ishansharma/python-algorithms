# From Python Data Strucutres and Algorithms
# http://proquest.safaribooksonline.com.libproxy.utdallas.edu/book/programming/python/9781786467355


class Node:
    """
    Node is just a container for data.
    It hols references for other nodes. We are using binary tree node, so only left and right children
    """
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

