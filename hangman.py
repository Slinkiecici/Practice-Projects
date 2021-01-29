import random

def hangman_game ():
    words = ("apple", "apricot", "grape", "orange")
    guesses = []
    chances = 10
    word = random.choice(words)
    length =  (len(word))
    length = ("_" * length)
    guesses = list(length)
    print (str(length))
    word = list(word)
    while chances > 0:
        
        guess = input("Please guess a letter: ")
        if guess in word:
            position = (word.enumerate(guess))
            print (position)
            guesses[position] = guess
            print (str(guesses))
            if "_" not in guesses:
                print (guesses)
                break
            else: continue
        else:
            print ("try again!")
            chances = chances - 1
            print (chances)



hangman_game()
