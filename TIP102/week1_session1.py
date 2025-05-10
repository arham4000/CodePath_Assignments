# def welcome():
#     print ("Welcome to The Hundred Acre Wood!")

# welcome()


# def greeting(name):

#     print ("Welcome to The Hundred Acre Wood",name ," My name is Christopher Robin.")

# greeting ("mustafa")

# def print_catchphrase(character):
#     if character == "Pooh":
#         print ("Oh bother!")
#     elif character == "Tigger":
#         print ("TFN: Ta-ta for now!")
#     elif character == "Ahmed":
#         print("Meow")
#     elif character == "Riz" :
#         print("wow")
#     else:
#         print ("Sorry! I don't know" , character , "catchphrase!")        

# print_catchphrase ("Tigger")


def print_catchphrase(character):
    phrases = {"Pooh": "Oh bother!", "Tigger": "TTFN: Ta-ta for now!", "Eeyore": "Thanks for noticing me.", "Christopher Robin":"Silly old bear."}
    if character in phrases:
        print(phrases[character])
    else: 
        print("Sorry! I don't know ", character,"'s catchphrase!")

print_catchphrase("Rizwana Tabassum")