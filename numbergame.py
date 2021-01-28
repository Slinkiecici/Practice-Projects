from random import randint

def guess_the_number ():
    number = randint(0, 10)
    guessed = 1
    while guessed == 1:
        print (number)
        guess = input("guess the number: ")
        guess = int(guess)
        if guess == number:
            print ("Well done!")
            guessed = 0
            break
        elif guess > number:
            print ("Your guess is too high!")
        elif guess < number:
            print ("Your guess is too low!")
        else:
            print ("Invalid input")
        continue

guess_the_number()