import copy

from chess import BLACK, WHITE, uniDict, Pawn, Rook, Knight, Queen, Bishop, King


def placePieces(self):
    for i in range(0, 8):
        self.gameboard[(i, 1)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
        self.gameboard[(i, 6)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)

    placers = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

    for i in range(0, 8):
        self.gameboard[(i, 0)] = placers[i](WHITE, uniDict[WHITE][placers[i]])
        self.gameboard[((7 - i), 7)] = placers[i](BLACK, uniDict[BLACK][placers[i]])
    placers.reverse()


def isCheck():
    pass


class Check:
    pass


def main(self):
    while True:
        self.printBoard()
        print(self.message)
        self.message = ""
        startpos, endpos = self.parseInput()
        try:
            target = self.gameboard[startpos]
        except:
            self.message = "could not find piece; index probably out of range"
            target = None

        if target:
            print("found " + str(target))
            if target.Color != self.playersturn:
                self.message = "This is Not Your Turn"
                continue
            if target.isValid(startpos, endpos, target.Color, self.gameboard):
                hasLegalMoves = False
                for position in self.gameboard:
                    piece = self.gameboard[position]
                    if piece.Color == self.playersturn:
                        for move in piece.availableMoves(position[0], position[1], self.gameboard):
                            overridegameboard = copy.deepcopy(self.gameboard)
                            overridegameboard[move] = self.gameboard[position]
                            del overridegameboard[position]
                            if isCheck() != self.playersturn:
                                hasLegalMoves = True
                                break
                if not hasLegalMoves:
                    if isCheck() == self.playersturn:
                        print("You are in checkmate. " + ({WHITE: BLACK, BLACK: WHITE})[self.playersturn] + " wins!")
                    else:
                        print("Stalemate. Nobody wins!")
                    return
                overridegameboard = copy.deepcopy(self.gameboard)
                overridegameboard[endpos] = self.gameboard[startpos]
                del overridegameboard[startpos]
                if isCheck() == self.playersturn:
                    self.message = "You are not allowed to put yourself in check!"
                else:
                    self.message = "That Move is Allowed"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    isCheck()
                    if Check:
                        self.message = "Player is in check"
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else:
                        self.playersturn = BLACK
            else:
                self.message = "invalid move" + str(target.availableMoves(startpos[0], startpos[1], self.gameboard))
                print(target.availableMoves(startpos[0], startpos[1], self.gameboard))
        else:
            self.message = "There is no Piece in That Space"


def parseInput():
    try:
        a, b = input().split('-')
        a = ((ord(a[0]) - 97), int(a[1]) - 1)
        b = (ord(b[0]) - 97, int(b[1]) - 1)
        print(a, b)
        return a, b

    except:
        print("error decoding input. please try again")
        return (-1, -1), (-1, -1)


"""def validateInput(self, *args):
    for arg in args:
        if type(arg[0]) is not type(1) or type(arg[1]) is not type(1):
            return False
    return True"""


def printBoard(self):
    print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
    for i in range(0, 8):
        print("-" * 32)
        print(chr(i + 97), end="|")
        for j in range(0, 8):
            item = self.gameboard.get((i, j), " ")
            print(str(item) + ' |', end=" ")
        print()
    print("-" * 32)


"""game class. contains the following members and methods:
two arrays of pieces for each player
8x8 piece array with references to these pieces
a parse function, which turns the input from the user into a list of two tuples denoting start and end points
a checkmateExists function which checks if either players are in checkmate
a checkExists function which checks if either players are in check
a main loop, which takes input, runs it through the parser, asks the piece if the move is valid, 
and moves the piece if it is.
If the move conflicts with another piece, that piece is removed. is check(mate) is run,
and if there is a checkmate, the game prints a message as to who wins.
"""


def isInBounds(x, y):
    """Checks if a position is on the board"""
    if 0 <= x < 8 and 0 <= y < 8:
        return True
    return False


def noConflict(gameboard, initialColor, x, y):
    """Checks if a single position poses no conflict to the rules of chess"""
    if isInBounds(x, y) and (((x, y) not in gameboard) or gameboard[(x, y)].Color != initialColor):
        return True
    return False


def availableMoves():
    print("ERROR: no movement for base class")


def AdNauseum(x, y, gameboard, Color, intervals):
    """Repeats the given interval until another piece is run into.
    if that piece is not of the same color, that square is added and
     then the list is returned"""
    answers = []
    for xint, yint in intervals:
        xtemp, ytemp = x + xint, y + yint
        while noConflict(gameboard, Color, xtemp, ytemp):

            target = gameboard.get((xtemp, ytemp), None)
            if target is None:
                answers.append((xtemp, ytemp))
            elif target.Color != Color:
                answers.append((xtemp, ytemp))
                break
            else:
                break

            xtemp, ytemp = xtemp + xint, ytemp + yint
    return answers


def isValid(startpos: object, endpos, Color, gameboard):
    if endpos in availableMoves(startpos[0], startpos[1], gameboard, Color):
        return True
    return False


class Piece:

    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.Color = color

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


chessCardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
chessDiagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
