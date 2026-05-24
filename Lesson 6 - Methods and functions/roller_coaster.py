# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input 

height = int(input("what is your height in cm?"))
age = int(input("What is your age?"))
heart_condition = input("Do you have a heart condition?")
VIP_pass = input("Do you have a VIP pass?")

# Check conditions and output verdict

if height > 150 and age > 10 and heart_condition == 'no':
    print("Access granted!")

if height > 150 and age > 10 and heart_condition == 'yes':
    print("Access denied!")

if height < 150 and age > 10 and heart_condition == 'no':
    print("Access denied!")

if height > 150 and age <= 10 and heart_condition == 'no':
    print ('Access denied!')

if height < 150 and age <= 10 and heart_condition == 'no':
    print('Access denied!')

if VIP_pass == 'yes':
    print("Access granted!")

# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient