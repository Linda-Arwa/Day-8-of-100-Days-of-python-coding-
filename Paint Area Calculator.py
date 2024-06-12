# A program that calculates the number of cans of paint needed in a room given the height of wall and width
# Instructions on the paint can say 1 paint can covers 5 sq. meters of the wall.

# solution

#Importing the math function coz we are going to use math.ceil() which rounds up a number to the nearest integer  e.g 16.1 becomes 17

import math

height = input("Enter the height of the wall you are going to paint\n") 
width = input("Enter the width of the wall you are going to paint\n")
coverage = 5

# converting the str to float

height = float(height)
width = float(width)

# Defining our function

def paint(height, width, coverage):
#Calculating the area of the room.
    Area = height * width

# Calculating the number of cans needed
    No_of_cans = Area / coverage
    
# rounding off to whole numbers
    No_of_cans = math.ceil(No_of_cans)  

    print(f"This wall requires {No_of_cans} cans of paint")
    
# Calling the function:

paint(height, width,coverage)