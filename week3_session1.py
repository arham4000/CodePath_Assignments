
# Problem 1

# def is_valid_post_format(posts):
#     dict_chars = {}
#     chars_stack = []
# # iterate through string
#     for char in posts:
# # if opening bracket:
#         if char == "(" or char == "{" or char == "[":
# #   push onto stack
#             chars_stack.append(char)
# #   set pushed value as previous
#             previous = char
# # else:
# #        if stack is empty:
#         else:
#             if not chars_stack:
#                 return False
# #       if previous matches closing bracket:
#             elif previous == "(" and char == ")":
#                 chars_stack.pop()
#             elif previous == "{" and char == "}":
#                 chars_stack.pop()
#             elif previous == "[" and char == "]":
#                 chars_stack.pop()
#             else:
#                 return False
#     if not chars_stack:
#         return True       


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))
# print(is_valid_post_format("([(]))"))

# Problem 2

# def reverse_comments_queue(comments):
#     new_list = []
#     stack = []

#     for comment in comments:
#         stack.append(comment)

#     for x in range(len(comments)):
#         new_list.append(stack.pop())
    
#     return new_list
  

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# Problem 3

# def is_symmetrical_title(title):
#   left_pointer = 0
#   title = title.lower()
#   title = title.replace(" ", "")
#   right_pointer = len(title)-1

#   while left_pointer <= right_pointer:
#     if title[left_pointer] != title[right_pointer]:
#       return False
#     left_pointer += 1
#     right_pointer -= 1
    
    
#   return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

# problem 4

# def engagement_boost(engagements):
#     squared_engagements = []

    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     squared_engagements.sort(reverse=True)
#     print(squared_engagements)
    
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result



# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))


# problem 6

def clean_post(post):
  stack = []

  prev = post[0]
  
  for letter in post:
    


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 