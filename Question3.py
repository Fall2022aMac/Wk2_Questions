#Write a program that accepts a number from the user and calculate the factorial of that
#number. The factorial of an integer n is defined as
#n ! = n ( n - 1)( n - 2)( n - 3) ... (3)(2)(1) ; if n>0
#For example, 5! = 5 x 4 x 3 x 2 x 1
# This function computes the factor of the argument passed
num = int(input("Enter a positive number: "))
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)






## In this program, the number whose factor is to be found is stored in num, which is passed to the print_factors() function. 
# This value is assigned to the variable x in print_factors().
#
# In the function, we use the for loop to iterate from i equal to x. If x is perfectly divisible by i, it's a factor of x.
