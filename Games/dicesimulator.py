from random import randint

def roll_dice ():
    while True:                                         #Allow continous rerolling until an input other than Y is entered.
        action = input("Roll again? Y or N?")
        action = str.capitalize(action)
        if action == "Y":
            roll = randint(1,6)
            print (roll)
        else:
            print ("Cheerio!")
            break                                       #Leaves the while loop to end the function


roll_dice()
