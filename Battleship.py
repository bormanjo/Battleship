from random import randint
import os

debug = True
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board(object):
    def __init__(self, size):
        self.size = size
        self.board = []
    def __repr__(self):
        return "Welcome To BattleShip"
    def cap(self, bsize):
        #Top and bottom of board boarder
        print('+','-' * (bsize + (bsize - 1)),'+')
    def create(self, bsize):
        #creates the board and saves to a list
        for x in range(0, bsize):
            self.board.append(['O'] * self.size)
    def refresh(self, gameBoard):
        #clears terminal and prints a fresh game board
        os.system('cls' if os.name == 'nt' else 'clear')
        self.cap(self.size)
        for row in gameBoard:
            screen = " ".join(row)
            print ('|', screen, '|')
        self.cap(self.size)
        
class Enemies(object):
    def __init__(self, quantity):
        self.quantity = quantity
        self.ships = []
        self.enemies = set()
    def __repr__(self):
        return "\n ***WARNING: {0} enemy ships have entered the region.*** \n".format(self.quantity)
    def rco(self):
        #Returns a Random Coordinate
        return randint(0, newGame.size-1)
    def createEnemies(self):
        #creates a specified number of enemies
        #Coordinates are stored in a temporary list 'ships'
        ships = []
        for each in range(0, self.quantity):
            self.ships.append([''])
        for ship in range(0, self.quantity):
            self.ships[ship] = [self.rco(), self.rco()]
    def checkDuplicate(self):
        #converts temporary list into tuple to check for duplicates
        #tuple is necessary for comparing multi-d lists
        for ship in self.ships:
            s = tuple(ship)
            if s not in self.enemies:
                self.enemies.add(s)
        if debug:
            print (self.enemies)
    def wasHit(self, guess):
        #Compares guessed coordinate with tuple of enemy ships
        t = tuple(guess)
        if t in self.enemies:
            return True
        return False

class Player(object):
    def __init__(self, turns):
        self.turns = turns
        self.hits = 0
        self.turn = 0
        self.guessRow = None
        self.guessCol = None
    def __repr__(self):
        return "Welcome, Admiral. The enemy is approaching us and we must commence a\n premptive strike before we are attacked."
    def attack(self):
        guessCoordinate = []
        print ('Admiral, you have ', (self.turns - self.turn + 1),'/',(self.turns + 1), ' attacks remaining.')
        self.guessRow = int(input("Guess a lattitude: "))
        self.guessCol = int(input("Guess a longitude: "))
        guessCoordinate = [self.guessRow, self.guessCol]
        return guessCoordinate 

class Menu(object):
    def __init__(self):
        self.menuOn = True
        self.choice = 0
    def __repr__(self):
        return "Welcome to Battleship \n \n 1. Play Battleship \n 2. Settings \n 3. About "

#Menu
newMenu = Menu()
while newMenu.menuOn:
    print (newMenu)
    newMenu.choice = int(input("\n \nEnter a number from the list above: "))
    if newMenu.choice == 1:
        playing = True
        break
    elif newMenu.choice == 2:
        clear()
        #Print/edit Settings from file i/o
    elif newMenu.choice == 3:
        clear()
        #read bio from file
    else:
        print ("Please enter a valid selection")
#Start Game
    

while playing:

    newGame = Board(6)
    newGame.create(newGame.size)
    newGame.refresh(newGame.board)
    print (newGame)

    newEnemies = Enemies(3)
    newEnemies.createEnemies()
    newEnemies.checkDuplicate()
    print (newEnemies)

    newPlayer = Player(newEnemies.quantity + 2) #reinitiates the player and sets variables to default
    print (newPlayer)

    while newPlayer.turn <= newPlayer.turns:
        move = newPlayer.attack()
        if newEnemies.wasHit(move) and not newGame.board[newPlayer.guessRow][newPlayer.guessCol] == "H":
            newGame.board[newPlayer.guessRow][newPlayer.guessCol] = 'H'
            newPlayer.hits += 1
            newPlayer.turn += 1
            newGame.refresh(newGame.board)
            print ("You hit an enemy ship!")
        else:
            newGame.refresh(newGame.board)
            if (newPlayer.guessRow < 0 or newPlayer.guessRow >= newGame.size) or (newPlayer.guessCol < 0 or newPlayer.guessCol >= newGame.size):
                newPlayer.turn += 1
                print ("You missed! That coordinate is off the map.")
            elif (newGame.board[newPlayer.guessRow][newPlayer.guessCol] == "X" or newGame.board[newPlayer.guessRow][newPlayer.guessCol] == "H"):
                print ("You have already fired there!")
            else:
                newGame.board[newPlayer.guessRow][newPlayer.guessCol] = "X"
                newGame.refresh(newGame.board)
                newPlayer.turn += 1
                print ("You missed the enemy!")
        if newPlayer.hits == newEnemies.quantity:
            print ("Congratulations, Admiral! You saved us all from impending doom!")
            break
    playAgain = input("Would you like to play again? \n Enter y/n: ")
    if playAgain.lower() == 'y':
        playing = True
    elif playAgain.lower() == 'n':
        playing = False
        break
        
    

















