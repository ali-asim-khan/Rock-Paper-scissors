import random
print("\n<<< Rock, Paper, Scissors >>>\n")

rounds = int(input("How many rounds do you want to play?: "))
while rounds != 0:

    AI = int(random.randrange(1,4))
    if AI == 1:
        AIO = 'Rock'
    elif AI == 2:
        AIO = 'Paper'
    else:
        AIO = 'Scissors'

    player = int(input("1: Rock, 2: Paper, 3: Scissors?: "))
    if player == 1:
        print("I go for: " + AIO)
        if AI == 3:
            print("You win")
        elif AI == 1:
            print("It's a draw")
        else:
            print("I win")

    elif player == 2:
        print("I go for: " + AIO)
        if AI == 1:
            print("You win")
        elif AI == 2:
            print("It's a draw")
        else:
            print("I win")

    elif player == 3:
        print("I go for: " + AIO)
        if AI == 2:
            print("You win")
        elif AI == 3:
            print("It's a draw")
        else:
            print("I win")
    rounds = rounds - 1