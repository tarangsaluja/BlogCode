#Import the mathematics library in order to do mathematical operations.
import math

#This code block asks for an integer value of x_squared. 
#If the user provides a non-integer value, a ValueError is detected.
#If a ValueError is detected, the user is asked to re-enter a value. 
while True:
    try:
        x_squared = int(input("What is the value of x-squared?"))
        break
    except ValueError:
        print("Please enter an integer.")

#The number of digits of x_squared is computed. 
#That is used to find the number of zeros in the power of 10 upper bound for x
#The number of zeros in the upper bound of x is the amount needed so that
#the upper bound squared has as many zeros as the number of digits in x_squared
digits = len(str(x_squared))
power_for_10 = math.ceil(digits/2)

#find upper bound and lower bound
upper_bound = 10 ** (power_for_10)
lower_bound = 0

#initialize guess and number of guesses made
guess = -1
count = 0

#Repeat until correct guess is found
#let guess be equal to average of upper bound and lower bound
#print out the upper bound, lower bound, guess, and number of guesses
#If guess squared is larger than x_squared,then make guess the new upper bound
# If guess squared is smaller than x_squared, then make guess the new lower bound 
while (guess**2 != x_squared):

    guess = int((lower_bound + upper_bound)//2)
    count += 1

    print(f"Your lower bound is {lower_bound} and your upper bound is {upper_bound}.")
    print(f"This is guess number {count}. Your guess is {guess}.")
    if guess**2 > x_squared:
        upper_bound = guess 
    else:
        lower_bound = guess
    





    



    




