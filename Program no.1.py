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

# STEPS
# 1 Ask for 3 Numbers
print("Lottery!")

firstNumber = int(input("1st Number: "))
secondNumber = int(input("2nd Number: "))
thirdNumber =  int(input("3rd Number: "))

# 2 Generate 3 random numbers
firstLotto = random.randint(0,9)
secondLotto = random.randint(0,9)
thirdLotto = random.randint(0,9)

# 3 Check if 3 inputs match generated numbers

# 4 Display
# 5 try again

