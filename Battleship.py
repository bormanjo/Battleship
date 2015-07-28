import os
from distutils.util import strtobool
from random import randint
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

config = ConfigParser()
config.read('Settings.ini')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_user_input(prompt, dataType):
    while True:
        try:
            if dataType == 1:       #return integer
                return int(input(prompt))
            elif dataType == 2:     #return bool y/n
                return strtobool(input(prompt))
        except ValueError:
            print("That was not a valid entry. Try again.")

class Settings(object):
    def __init__(self):
        self.settingsDict = {1:'player_turns', 2:'num_enemy_ships', 3:'board_size', 4:'debug'}
        
    def run(self):
        clear()
        increment = 1
        for item in config.items('Settings'):
            print(increment, '. ', item)
            increment += 1
        settingsChoice = get_user_input("\nTo return enter 0\nOtherwise enter the number of the value you would like to edit: ", 1)
        if settingsChoice == 0:
            clear()
            newGame.inSettings = False
        elif settingsChoice == 4:
            input("Switch Debug on/off")
            if not config.getboolean('Settings', 'debug'):
                config.set('Settings', 'debug', 'true')
            else:
                config.set('Settings', 'debug', 'false')
        elif settingsChoice in self.settingsDict:
            valueChoice = get_user_input("Enter the new value of {0}: ".format(self.settingsDict[settingsChoice]), 1)
            self.change_value(settingsChoice, valueChoice)
            if not self.validate_settings():
                self.reset()
        else:
            print("That is not a valid entry. Try again.")
        with open('Settings.ini', 'w') as configfile:
            config.write(configfile)
            
    def change_value(self, choice, value):
        if debug: print(self.settingsDict[choice])
        config.set("Settings", self.settingsDict[choice], str(value))
    def validate_settings(self):
        board_size = config.getint('Settings', 'board_size')
        enemy_ships = config.getint('Settings', 'num_enemy_ships')
        player_turns = config.getint('Settings', 'player_turns')
        if (board_size < 1 or board_size > 10) or (player_turns < enemy_ships or player_turns < 0) or (enemy_ships < 0 or enemy_ships > board_size**2):
            return False
        else:
            return True
    def reset(self):
        print("***Error: Invalid entry. Settings reset.***")
        config.set('Settings', 'player_turns', '8')
        config.set('Settings', 'num_enemy_ships', '3')
        config.set('Settings', 'board_size', '6')
        config.set('Settings', 'debug', 'false')
                   
class Game(object):
    def __init__(self):
        self.inProgram = True
        self.inMenu = True
        self.inGame = False
        self.inSettings = False
        self.inAbout = False
        
    def __repr__(self):
        return "Welcome to Battleship \n"
    
    def menu(self):
        print("\n 1. Play Battleship \n 2. Settings \n 3. About \n 4. Quit ")
        menuChoice = get_user_input("\nEnter a number from the list above: ", 1)
        options = {1:self.enter_game, 2:self.enter_settings, 3:self.enter_about, 4:self.terminate}
        try:
            options[menuChoice]()
        except KeyError:
            clear()
            print("That was not a valid entry. Try Again.")
        
    def enter_game(self):
        self.inGame = True
        self.inMenu = False
    def enter_menu(self):
        self.inGame = False
        self.inMenu = True
    def enter_settings(self):
        self.inSettings = True
    def enter_about(self):
        self.inAbout = True
    def terminate(self):
        print("Terminating Program...")
        self.inGame = False
        self.inMenu = False
        self.inProgram = False
        
    def about(self):
        clear()
        aboutfile = open('About.txt', 'r')
        for line in aboutfile:
            print(line)
        aboutfile.close()
        input('\n\nHit enter to return to the Main Menu: ')
        clear()
        self.inAbout = False
    def play_again(self):
        playAgain = get_user_input("Would you like to play again? \n Enter y/n: ", 2)
        if playAgain:
            self.enter_game()
        elif not playAgain:
            self.enter_menu()
        clear()

