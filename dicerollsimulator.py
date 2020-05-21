import random
import randint
# sets options for dice, 1-6.
min = 1
max = 6
# gives option to repeat
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    # Print two numbers for two dice
    print random.randint(min, max),
"I am trying to figure the syntax error out here^"
    print random.randint(min, max)
"and here^"    

    roll_again = raw_input("Roll the dices again?")