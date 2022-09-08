#Question 1
#Write a program that checks entered password is valid or not. For a password to be
#valid it must be at least eight characters long and have at least one special character.

import re
p = input("Input your password:  \t")
x = True
while x:  
    if (len(p)<6 or len(p)<8):
        break
    elif not re.search("[a-z]",p): #checks for lowercase letters
        break
    elif not re.search("[0-9]",p): #checks for numbers
        break
    elif not re.search("[A-Z]",p): #checks for uppercase letters
        break
    elif not re.search("[$#@]",p): #checks for special characters
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("\n   Not a Valid Password! \n", p)



#to hide password with *** use getpass.getpass ("Enter your password")