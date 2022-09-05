#Question 6
#Write a program which asks user to enter price and quantity of a
#product. Your program should calculate and display the bill amount
#as price * quantity. If bill amount is more than 2000 discount of 20%
#on bill amount should be subtracted from bill.
#----------------------------------------------------------------
# Sample Output
# Enter price of product: 550
# Enter quantity: 4
# Bill amount: 2200
# Discount: 440.0
# Your net bill amount is 1760.0

price = float(input('Enter price of product: $'))
quant = float(input('Enter how many:   '))
total = price * quant

if total > 2000: #loop for discount of product i.e. like a coupon or bulk buying if over a certain amount
    discount = total*0.20
else:
    discount = 0.00

net_total = total - discount #applying the discount

print('Bill total: $',total)
print('Discount: $',discount)
print('Your net bill amount is: $', net_total)

