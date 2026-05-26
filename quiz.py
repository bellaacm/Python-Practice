### QUIZ ###
# this is a 10 question quiz involving a large variety of topics 

# QUIZ INTRODUCTION 
name = input("What is your name?")
print(f"hello {name}, welcome to this quiz!")
print("This will be a 10 question quiz assesing your general knowledge.")


## SCORE



## QUESTION 1
print("First question:")
first_question = input("What is the worlds tallest building?")

first_question = first_question.strip().lower()

# output 
if first_question == 'the burj khalifa':
   print("Good job!")

else:
   print("Incorrect")

first_question_answer = print("As of 2026, the worlds tallest building is The Burj Khalifa in Dubai.")





## QUESTION 2
print("Second question:")
second_question = input("What is the largest ocean on Earth?")

second_question = second_question.strip().lower()

# output
if second_question == 'the pacific ocean':
   print("Good job!")

else:
   print("Incorrect")
   
second_question_answer = print("The largest ocean on Earth is the Pacific Ocean.")





## QUESTION 3
print("Third question:")
third_question = input("Who was the first person to walk on the moon?")

third_question = third_question.strip().lower()

# output 
if third_question == 'neil armstrong':
   print("Good job!")

else:
   print("Incorrect")

third_question_answer = print("The first person to walk on the moon was Neil Armstrong.")





## QUESTION 4
print("Fourth question:")
fourth_question = input("Which superhero is known as the 'Man of Steel'?")

fourth_question = fourth_question.strip().lower()

# output 
if fourth_question == 'superman':
   print("Good job!")

else:
   print("Incorrect")

fourth_question_answer = print("Superman is known as the 'Man of Steel'.")





## QUESTION 5
print("Fifth question:")
fifth_question = input("What is the highest rated TV show?")

fifth_question = fifth_question.strip().lower()

# output 
if fifth_question == 'breaking bad':
   print("Good job!")

else:
   print("incorrect")

fifth_question_answer = print("The highest rated TV show is Breaking Bad.")





## QUESTION 6 
print("Sixth question:")
Sixth_question = input("How many days does it take for the Earth to orbit the Sun?")

Sixth_question = Sixth_question.strip().lower()

# output 
if Sixth_question == '365':
   print("Good job!")

else:
   print("Incorrect")
   
Sixth_question_answer = print("It takes 365 days for the Earth to orbit the Sun.")





# QUESTION 7
print("Seventh question:")
Seventh_question = input("What are the two national animals of Australia?")

Seventh_question = Seventh_question.strip().lower()

# output 
if Seventh_question == 'red kangaroo and emu':
   print("Good job!")

else:
   print("Incorrect")

Seventh_question_answer = print("The red kangaroo and the emu are the two national animals of Austrailia.")





## QUESTION 8 
print("Eighth question:")
Eighth_question = input("Which artist painted the ceiling of the Sistine Chapel in Rome?")

Eighth_question = Eighth_question.strip().lower()

# output 
if Eighth_question == 'michelangelo':
   print("Good job!")

else:
   print("Incorrect")

Eighth_question_answer = print("Michelangelo painted the ceiling of the Sistine Chapel in Rome.")





## QUESTION 9
print("Ninth question:")
Ninth_question = input("What is the only body part fully grown from birth?")

Ninth_question = Ninth_question.strip().lower()

# output 
if Ninth_question == 'eyes':
   print("Good job!")

else:
   print("Incorrect")

Ninth_question_answer = print("The only body part fully grown from birth are your eyes.")






## QUESTION 10 
print("Tenth and final question:")
Tenth_question = input("What are a groups of crows called?")

Tenth_question = Tenth_question.strip().lower()

# output 
if Tenth_question == 'murder':
   print("Good job!")

else:
   print("Incorrect")

Tenth_question_answer = print("A group of crows are famously reffered to as a 'murder'.")





# outro
print("This is the end of the quiz.")
input("How many questions did you answer correctly?")
print(f"Congratulations! Thank you {name} for participating in this quiz :)" )













