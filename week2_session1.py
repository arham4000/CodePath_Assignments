# problem 1

# def total_treasure(treasure_map):
#     total = 0
#     for key in treasure_map:
#         total += treasure_map[key]

#     return total





# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasure(treasure_map1)) 
# print(total_treasure(treasure_map2)) 

# problem 2

import string

# Initialize list with lowercase alphabets


def can_trust_message(message):
    lc_list = list(string.ascii_lowercase)
    lc_dict = {}
    for char in lc_list:
        lc_dict[char] = 0
    for char in message:
        if char != ' ':
            lc_dict[char] += 1

    # check if theres any zeros in dict
    if 0 in lc_dict.values():
        return False
    else:
        return True

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
