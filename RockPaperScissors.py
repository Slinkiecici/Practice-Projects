import random


possibilities = ['R','P','S']
comp_score = 0
score = 0

while (abs(comp_score - score) <2) or (comp_score <= 1 or score <= 1):                       #and (comp_score+score/2).is_integer()
    move = input("Rock = R, Paper = P, Scissors = S. Give your move: ")
    comp_move = random.choice(possibilities)
    if move == "R":
        if move == comp_move:
            print ("Tied!")
        elif comp_move == "P":
            print ("Computer played paper! You lose!")
            comp_score = comp_score +1
        elif comp_move == "S":
            print ("Computer played scissors! You win!")
            score = score + 1
    elif move == "S":
        if move == comp_move:
            print ("Tied!")
        elif comp_move == "R":
            print ("Computer played rock! You lose!")
            comp_score = comp_score +1
        elif comp_move == "P":
            print ("Computer played paper! You win!")
            score = score + 1
    elif move == "P":
        if move == comp_move:
            print ("Tied!")
        elif comp_move == "S":
            print ("Computer played scissors! You lose!")
            comp_score = comp_score +1
        elif comp_move == "R":
            print ("Computer played rock! You win!")
            score = score + 1
    else:
        print ("Seems you have entered an invalid move!")
    print ("Computer current score: " + str(comp_score))
    print ("Your current score: " + str(score))
    continue
