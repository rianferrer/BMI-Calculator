#Ferrer, Marion Caryl R.
#3ITD
#BMI Calculator
 
import math
import sys

def bmicalc(height,weight):
    bmi = (weight/(height*height))
    return bmi

def bmi_result(bmi):
    if (bmi < 18.5):
        return 'underweight.'
    elif (bmi >= 18.5 and bmi < 24.9):
        return 'healthy.'
    elif (bmi >= 24.9 and bmi < 30):
        return 'overweight.'
    elif (bmi >= 30):
        return 'obese.'
    
def start():
    try:
        print('\nWelcome to BMI Analyzer Program.')
        height = float(input('Enter your height (in m): '))
        weight = float(input('Enter your weight (in kg): '))

    except:
        print('Enter correct value.')
        
    else:
        bmi = bmicalc(height, weight)
        result = bmi_result(bmi)

        print(f'\nYour BMI is ', round(bmi,2))
        print('You are', result)

start()

while True:
    try_again = input('Try again? Y/N: ')
    
    if try_again == 'Y':
        start()
    elif try_again == 'N':
        print('\nThank you for trying this BMI Analyzer Program.')
        print('Made by: Ferrer, Marion | 3ITD')
        sys.exit()
    else:
        try_again
