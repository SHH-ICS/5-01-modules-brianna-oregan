# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random
random.seed() # initialize the random number generator

#get the range from user
start = input("Enter the starting number of the range: ")
end = input("Enter the ending number of the range: ")

#check both inputs are valid (can be converted to integers)
try:
    start = int(start)
    end = int(end)
except ValueError:
    print("Invalid input. Please enter integer values.")
    exit() #exit if the inputs are invalid

#make sure the start number is less than the end number
if start > end:
    print("The starting number must be less than the ending number.")
    exit() #exits if range is invalid

#outputs random integer between start and end (inclusive)
randomNumber = random.randint(start, end)
print("A random number between", start, "and", end, "is:", randomNumber)