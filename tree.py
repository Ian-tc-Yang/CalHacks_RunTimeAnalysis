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
    
    def label(self):
        # Return the label value of a current node.
        return self.value
    
    def branches(self):
        # Return the list of branches of the current node.
        return self.children
    
    def is_leaf(self):
        # Returns True if the given tree is a tree, and False otherwise.
        return not self.children
    


# Example usage
# if __name__ == "__main__":
#     root = TreeNode("root")
#     child1 = TreeNode("child1")
#     child2 = TreeNode("child2")
    
#     root.add_child(child1)
#     root.add_child(child2)
    
#     child1.add_child(TreeNode("child1.1"))
#     child1.add_child(TreeNode("child1.2"))
    
#     child2.add_child(TreeNode("child2.1"))

#     print(root)
