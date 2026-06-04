# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
# TODO: Import the 'random' module so you can generate a secret number.
import random

# VARIABLES
# TODO: Generate a random number between 1 and 100 and save it to 'secret_number'.
secret_number = 42
# TODO: Create a variable to keep track of the user's current guess.
guess = 0
#       (Hint: Start it as 0 so it doesn't accidentally match the secret number!)


# INTRODUCE THE GAME
# TODO: Print a welcome message explaining that the number is between 1 and 100.
print('Welcome to this game! there is a secret number between 1-100')
print('Can you guess it?')

# START THE GAME
# TODO: Start a 'while' loop that keeps running AS LONG AS the 
#       user's guess is NOT EQUAL to the secret_number.
guess = int(input("guess the number"))
while guess != secret_number:
    guess = int(input("try again"))

if guess < secret_number:
    print("Too Low! Try a higher number.")

elif guess > secret_number:
    print("Too high! Try a lower number.")

# GAME OVER / WINNING MESSAGE
# TODO: Print a big victory message telling them they got it right!
print('congrats! you guessed the right number!')

# ===========================================
# EXTENSION
# TODO: Create a play again option (you'll need to loop the whole code, including creating the random number)
# TODO: Add an extra condition that tells them if they are within 5 of the secret number

# ===========================================
# EXPERT
# TODO: Try to structure the program using defined functions