# now we build a simple password generator.
# from string methods
# by tools like python and string module
# import string 
# create a password variable 
# password = input("Enter the password: ")
# alpha = True
# uppercase = False
# strip = True
# digit = True
# lowercase = False
# number = False

# for character in password:
# if character.isalpha():
# alpha = True
# if character.upper():
# uppercase = True
# if character.islower():
# lowercase = True
# if character.strip():
# strip = True
# if character.isalnum():
# number = True
# if character.isdigit():
# digit = True

# if alpha and uppercase and lowercase and strip and digit and number :
# print (password is done)
#else:
# print(password is incomplete)


import string

password = input("Enter your password: ")

uppercase = False
lowercase = False
digit = False
special = False

for character in password:
    if character.isupper():
        uppercase = True

    if character.islower():
        lowercase = True

    if character.isdigit():
        digit = True

    if character in string.punctuation:
        special = True

if len(password) >= 8 and uppercase and lowercase and digit and special:
    print("Password is valid")
else:
    print("Password is incomplete")

    if len(password) < 8:
        print("Password must contain at least 8 characters")

    if not uppercase:
        print("Password must contain an uppercase character")

    if not lowercase:
        print("Password must contain a lowercase character")

    if not digit:
        print("Password must contain a number")

    if not special:
        print("Password must contain a special character")