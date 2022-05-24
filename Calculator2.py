#Created by: Olivia G.
#Completion date: 5/22/2022
#Prompt: Create a calulator that accepts two numbers and adds them.The program should continue calculating entered 
#inputs until the user enters 'AC' (all clear).

import sys 
while True: #This while loop will continuously run the loops within it.
    #This loop asks for the first input. It checks to see if it is 'AC'. Program will stop if 'AC' is entered, and will continue if not.
    while True:
        num1 = input('>>')
        if num1 != 'AC':
            break
        elif num1 == 'AC':
            sys.exit() #forces program to halt
    
    #This loop asks for the second input. It checks to see if it is 'AC'. Program will stop if 'AC' is entered, and will continue if not.
    while True:
        num2 = input('>>')
        if num2 != 'AC':
            break
        elif num2 == 'AC':
            sys.exit()

    #This if statement will check to see if the user inputs were numbers, if so, the inputs will be added.
    if num1.isdigit() == True and num2.isdigit() == True:
        n1 = int(num1)
        n2 = int(num2)
        print('Result:',n1 + n2)