import random
import sys

print('Rock , Paper, Scissors')
win = 0
losses = 0
tie = 0
counter = 0
while counter < 5:
    comp = random.randint(1, 3)
    person = input("Enter your move (r)ock, (p)aper, (s)cissors and q(uit)")

    if person == 'r':
        if comp == 1:
            print('Rock versus Rock')
            print('You tie')
            tie += 1

        elif comp == 2:
            print('Rock versus Paper')
            print('You Lose')
            losses += 1
        elif comp == 3:
            print('Rock versus scissors')
            print('You win')
            win += 1
        else:
            pass

    elif person == 'p':
        if comp == 1:
            print('Paper versus Rock')
            print('You win')
            win += 1
        elif comp == 2:
            print('Paper versus paper')
            print('You tie')
            tie += 1
        elif comp == 3:
            print('Paper versus scissors')
            print('You loose')
            losses += 1
        else:
            pass

    elif person == 's':
        if comp == 1:
            print('Scissor versus rock')
            print('You loose')
            losses += 1
        elif comp == 2:
            print('Scissor versus paper')
            print('You win')
            win += 1
        elif comp == 3:
            print('Scissor versus scissor ')
            print('You tie')
            tie += 1
    elif person == 'q':
        sys.exit()
    else:
        print('Invalid move try again')
    counter += 1

print(f'wins: {win}, loses: {losses}, tie: {tie}')