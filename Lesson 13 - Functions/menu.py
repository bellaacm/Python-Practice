"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1. 
2.
3.
"""

# INSTRUCTIONS
# TODO Copy over the code from 3 of your other programs into their own function.

def rectangle_calculator():
    
 def calculate_area():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The area is {length * width }².")


 def calculate_circumference():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The circumference is {length * 2 + width * 2}.")


 def main():

    # introduction 
    print("Hello! this is a calculator you can use to find the area or circumference of a rectangle")
    
    while True:
        user_choice = input("If you would like to find the area enter 1. If you would like to calculate the circumference enter 2:")
        
        if user_choice == "1":
            calculate_area()

        elif user_choice == "2":
            calculate_circumference()

        else:
            print("This input is invalid")

        user_exit = input("Would you like to repeat the calculator? [yes/no]")
        if user_exit == "no":
         break 

 main()

def security_check():
    security_status = "LOCKED"
    alarm_sound = "SIREN"

    def trigger_alarm():
        print(f"Alert! Sounding the {alarm_sound}")

    def check_system():
        print("Checking home network stability...")
        if security_status == "LOCKED":
            print("All doors are secured.")
        else:
            trigger_alarm()

    def reset_system():
        print("System rebooting...")

    def main():
        print(f"The current alarm sound is: {alarm_sound}")
        check_system()
        reset_system()

    main()

def inventory():
    banned_items = ["slingshot", "laser"]
    inventory_items = ["apple", "slingshot", "book", "laser"]
    confiscated = []

    print(f"Scanning inventory: {inventory_items}")

    for item in inventory_items:
        if item in banned_items:
            print(f"Alert! Found banned item: {item}")
            confiscated.append(item)

    print(f"Scan complete. Total flag matches: {len(confiscated)}")

    if len(confiscated) > 0:
        print("Items confiscated:")
        for item in confiscated:
            print(item)

def main():

   print("Here is a menu of some of my previous projects:")

while True:
    user_choice = input("If you would like to run the rectangle area/circumference calculator enter 1. If you would like to run the security program enter 2. If you would like to run the inventory program press 3.")

    if user_choice == "1":
            rectangle_calculator()

    elif user_choice == "2":
            security_check()

    elif user_choice == "3":
            inventory()

    else:
            print("Invalid input.")

    user_exit = input("Would you like to go back to the main menu? [yes/no] ")
    if user_exit.lower() == "no":
            break


  



    




# TODO If you have any imports, make sure to move them out of the function to IMPORTS section 
# (everything else can stay in the functions)
# TODO Create a menu program in the main function and call each program function based on user input

#===============================
# IMPORTS
#===============================


#===============================
# FUNCTIONS
#===============================

# Run program 1


# Run program 2


# Run program 3


# Run main code

#===============================
# EXECUTION
#===============================

# Execute main code



#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()