#5/22/2022
#Prompt: Create a calulator that accepts two numbers and adds them.The program should continue calculating entered 
#inputs until the user enters 'AC' (all clear).

import sys
while True:
    while True:
        num1 = input('>>')
        if num1 != 'AC':
            break
        elif num1 == 'AC':
            sys.exit()
            
    while True:
        num2 = input('>>')
        if num2 != 'AC':
            break
        elif num2 == 'AC':
            sys.exit()

    if num1.isdigit() == True and num2.isdigit() == True:
        n1 = int(num1)
        n2 = int(num2)
        print('Result:',n1 + n2)
        