class Board(object):
    def __init__(self):
        self.size = config.getint('Settings','board_size')
        self.board = []
        self.centerSpacing = (" " * 20)
    def board_cap(self, bsize):
        print(self.centerSpacing, '+', '-' * ((bsize * 2) - 1),'+')
    def create(self, bsize):
        for x in range(0, bsize):
            self.board.append(['O'] * self.size)
    def refresh(self, gameBoard):
        self.board_cap(self.size)
        for row in gameBoard:
            screen = " ".join(row)
            print (self.centerSpacing,'|', screen, '|')
        self.board_cap(self.size)
        
class Enemy(object):
    def __init__(self):
        self.quantity = config.getint("Settings","num_enemy_ships")
        self.ships = []
        self.enemies = set()
    def __repr__(self):
        return "\n ***WARNING: {0} enemy ships have entered the region.*** \n".format(self.quantity)
    def random_coordinate(self):
        return randint(0, newBoard.size-1)
    def create_enemies(self):
        ships = []
        for each in range(0, self.quantity):
            self.ships.append([''])
        for ship in range(0, self.quantity):
            self.ships[ship] = [self.random_coordinate(), self.random_coordinate()]
    def check_duplicate(self):
        del self.enemies
        self.enemies = set()
        for ship in self.ships:
            s = tuple(ship)
            if s not in self.enemies:
                self.enemies.add(s)
    def was_hit(self, guess):
        #Compares guessed coordinate with tuple of enemy ships
        t = tuple(guess)
        if t in self.enemies:
            return True
        return False

class Player(object):
    def __init__(self):
        self.turns = config.getint('Settings', 'player_turns')
        self.hits = 0
        self.turn = 0
        self.guessRow = None
        self.guessCol = None
    def __repr__(self):
        return "Welcome, Admiral. The enemy is approaching us and we must commence a\n premptive strike before we are attacked."
    def attack(self):
        guessCoordinate = []
        print('Admiral, you have ', (self.turns - self.turn + 1),'/',(self.turns + 1), ' attacks remaining.')
        if debug: print(newEnemies.enemies)
        self.guessRow = get_user_input("Guess a lattitude: ", 1)
        self.guessCol = get_user_input("Guess a longitude: ", 1)
        guessCoordinate = [self.guessRow, self.guessCol]
        return guessCoordinate 

#Menu
newGame = Game()
newSettings = Settings()
while newGame.inProgram:
    
    while newGame.inMenu:
        debug = config.getboolean('Settings', 'debug')
        print(newGame)
        newGame.menu()
        while newGame.inSettings:
            newSettings.run()
        while newGame.inAbout:
            newGame.about()
        
    while newGame.inGame:
        clear()
        newBoard = Board()
        newBoard.create(newBoard.size)
        newBoard.refresh(newBoard.board)

        newEnemies = Enemy()
        newEnemies.create_enemies()
        newEnemies.check_duplicate()
        print (newEnemies)

        newPlayer = Player()                    #reinitiates the player and sets variables to default
        print (newPlayer)

        while newPlayer.turn <= newPlayer.turns:
            move = newPlayer.attack()
            if newEnemies.was_hit(move) and not newBoard.board[newPlayer.guessRow][newPlayer.guessCol] == "H":
                clear()
                newBoard.board[newPlayer.guessRow][newPlayer.guessCol] = 'H'
                newPlayer.hits += 1
                newPlayer.turn += 1
                print("You hit an enemy ship at {0}!".format([newPlayer.guessRow, newPlayer.guessCol]))
                newBoard.refresh(newBoard.board)
            else:
                clear()
                if (newPlayer.guessRow < 0 or newPlayer.guessRow >= newBoard.size) or (newPlayer.guessCol < 0 or newPlayer.guessCol >= newBoard.size):
                    newPlayer.turn += 1
                    print ("You missed! That coordinate is off the map.")
                elif (newBoard.board[newPlayer.guessRow][newPlayer.guessCol] == "X" or newBoard.board[newPlayer.guessRow][newPlayer.guessCol] == "H"):
                    print ("You have already fired there!")
                else:
                    newBoard.board[newPlayer.guessRow][newPlayer.guessCol] = "X"
                    newBoard.refresh(newBoard.board)
                    newPlayer.turn += 1
                    print ("You missed the enemy!")
                newBoard.refresh(newBoard.board)
            if newPlayer.hits == newEnemies.quantity:
                print ("Congratulations, Admiral! You saved us all from impending doom!")
                break
           
        newGame.play_again()
        

















