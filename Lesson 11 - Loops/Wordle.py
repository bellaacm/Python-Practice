# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random 

# VALUES
# TODO Create a list of at least 5 different 5-letter words
word_list = ['lucky','legal','pitch','state','lower']
# TODO Create a variable called play and set it to True
play = True

# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
print("Wordle gives you six chances to guess a secret, five-letter word. You submit valid English words, and the game provides clues after every guess to help you figure out the solution.")

# MAIN
# TODO Create a while loop that runs if play is true
while play:
 
    # TODO Create word variable and store a random word from your list (using random.choice)
    word = random.choice(word_list)

    # USER INPUT
    # TODO Get user's first guess and save it into a variable
    first_guess = input("Insert your first guess:")
    # TODO Create a while loop if the guess is not 5 characters long
    while len(first_guess) != 5:

        # TODO Tell them it's not 5 letters and to try again
        if first_guess > 5:
            print("Try again")


    # TODO Check if they got it correct and if they did, tell them so and then break the loop
        elif first_guess == word_list:
            print("You got the word!")
            break

    # TODO Create a for loop that loops 5 times

    second_guess = input("Insert your second guess:")
    while len(second_guess) != 5:

        if second_guess > 5:
            print("try again")

        elif second_guess == word_list:
            print("You got the word!")
            break

    third_guess = input("Insert your third guess:")
    while len(third_guess) != 5:

        if third_guess > 5:
            print("try again")

        elif third_guess == word_list:
            print("You got the word!")
            break

    fourth_guess = input("Insert your fourth guess:")
    while len(fourth_guess) != 5:

        if fourth_guess > 5:
            print("try again")

        elif fourth_guess == word_list:
            print("You got the word!")
            break
    
    fifth_guess = input("Insert your fifth guess:")
    while len(fifth_guess) != 5:

        if fifth_guess > 5:
            print("try again")

        elif fifth_guess == word_list:
            print("You got the word!")
            break


        # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
        

        # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position

        # TODO Else tell them that letter is wrong

# TODO Ask if they want to play again. If they don't, set play to false.


# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions