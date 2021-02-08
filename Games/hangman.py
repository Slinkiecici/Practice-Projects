import random

def hangman_game ():
    words = ("APPLE", "APRICOT", "GRAPE", "ORANGE", "EAGLE")                          #List of words used to randomize option
    guesses = []
    chances = 10
    word = random.choice(words)
    length =  (len(word))                                                       #Length of chosen word used to show user how many letters to guess
    length = ("_" * length)
    guesses = list(length)
    print (str(length))
    word = list(word)
    while chances > 0:                                                          #User will only get 10 chances, else the loop breaks out
        
        guess = input("Please guess a letter: ")                                #Ask for users guess
        guess = guess.capitalize()
        if guess in word:                               
            indices = [i for i, a in enumerate(word) if a == guess]             #To ensure all instances of a certain letter in a word is caught
            for i in indices:                                                   #replaces "_" with correctly guessed letters
                guesses[i] = guess
            if "_" not in guesses:                                              #win condition check, once no more "_" are present, all letters have been guessed
                final = ""
                for i in guesses:
                    final = (final + (i))
                print (final + "! Well done!")
                break
            else: 
                print (guesses)
                continue
        else:                                                                   #Incorrect guesses
            chances = chances - 1
            print ("you have " + str(chances) + " chances left. Try again!")

hangman_game()
