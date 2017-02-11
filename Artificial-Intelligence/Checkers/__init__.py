class Player:

    def __init__(self):
        pass

class Piece:

    def __init__(self, colour):
        self.colour = colour
        if colour is ' ' or colour is '.':
            self.isActive = False
        else:
            self.isActive = True

class Board:

    size = 8

    def setUpBoard(self):

        matrix = [[Piece(' ') for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):

                if i is 0 or i is 2:
                    if j % 2 is 1:
                        matrix[i][j] = Piece('w')
                elif i is 1:
                    if j % 2 is 0:
                        matrix[i][j] = Piece('w')
                elif i is 5 or i is 7:
                    if j % 2 is 0:
                        matrix[i][j] = Piece('b')
                elif i is 6:
                    if j % 2 is 1:
                        matrix[i][j] = Piece('b')
                else:
                    if j % 2 is 0:
                        matrix[3][j] = Piece('.')
                    else:
                        matrix[4][j] = Piece('.')

        return matrix

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print self.boardState[i][j].colour,
            print ""

    def switchTurns(self):
        if self.currentTurn is self.player1:
            self.currentTurn = self.player1
        else:
            self.currentTurn = self.player2

    def validMoves(self):
        """player1 is x and player2 is y"""
        if self.currentTurn is self.player1:
            """look for valid w moves"""

        else:
            """look for valid b moves"""

    def __init__(self):
        self.boardState = self.setUpBoard()
        self.player1 = Player
        self.player2 = Player
        self.currentTurn = self.player1


if __name__ == '__main__':

    x = Board()
    x.printBoard()