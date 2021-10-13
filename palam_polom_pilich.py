# In The Name Of GOD
# Programmer is : Faezeh Oraei MiriNejad
# ID is : 96440164

import random
import sys

print('palam polom pilich')
while True:
    auto1 = random.randint(1, 2)
    auto2 = random.randint(1, 2)
    user = int(input('please enter your choose = '))

    if auto1==auto2 and auto1!=user :
        print('You lose!!')
    elif auto1==user and auto1!=auto2 :
        print('second computer lose!! ')
    elif auto2==user and auto2!=auto1 :
        print('first computer lose!! ')
    elif auto1==auto2==user:
        print('All the Gamers choose the same operation\nTry again!!')
    elif user!=1 or user!=2 :
        print('choose between number Back(1) and forth(2)')
        sys.exit(0)