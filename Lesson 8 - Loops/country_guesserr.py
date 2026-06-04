# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
correct_country = 'italy'
correct_country = correct_country.lower().strip()

# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)
guess = ''

# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
guess = input("Guess the country:")
while guess != correct_country:
    guess = input("try again")
input ('welcome')

    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!
print('congrats! you guessed the correct country!')
# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option