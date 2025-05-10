from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# # Problem 1

# root = TreeNode("Trunk")
# root.left = TreeNode("Mcintosh", TreeNode("Fuji"), TreeNode("Opal"))
# root.right = TreeNode("Granny Smith", TreeNode("Crab"), TreeNode("Gala"))

# print_tree(root)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Problem 2

# def calculate_yield(root):
#     if not root:
#         return None

#     if root.val == "+":
#         return root.left.val + root.right.val
#     elif root.val == "-":
#         return root.left.val - root.right.val
#     elif root.val == "*":
#         return root.left.val * root.right.val
#     elif root.val == "/":
#         return root.left.val / root.right.val
#     else:
#         return None
    
# """
#     +
#   /   \
#  7     5
# """
# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

    



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 3

# def right_vine(root):
#     plant_path = []
#     plant_path.append(root.val)

#     while root.right:
#         plant_path.append(root.right.val)
#         root = root.right
#     return plant_path

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 4 (Recursive Implementation of Problem 3)

# def right_vine(root, plant_path = None):
    # if plant_path is None:
    #     plant_path = [root.val]
    
    # if root.right is None:
    #     return plant_path
    # else:
    #     plant_path.append(root.right.val)
    #     return right_vine(root.right, plant_path)


# def right_vine(root):

#     def rec_helper(root, path):
#         #base
#         if root.right is None:
#             return 
#         else:
#             path.append(root.right.val)
#             return rec_helper(root.right, path)
        
#     result = []

#     if root:
#         result.append(root.val)
#         rec_helper(root, result)
    
#     return result


# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 5
def count_leaves(root):

    leaf_count = 0
    
    # base
    if root.right is None and root.left is None:
        leaf_counter += 1
    else:


    



# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))
