from random import randint
import os

debug = True

class Board(object):
    def __init__(self, size):
        self.size = size
    def __repr__(self):
        return "Welcome To BattleShip"
    board=[]
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
    ships = []
    enemies = set()
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
        #tuple is necessary for checking multi-d lists
        seen = []
        for ship in self.ships:
            s = tuple(ship)
            if s not in self.enemies:
                seen.append(ship)
                self.enemies.add(s)
        if debug:
            print (self.enemies)
            

newGame = Board(6)
print (newGame)
newGame.create(newGame.size)
newGame.refresh(newGame.board)
newEnemies = Enemies(3)
newEnemies.createEnemies()
newEnemies.checkDuplicate()
            
