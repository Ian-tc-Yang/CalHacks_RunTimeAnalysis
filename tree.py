# chatGPT
# TODO
class TreeNode:
    def __init__(self, value):
        # Initialize the node with a string value and an empty list for children nodes
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Node value must be a string.")
        
        self.children = []  # List to store children nodes
    
    def add_child(self, child_node):
        # Add a child node to the current node
        if isinstance(child_node, TreeNode):
            self.children.append(child_node)
        else:
            raise ValueError("Child node must be an instance of TreeNode.")
    
    def __repr__(self, level=0):
        # Recursive function to print the tree structure
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


# Example usage
if __name__ == "__main__":
    root = TreeNode("root")
    child1 = TreeNode("child1")
    child2 = TreeNode("child2")
    
    root.add_child(child1)
    root.add_child(child2)
    
    child1.add_child(TreeNode("child1.1"))
    child1.add_child(TreeNode("child1.2"))
    
    child2.add_child(TreeNode("child2.1"))

    print(root)


# 61A
# TODO
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree is a leaf. (i.e. It has no branches.)"""
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])