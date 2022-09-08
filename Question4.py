#Question 4
#Write a program that generates a random number and asks the user to guess what the
#number is. If the user's guess is higher than the random number, the program should display
#"Too high, try again." If the user's guess is lower than the random number, the program
#should display "Too low, try again." The program should use a loop that repeats until the user
#correctly guesses the random number.

import random #random number generator

computer = random.randint(1,10) #random number pool
player = 0 #score keeper
tries=0    # tries keeper could do a fails one but who likes that :)

print("\n -----------Guess a number game----------- \n")

while(player != computer):
    player = int(input('Enter your guess 1 - 10: '))
    tries = tries + 1 #counts the amount of tries
    
    #loop for the tries. 
    if player < computer:
        print('To low, try again.')
    elif player > computer:
        print ('To high, try again.')
    else:
        print ("Correct!,you got it in",+tries,"tries")
