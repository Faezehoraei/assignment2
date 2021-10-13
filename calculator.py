# In The Name Of GOD
# Programmer is : Faezeh Oraei MiriNejad
# ID is : 96440164

import math
import sys

print('Assignment 2 - 1st Excercise - Calculator')
while (True):
    print('1- summation')
    print('2- subtract')
    print('3- multiply')
    print('4- divide')
    print('5- logarithm')
    print('6- sin')
    print('7- cos')
    print('8- tan')
    print('9- cot')
    print('10- exit')

    print('----------------------------------------------')
    op=input('please choose the operation = ')
        
    if op == '1':
        number1 = int(input('first number : '))
        number2 = int(input('second number : ')) 
        result = number1 + number2
    elif op == '2':
        number1 = int(input('first number : '))
        number2 = int(input('second number : ')) 
        result = number1 - number2
    elif op == '3':
        number1 = int(input('first number : '))
        number2 = int(input('second number : ')) 
        result = number1 * number2
    elif op == '4':
        number1 = int(input('first number : '))
        number2 = int(input('second number : ')) 
        if number2 != 0:
            result = number1 / number2
        else:
          result = 'cannot divide by zero'  
    elif op == '5' :
        choose = int(input('please enter your number for log operation = '))
        result=math.log10(choose)
    elif op == '6' :
        choose = int(input('please enter your number for sin operation = '))
        result=math.sin(math.radians(choose))
    elif op == '7' :
        choose = int(input('please enter your number for cos operation = '))
        result=math.cos(math.radians(choose))        
    elif op == '8' :
        choose = int(input('please enter your number for tan operation = '))
        result=math.tan(math.radians(choose))
    elif op == '9' :
        choose = int(input('please enter your number for cot operation = '))
        ans=math.tan(math.radians(choose))
        result=1/ans 
    elif op == '10':
        sys.exit(0)          
    else:
            result = 'No Operation'    
    print(result)     