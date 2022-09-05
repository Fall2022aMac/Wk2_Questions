#Question 5
#Write a program to obtain the first 10 numbers of a Fibonacci sequence. In a Fibonacci sequence the sum of
#two successive terms gives the third term.
#Following are the first 10 terms of the Fibonacci sequence:
#0 1 1 2 3 5 8 13 21 34

terms = int(input("Enter a number between 1 & 10: ")) #how many items we want from user 

n1,n2=0,1 #n1/2 first two items in the list so we know where to start
counted = 0 #number of terms we have calculated based on user input

while counted < terms:
	print(n1)
	new_number = n1 + n2
	n1 = n2
	n2 = new_number
	counted += 1

	#The while loop runs until the number of values calculated is equal to the total number inputed. 
    # The loop prints out the value of n1 to the shell. 
    # It calculates the next number by adding the previous number in the sequence to the number before.
	#
	# 1st: swap the value of n1 to be equal to n2. 
    # 2nd: This makes n1 the first number back after the new number. 
    # 3rd: set n2 to be equal to the new number. 
    # 4th: Next, we use the += operator to add 1 to our counted variable.


    #Math of a Fibonacci series
    #F1=0
    # F2=1
    # FN=FN-1+FN-2
