#Question 2
#Write a program that accepts a string. Your program should delete all numbers from it.
#Example if entered string is 'Welcome to 2021 class.' it should display 'Welcome to class'
import re

string =input("Write words and letters:")    #takes user input    
newstring = re.sub(r'[0-9]+','',string) #checks user input for letters and numbers and removes the numbers
print (newstring) #prints new string 