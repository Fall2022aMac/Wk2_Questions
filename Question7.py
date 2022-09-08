#Question 7
#The marks obtained by a student in computer science is input
#by the user. Your program should display the grade. The
#student gets a grade as per the following rules:
#marks Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F
#Sample Output
#Enter your marks in CS: 67
#Your grade is D


print('\n' '------- Student grade calculator!!! -----''\n')

score = float(input('Enter students score: ')) #used a float for partial scores

#grade calculations 
if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'

print('Your grade of '+str(score)+' is a: '+(grade))
