# In The Name Of GOD
# Programmer is : Faezeh Oraei MiriNejad
# ID is : 96440164

import random
i=5
you = comp = eq = 0
while i:
   
    print('1:Rock\n2:Paper\n3:Scissors')
    user=int(input('choose your operation = '))
    computer=random.randint(1,3)
    if user==1 :
        if computer==1 :
            print('Equal!\n')
            eq = eq + 1
        elif computer==2 :   
            print('Computer Win!\n')
            comp = comp + 1
        else :
            print('You Win!\n') 
            you = you + 1

    elif user==2:
        if computer==1:           
            print('You Win!\n')
            you = you + 1
        elif computer==2 :    
            print('Equal!\n')
            eq = eq + 1
        else :
            print('Computer Win!\n')
            comp = comp + 1

    elif user==3 :
        if computer==1 :  
            print('Computer Win!\n')
            comp = comp + 1
        elif computer==2 :
            print('You Win!\n')
            you = you + 1
        else :    
            print('Equal!\n')
            eq = eq + 1
    else :
        print('Game over!\n')  
         
    i-=1    

print("Equal times = " , eq)
print("computer win times = " , comp)
print("user win times = " , you)