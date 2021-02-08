from random import randint                              #import for generating a random number (in this case only a random integer)

def guess_the_number ():                                #function holding mechanism for game
    number = randint(0, 10)                             #initialise the random number
    guessed = 1                                         #This is variable is used to keep a user in a loop till the correct value is input
    score = 100                                         #Starting score for game
    while guessed == 1:
        guess = input("guess the number: ")             #user guess input
        guess = int(guess)
        if guess == number:
            print ("Well done!")
            guessed = 0                                 #guessed value only changed to 0 once condition is met
            print ("You socred " + str(score) + "/100")
            break
        elif guess > number:
            print ("Your guess is too high!")
            score = (score-1)
        elif guess < number:
            print ("Your guess is too low!")
            score = (score-1)
        else:
            print ("Invalid input")
        continue

guess_the_number()