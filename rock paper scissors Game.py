import random, sys, time

while True:
    print("Klassic(1) or A Computer Plays for you(2)?")
    whichone = input()
    if whichone == "2":
        which = True
        break
    elif whichone == "1":
        which = False
        break
    print("NO")
    print(" ")

print("")
print("How many points do you want to play for?")
print("If you okay with 3, tip nothing just press enter")
y = input()
if y == "":
    x = 3
else:
    x = int(y)
    print(" ")
print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while wins < x and losses < x:

    while True: # The player input loop.
        if which == False:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            playerMove = input()
            if playerMove == 'q':
              sys.exit() # Quit the program.
            if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break # Break out of the player input loop.
            print('Type one of r, p, s, or q.')
        elif which == True:
            randomNumber2 = random.randint(1, 3)
            if randomNumber2 == 1:
                playerMove = 'r'
            elif randomNumber2 == 2:
                playerMove = 'p'
            elif randomNumber2 == 3:
                playerMove = 's'
            break

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print(" ")

if wins > losses:
    print("You Win this Battel")
elif losses > wins:
    print("You Lost this Battel")
else:
    print("Ties?")

time.sleep(10)
