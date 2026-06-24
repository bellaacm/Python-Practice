### QUIZ ###
# this is a 10 question quiz involving a large variety of general knowledge topics 

## QUIZ INTRODUCTION 

name = input("What is your name?")
print(f"Hello {name}, welcome to this quiz!")
print()
print("This will be a 10 question quiz assesing your general knowledge.")
print("You will have to enter the letter of your answer from the given options. ( ex:'a' or 'd')")
print("( •̀ ᗜ •́ )ᕗ")
print()

def ready():
    
 while True:
    ready = input("Are you ready to begin?").strip().lower() 
      
    if ready in ["yes","y","ye","sure","ready", "yeah","absolutely","definitely"]:
           print("Great! let's begin.")
           return

    else:
            print("Come back when you're ready!")
            exit
ready()

## SCORE 
score = 0

## ANSWER OPTIONS 
answer_options = ["a","b","c","d"]

## QUIZ MAIN FUNCTION
def main():
    
## QUESTION 1
 print()
print("First question:")
first_question = input("What is the worlds tallest building? a) Burj Khalifa, b) Shanghai Tower, c) Makkah Clock Royal Tower, d) Merdeka 118")
first_question = first_question.strip().lower()
print()

    # QUESTION 1 ANSWER
if first_question == 'a':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1

elif first_question not in answer_options:
  print("answer not applicable. Try again: ")
  


else:
        print("Incorrect!")
        print("(ó﹏ò｡)")

first_question_answer = print("As of 2026, the worlds tallest building is The Burj Khalifa in Dubai.")
print()


## QUESTION 2
print("Second question:")
second_question = input("What is the largest ocean on Earth? a) Atlantic Ocean, b) Southern Ocean, c) Pacific Ocean, d) Arctic Ocean")
second_question = second_question.strip().lower()
print()

    # OUTPUT
if second_question == 'c':
    print("Good job!")
    print("◝(ᵔᗜᵔ)◜")
    score += 1
else:
    print("Incorrect!")
    print("(ó﹏ò｡)")
        
second_question_answer = print("The largest ocean on Earth is the Pacific Ocean.")
print()




## QUESTION 3
print("Third question:")
third_question = input("Who was the first person to walk on the moon? a) Valentina Tereshkova, b) Neil Armstrong, c) John Glenn, d) Yuri Gagarin")
third_question = third_question.strip().lower()
print()

# QUESTION 3 ANSWER
if third_question == 'b':
    print("Good job!")
    print("◝(ᵔᗜᵔ)◜")
    score += 1
else:
  print("Incorrect!")
  print("(ó﹏ò｡)")

third_question_answer = print("The first person to walk on the moon was Neil Armstrong.")
print()




## QUESTION 4
print("Fourth question:")
fourth_question = input("Which superhero is known as the 'Man of Steel'? a) Batman, b) Wonder Woman, c) Superman, d) Green Lantern")
fourth_question = fourth_question.strip().lower()
print()

# QUESTION 4 ANSWER 
if fourth_question == 'c':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1
else:
   print("Incorrect!")
   print("(ó﹏ò｡)")

fourth_question_answer = print("Superman is known as the 'Man of Steel'.")
print()




## QUESTION 5
print("Fifth question:")
fifth_question = input("What is the highest rated TV show? a) Breaking Bad, b) Black Mirror, c) Stranger Things, d) Dark")
fifth_question = fifth_question.strip().lower()
print()

# OUTPUT
if fifth_question == 'a':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1
else:
   print("Incorrect!")
   print("(ó﹏ò｡)")

fifth_question_answer = print("The highest rated TV show is Breaking Bad with a rating of 9.5/10 on IMDB.")
print()




## QUESTION 6 
print("Sixth question:")
Sixth_question = input("How many days does it take for the Earth to orbit the Sun? a) 350, b) 256, c)366, d) 356")
Sixth_question = Sixth_question.strip().lower()
print()

    # QUESTION 6 ANSWER
if Sixth_question == 'd':
        print("Good job!")
        print("◝(ᵔᗜᵔ)◜")
        score += 1
else:
        print("Incorrect!")
        print("(ó﹏ò｡)")
        
Sixth_question_answer = print("It takes 365 days for the Earth to orbit the Sun.")
print()




# QUESTION 7
print("Seventh question:")
Seventh_question = input("What are the two national animals of Australia? a) Kangaroo & Koala, b) Platypus & Emu, c) Kangaroo & Emu, d) Crocodile & Koala")
Seventh_question = Seventh_question.strip().lower()
print()

    # OUTPUT 
if Seventh_question == 'c':
        print("Good job!")
        print("◝(ᵔᗜᵔ)◜")
        score += 1
else:
        print("Incorrect!")
        print("(ó﹏ò｡)")

Seventh_question_answer = print("The red kangaroo and the emu are the two national animals of Austrailia.")
print()




## QUESTION 8 
print("Eighth question:")
Eighth_question = input("Which artist painted the ceiling of the Sistine Chapel in Rome? a) Leonardo da Vinci, b) Michelangelo, c) Raphael, d) Rembrandt van Rijn")
Eighth_question = Eighth_question.strip().lower()
print()

    # OUTPUT
if Eighth_question == 'b':
        print("Good job!")
        print("◝(ᵔᗜᵔ)◜")
        score += 1
else:
        print("Incorrect!")
        print("(ó﹏ò｡)")

Eighth_question_answer = print("Michelangelo painted the ceiling of the Sistine Chapel in Rome.")
print()




## QUESTION 9
print("Ninth question:")
Ninth_question = input("What is the only body part fully grown from birth? a) eyes, b) nose, c) tongue, d) ears")
Ninth_question = Ninth_question.strip().lower()
print()

    # OUTPUT
if Ninth_question == 'a':
        print("Good job!")
        print("◝(ᵔᗜᵔ)◜")
        score += 1
else:
        print("Incorrect!")
        print("(ó﹏ò｡)")

Ninth_question_answer = print("The only body part fully grown from birth are your eyes.")
print()





## QUESTION 10 
print("Tenth and final question:")
Tenth_question = input("What are a groups of crows called? a) a gaggle, b) a parliment, c) a flamboyance, d) a murder")
Tenth_question = Tenth_question.strip().lower()
print()

# OUTPUT
if Tenth_question == 'd':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1
else:
   print("Incorrect!")
   print("(ó﹏ò｡)")

Tenth_question_answer = print("A group of crows are famously reffered to as a 'murder'.")
print()

    # OUTRO
print("This is the end of the quiz.")
print(f"You scored {score} out of 10.") 
print()
print(f"Congratulations! Thank you {name} for participating in this quiz")
print("(ㅅ´ ˘ `)")
print()

# REPLAY LOOP
while True:
    replay = input("Would you like to play again? ∘ ∘ ∘ ( °ヮ° )").lower().strip()
    
    if replay in ["yes","y","ye","sure","ready", "yeah","absolutely","definitely"]:
         main()

    else:
        print("See you next time!")
        break












