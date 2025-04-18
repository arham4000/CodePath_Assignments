class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
	# height of each subtree can only differ by 1
    # need to find method to calculate height of tree
    # apply it to each node that isnt a leaf
    # calculate height of tree by finding longest path
    # 
    def height_subtree(node):
        if node is None:
            return 0
        
        return height_subtree(node.left) + 1

        # 