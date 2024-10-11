# Programmer: Teresa Fischer
# Date: 10/8/24
# Program #1: Random Dice


# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    num_1 = random.randint(1, 6)
    num_2 = random.randint(1, 6)
    # Sum 2 numbers
    sum = 0
    sum = num_1 + num_2
    # return sum to calling function
    return sum
    #########
    # Then write a mainline that calls the "randDice" function 100 times in a for loop.
def main():
    total_sum = 0
    for i in range(1,101):
        total_sum = total_sum + randDice()
    average = total_sum / 100
    print('Average of 100 rolls:', float(f"{average :.2f}"))
    # The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

main()