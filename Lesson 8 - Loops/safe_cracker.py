# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
# TODO: Create a variable for the correct vault combination (e.g., "742").
correct_combination = "742"
# TODO: Create a variable to keep track of how many attempts the player has used (start at 0).
attempts = 0

# INTRODUCE THE GAME
# TODO: Print a cool message explaining they are trying to hack a safe.
print("You are trying to crack a safe but there is a secret 3  digit code you must guess to open it.")
# TODO: Let them know that typing 'exit' will quit the game entirely.
print("Type 'exit' anytime you want to leave the game.")



while True:
 
    user_input = input("Enter the 3 digit code: ")

    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------

    if user_input.lower().strip() == 'exit':
        print('Aborting mission...')
        break

    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    
    try:
        int(user_input)
    except ValueError:
        print("Error: Safe only accepts digits. Try again.")
        continue

    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    attempts += 1

    if user_input == correct_combination:
        print("Vault unlocked! You found the treasure!")
        break
    else:
        print("Combination failed. Try again.")

    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    if attempts >= 5:
        print("Alarm triggered! Security is on the way!")
        break

# GAME OVER
# ---------------------------------------------------------------------
print("Game Over")



# =========================================
# EXTENSION
# TODO Add a scenario D to your loop: Running out of time
    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # TODO: Check if their attempts tracker has reached 5.
    #       If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

# =========================================
# EXPERT
# Mastermind Version:
# Add a part that lets you check each digit (you'll need to use split()) and tells the user how many digits are correct in their guess