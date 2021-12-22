from functools import total_ordering

@total_ordering
class TreeNode:
    """
    A tree node, represents data in a tree and allows for relative ordering of keys.
    """
    def __init__(self, key, value):
        """
        Initializes a tree node.

        Params:
            key : Any - The key for the node.
            value : Number - The value stored in the node.

        Returns:
            TreeNode - The TreeNode object.
        """
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        """
        Adds another tree node as a child to this tree node.

        Params:
            child : TreeNode - The node to be added as a child.
        """
        self.children.append(child)

    def  __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.value == other.value
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return self.value < other.value
        else:
            return NotImplemented
