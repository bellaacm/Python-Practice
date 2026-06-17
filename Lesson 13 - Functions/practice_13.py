"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing a function for calculating the circumference, 
# and calling each calculate function based on user choice


# Calculate the area of a rectangle based on length and width from user
def calculate_area():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The area is {length * width }².")


def calculate_circumference():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The circumference is {length * 2 + width * 2}.")

# =====================================================================
# EXECUTION
# =====================================================================
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

