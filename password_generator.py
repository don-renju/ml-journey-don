import random


password_characters = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
     "v", "w", "x", "y", "z"],

    ["!", "#", "@", "$", "%", "^", "&", "*", "(", ")", "-", "_",
     "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".",
     "<", ">", "/", "?", "//", "|", "`", "~"],

    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
]
while True:
    try:
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("Please enter a number.")
symbol_permision_user= input("Do You want symbols? y/n: ").lower()
while True:
    if symbol_permision_user == "yes" or symbol_permision_user == "y":
        symbol_permision_user = True
        break
    elif symbol_permision_user == "no" or symbol_permision_user == "n":
        symbol_permision_user = False
        break
    else:
        print("Please enter yes or no only.")
        symbol_permision_user = input("Do You want symbols?: ").lower()

password = ""

characters = password_characters[0] + password_characters[2]

if symbol_permision_user:
    characters += password_characters[1]

for i in range(length):
    password += random.choice(characters)

print(f"password generated: {password}")
