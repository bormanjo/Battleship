from random import randint
import os

#setup board
def setup():
    for x in range(0, bsize):
        board.append(['O']*bsize)
    print ("Welcome to Battleship")
#board functions
def cls():
    print('\n' * 100)
    os.system('clear')
    os.system('cls')
def cap(bsize): #Top and bottom of board boarder
    print('+','-' * (bsize + (bsize - 1)),'+')
def createBoard(board, clear):
    if clear:
        cls()
    cap(bsize)
    for row in board:
        screen = " ".join(row)
        print ('|',screen,'|')
    cap(bsize)
def rRow(board):
    return randint(0, bsize-1)
def rCol(board):
    return randint(0, bsize-1)

#create enemy ships (numships)
def initShips():
    for x in range(0, numships):
        ships.append([''])
    for ship in range(0, numships):
        ships[ship] = [rRow(board), rCol(board)]
    print (ships)

#tests if ship location was hit
def shipLoc(guess):
    for s in range(0, numships):
        if guess == ships[s]:
            return True
    return False

#start game
playing = True
while playing:
    #initVars()
    board = []      #board stored as a list
    bsize = 6       #size of board
    hits = 0        #number of hits on enemy ships
    ships = []      #ship locations stored as a list
    numships = 2    #number of enemy ships
    turns = 6       #number of turns
    cls()
    setup()
    createBoard(board, False)
    initShips()
    for turn in range(1, turns + 1): 
        print ('Turn: ', str(turn), '/', str(turns))
        guess = []
        guessRow = int(input("Guess Row: "))
        guessCol = int(input("Guess Col: "))
        guess = [guessRow, guessCol]
        if shipLoc(guess) and not board[guessRow][guessCol] == "H" :
            board[guessRow][guessCol] = "H"
            hits += 1
            createBoard(board, True)
            print ("You hit an enemy battleship")
        else:
            createBoard(board, True)
            if (guessRow < 0 or guessRow > 5) or (guessCol < 0 or guessCol > 5):
                turn -= 1
                print ('That coordinate is outside the battlefield.')
            elif (board[guessRow][guessCol] == "X" or board[guessRow][guessCol] == "H"):
                print ("You have already fired there.")
            else:
                board[guessRow][guessCol] = "X"
                createBoard(board, True)
                print("You missed!")
        if hits == numships:
            print('\n Congratulations! You won!')
            break
    play = input("Would you like to play again? \n Enter y/n: ")
    if play == 'y':
        playing = True
    elif play == 'n':
        playing = False
        break
