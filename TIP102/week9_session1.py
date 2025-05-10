from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


# Problem 2

# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def print_design(design):
# # If the tree is empty:
#     if not design:
# #     return an empty list
#         return []
# # Create an empty queue
#     queue = deque()
# # Create an empty list to store visited nodes
#     result = []

# # Add the root into the queue
#     queue.append(design)
# # While the queue is not empty:
#     while queue:
# #     Pop the next node off the queue 
#         node = queue.popleft()
#         if node:
#     #     Add the popped node to the list of visited nodes
#             result.append(node.val)

#     #     Add the popped node's left child to the queue
#             queue.append(node.left)
#     #     Add the popped node's right child to the queue
#             queue.append(node.right)

#     return result



# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))

# print(print_design(croquembouche))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Problem 3

def max_tiers(cake):

    paths = []

    def rec_helper(node, path, paths):
        
        if not node:
            return
        
        path.append(node.val)

        if not node.left and not node.right:
            paths.append(path)
        else:
            rec_helper(node.left, path, paths)
            rec_helper(node.right, path, paths)

        path.pop()

