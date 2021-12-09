# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# CONDITIONAL LOOP

# 1 Generate Random Number 0-100
import random

print('Guess the Number!')

randomNumber = random.randint(0,100)

# 2 Input from user
userGuess = input('Guess: ')

# 3 Conditional Loop
while userGuess != randomNumber:

# 4 Display if Guess is greater or lesser
# 5 Print Congratutalions 