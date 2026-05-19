
print("Welcome to the quiz where we find out the perfect animal for you!")\

# first question 
first_question = input ('Would you like to go on walks with your pet?')
if first_question == 'yes':
 
 # second question 
 second_question = input('Do you suit a more social pet?')
 if second_question == 'yes':
  print('you got a dog!')
 else:
  print('You got a ferret!')

# third question
else:
 third_question = input('Do you like soft animals? ')
 if third_question == 'yes':
  print('You got a cat!')
 else:
  print('You got a fish!')
