#Tic Tac Toe

class Board:

    def __init__(self, square1 =' ', square2=' ', square3=' ', square4=' ', square5=' ', square6=' ', square7=' ', square8=' ', square9=' '):
        self.square1 = square1
        self.square2 = square2
        self.square3 = square3
        self.square4 = square4
        self.square5 = square5
        self.square6 = square6
        self.square7 = square7
        self.square8 = square8
        self.square9 = square9

    def grid(self):
        message = '\nSQUARES ARE 0-8, TOP LEFT TO BOTTOM RIGHT, TRAVEL HORIZONTALLY\n  | | \n ' +self.square1+' | '+self.square2+' | '+self.square3+' \n___|___|___\n  | | \n '+self.square4+' | '+self.square5+' | '+self.square6+' \n___|___|___\n  | | \n '+self.square7+' | 'self.square8+' | '+self.square9+' \n | | '
        print(message)

game= Board()

print(game.grid)

while True:
    entry = raw_input('Please enter a number\n')
    if entry == '0':
        game.square1='X'

    elif entry == '1':
        game.square2='X'

    elif entry == '2':
        game.square3='X'

    elif entry == '3':
        game.square4='X'

    elif entry == '4':
        game.square5='X'

    elif entry == '5':
        game.square6='X'

    elif entry == '6':
        game.square7='X'

    elif entry == '7':
        game.square8='X'

    elif entry == '8':
        game.square9='X'

    print(game.grid())