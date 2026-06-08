# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
valid_input = False

while not valid_input:
    user_age = input("What is your age?")

    try:
        user_age = int(user_age)
        valid_input = True
    except ValueError:
        print("Invalid Input! please enter a number")


if user_age >= 18:
    print("You have access")
else:
    print("Access denied")