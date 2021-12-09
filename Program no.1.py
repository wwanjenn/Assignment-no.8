# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

# Interactive Loop
import random
tryAgain = 'y'

# STEPS
while tryAgain[0] == 'y' or tryAgain[0] == 'Y':

# 1 Ask for 3 Numbers
    print("Lottery!")
    firstNumber = int(input("1st Number: "))
    while firstNumber < 0 or firstNumber > 9:
        print('Choose a number from 0-9')
        firstNumber = int(input("1st Number: "))
        
    secondNumber = int(input("2nd Number: "))
    while secondNumber < 0 or secondNumber > 9:
        print('Choose a number from 0-9')
        secondNumber = int(input("2nd Number: "))
        

    thirdNumber =  int(input("3rd Number: "))
    while thirdNumber < 0  or secondNumber > 9:
        print('Choose a number from 0-9')
        thirdNumber =  int(input("3rd Number: "))
        
    
# 2 Generate 3 random numbers
    firstLotto = random.randint(0,9)
    secondLotto = random.randint(0,9)
    thirdLotto = random.randint(0,9)

# 3 Check if 3 inputs match generated numbers
    if firstNumber == firstLotto and secondNumber == secondLotto and thirdNumber == thirdLotto:
        messageDisplay = 'You Win!'
    else:
        messageDisplay = 'You lose!'
# 4 Display
    print(f'{firstNumber}, {secondNumber}, {thirdNumber}')
    print(f'{firstLotto}, {secondLotto}, {thirdLotto}')
    print(f'{messageDisplay}')
# 5 try again

    tryAgain = input('Try again?(y/n): ')

