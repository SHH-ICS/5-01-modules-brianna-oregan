# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random

number1 = random.randint(1,100) # generate the 2 random numbers 1-100
number2 = random.randint(1,100)

print("What is", number1, "+", number2, "?") #asks user the addition question

while True:
    try:
        userAnswer = int(input("Your answer: ")) #gets and validates the user's answer
        break # exit loop and continue on when it's determined the user's answer is valid
    except ValueError:
        print("Invalid answer. Please enter an integer value.")

correctAnswer = number1 + number2 # calculates the right answer

if userAnswer == correctAnswer:
    print("Correct!")
else:
    print("Incorrect! The correct answer is " + str(correctAnswer) + ".")