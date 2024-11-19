# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.

import math

a = input("Enter the length of leg a: ")

try: #check if input is valid
    a = float(a)
except ValueError:
    print("Invalid input for leg a. Please enter a numeric value.")
    exit()

b = input("Enter the length of leg b: ")

try:
    b = float(b)
except ValueError:
    print("Invalid input for leg b. Please enter a numeric value.")
    exit()

c = math.sqrt(a**2 + b**2)

print("the length of the hypoteneuse is: " + str(round(c, 2)))