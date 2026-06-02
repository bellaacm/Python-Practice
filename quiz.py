### QUIZ ###
# this is a 10 question quiz involving a large variety of general knowledge topics 

## QUIZ INTRODUCTION 
name = input("What is your name?")
print(f"Hello {name}, welcome to this quiz!")
print("This will be a 10 question quiz assesing your general knowledge.")
print("( •̀ ᗜ •́ )ᕗ")
print()

## SCORE
score = 0


## QUESTION 1
print("First question:")
first_question = input("What is the worlds tallest building?")
print()

first_question = first_question.strip().lower()

# OUTPUT
if first_question == 'the burj khalifa' or first_question == 'burj khalifa':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1

else:
   print("Incorrect!")
   print("(ó﹏ò｡)")

first_question_answer = print("As of 2026, the worlds tallest building is The Burj Khalifa in Dubai.")
print()




## QUESTION 2
print("Second question:")
second_question = input("What is the largest ocean on Earth?")
print()

second_question = second_question.strip().lower()

# OUTPUT
if second_question == 'the pacific ocean' or second_question == 'pacific ocean' or second_question == 'pacific':
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
third_question = input("Who was the first person to walk on the moon?")
print()

third_question = third_question.strip().lower()

# OUTPUT
if third_question == 'neil armstrong':
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
fourth_question = input("Which superhero is known as the 'Man of Steel'?")
print()

fourth_question = fourth_question.strip().lower()

# OUTPUT
if fourth_question == 'superman':
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
fifth_question = input("What is the highest rated TV show?")
print()

fifth_question = fifth_question.strip().lower()

# OUTPUT
if fifth_question == 'breaking bad':
   print("Good job!")
   print("◝(ᵔᗜᵔ)◜")
   score += 1

else:
   print("Incorrect!")
   print("(ó﹏ò｡)")

fifth_question_answer = print("The highest rated TV show is Breaking Bad.")
print()




## QUESTION 6 
print("Sixth question:")
Sixth_question = input("How many days does it take for the Earth to orbit the Sun?")
print()

Sixth_question = Sixth_question.strip().lower()

# OUTPUT
if Sixth_question == '365':
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
Seventh_question = input("What are the two national animals of Australia?")
print()

Seventh_question = Seventh_question.strip().lower()

# OUTPUT 
if Seventh_question == 'red kangaroo and emu':
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
Eighth_question = input("Which artist painted the ceiling of the Sistine Chapel in Rome?")
print()

Eighth_question = Eighth_question.strip().lower()

# OUTPUT
if Eighth_question == 'michelangelo':
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
Ninth_question = input("What is the only body part fully grown from birth?")
print()
Ninth_question = Ninth_question.strip().lower()

# OUTPUT
if Ninth_question == 'eyes':
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
Tenth_question = input("What are a groups of crows called?")
print()

Tenth_question = Tenth_question.strip().lower()

# OUTPUT
if Tenth_question == 'murder':
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
print(f"You got {score} out of 10.")
print()
print(f"Congratulations! Thank you {name} for participating in this quiz")
print("(ㅅ´ ˘ `)")












