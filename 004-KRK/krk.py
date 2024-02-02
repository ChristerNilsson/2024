# https://syzygy-tables.info/
# http://tablebase.sesse.net/syzygy/3-4-5/ (download)

import random
import time

ALFABET = "0123456789abcdefghijklmnopqrstuvwxyz"
DRAW = 0
MATE = '1'

def ass(a, b):
    if a != b:
        print('Failed:', b, a)
        assert a == b

def getData(filename):
    with open(filename) as f:
        return f.read()

blackData = getData("KRKb.txt")
whiteData = getData("KRKw.txt")
ass(len(blackData), 262144)
ass(len(whiteData), 262144)

ROOK_MOVES = [[-1, 0], [0, -1], [0, 1], [1, 0]]
KING_MOVES = [[-1, -1], [-1, 0], [-1, 1],  [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def row(p): return p // 8
def col(p): return p % 8
def pos(x,y): return x+8*y
def pretty(piece): return "abcdefgh"[col(piece)] + str(1+row(piece))
def onBoard(x,y): return 0 <= x < 8 and 0 <= y < 8
def getWhiteScore(index): return whiteData[index]
def getBlackScore(index): return blackData[index]
def forwardIndex(wk,wr,bk): return 64 * 64 * wk + 64 * wr + bk

def getIndex(s):
    col = "abcdefgh".index(s[0])
    row = "12345678".index(s[1])
    return 8 * row + col

def reverseIndex(index):
    k = index % 64
    index //= 64
    j = index % 64
    index //= 64
    i = index
    return [i,j,k]

illegalSquaresBlack = []
illegalSquaresWhite = []

def sqDist(a,b):
    dx = col(a) - col(b)
    dy = row(a) - row(b)
    return dx*dx + dy*dy

def getRandomPosition(n):
    ass(n % 2, 1)
    letter = ALFABET[n]
    indexes = [i for i in range(len(whiteData)) if whiteData[i] == letter]

    i = random.choice(indexes)
    #i = 146745

    [wk,wr,bk] = reverseIndex(i)
    print('Random position:',i)
    return Position(wk,wr,bk)

def illegalSquaresBlack(wk,wr,bk): # Rutor svart kung ej får gå till
    x0 = col(wk)
    y0 = row(wk)
    result = []
    for [dx, dy] in KING_MOVES:  # WK
        x,y = x0 + dx, y0 + dy
        sq = pos(x, y)
        if onBoard(x, y) and sqDist(sq, wk) <= 2: result.append(sq)

    x0 = col(wr)
    y0 = row(wr)
    for [dx,dy] in ROOK_MOVES: # WR
        x,y = x0+dx, y0+dy
        sq = pos(x,y)
        while onBoard(x,y) and sq != wk:
            result.append(sq)
            x,y = x+dx,y+dy
            sq = pos(x,y)
    return result

def illegalSquaresWhite(wk,wr,bk): # Rutor vit kung ej får gå till
    x0 = col(bk)
    y0 = row(bk)
    result = []
    for [dx, dy] in KING_MOVES:  # BK
        x,y = x0 + dx, y0 + dy
        sq = pos(x, y)
        if onBoard(x, y) and sqDist(sq, bk) <= 2: result.append(sq)
    return result

class Position:
    def __init__(self, wk, wr, bk):  # 64
        self.set(wk,wr,bk)

    def set(self,wk,wr,bk):
        self.wk = wk
        self.wr = wr
        self.bk = bk
        self.index = forwardIndex(wk,wr,bk) # används för att slå i whiteData och blackData

    def nice(self): return pretty(self.wk) + ' ' + pretty(self.wr) + ' ' + pretty(self.bk)
    def nicestWhite(self): return "K"+pretty(self.wk) + ' R' + pretty(self.wr) + ' K' + pretty(self.bk) + ' (' + str(self.whiteScore()) + ')'
    def nicestBlack(self): return "K"+pretty(self.wk) + ' R' + pretty(self.wr) + ' K' + pretty(self.bk) + ' (' + str(self.blackScore()) + ')'
    def whiteScore(self): return getWhiteScore(self.index)
    def blackScore(self): return getBlackScore(self.index)

    def whiteMoves(self):
        res = []
        illegalSquares = illegalSquaresWhite(self.wk,self.wr,self.bk)

        x0 = col(self.wk)
        y0 = row(self.wk)
        for [dx,dy] in KING_MOVES: # WK
            x,y = x0+dx, y0+dy
            wk = pos(x,y)
            if onBoard(x,y) and wk != self.wr and wk not in illegalSquares:
                index = forwardIndex(wk, self.wr, self.bk)
                res.append([wk,self.wr,self.bk, getBlackScore(index)])

        x0 = col(self.wr)
        y0 = row(self.wr)
        for [dx,dy] in ROOK_MOVES: # WR
            x,y = x0+dx, y0+dy
            wr = pos(x,y)
            while onBoard(x,y) and wr != self.wk and wr != self.bk:
                index = forwardIndex(self.wk, wr, self.bk)
                res.append([self.wk,wr,self.bk, getBlackScore(index)])
                x,y = x+dx,y+dy
                wr = pos(x,y)

        return res

    def blackMoves(self):
        res = []
        x0 = col(self.bk)
        y0 = row(self.bk)

        illegalSquares = illegalSquaresBlack(self.wk,self.wr,self.bk)

        for [dx,dy] in KING_MOVES: # BK
            x,y = x0+dx, y0+dy
            bk = pos(x,y)
            if onBoard(x,y) and bk not in illegalSquares:
                index = forwardIndex(self.wk, self.wr, bk)
                # index = 64 * 64 * self.wk + 64 * self.wr + bk
                res.append([self.wk,self.wr,bk, getWhiteScore(index)])
        return res

ass(illegalSquaresBlack(27,3,44), [18, 26, 34, 19, 35, 20, 28, 36, 2, 1, 0, 11, 19, 4, 5, 6, 7])
ass(illegalSquaresBlack(46,3,44), [37, 45, 53, 38, 54, 39, 47, 55, 2, 1, 0, 11, 19, 27, 35, 43, 51, 59, 4, 5, 6, 7])
ass(illegalSquaresWhite(26,27,44), [35, 43, 51, 36, 52, 37, 45, 53])

ass(Position( 0, 8, 2).blackScore(), 'e')
ass(Position( 0, 8,13).blackScore(), 'q')
ass(Position( 0,16, 2).blackScore(), 'm')
ass(Position( 0,17,10).blackScore(), '|')
ass(Position( 1,54,38).blackScore(), 'w')
ass(Position( 2, 8, 4).blackScore(), 'a')

ass(Position( 2,16, 0).blackScore(), MATE)
ass(Position( 2,17, 0).blackScore(), '4')
ass(Position( 2,18, 8).blackScore(), '2')
ass(Position( 2,25, 0).blackScore(), '6')
ass(Position( 3, 5,19).blackScore(), 'u')
ass(Position( 3,45,42).blackScore(), 'u')
ass(Position( 3,54,44).blackScore(), 'u')

ass(Position( 5,39,56).blackScore(), 'q')
ass(Position( 9,27, 7).blackScore(), 'i')
ass(Position(10,33, 8).blackScore(), '8')
ass(Position(13,17,10).blackScore(), '|')
ass(Position(13,17,10).whiteScore(), 'f')
ass(Position(17,32, 2).blackScore(), 'o')
ass(Position(24,54,37).blackScore(), 'u')
ass(Position(29,17,10).blackScore(), '|')
ass(Position(36,17,46).blackScore(), 'g')
ass(Position(42,53,13).blackScore(), 'q')
ass(Position(42,53,60).blackScore(), '|')
ass(Position(49,17,10).blackScore(), '|')
ass(Position(49,17,46).blackScore(), 'q')
ass(Position(60,17,10).blackScore(), '|')

ass(Position( 9,27, 7).whiteScore(), 'd')
ass(Position( 3, 5,19).whiteScore(), 'n')

position = getRandomPosition(1) # odd number of moves

def showWhiteMoves(moves): # Ka6 (e) Ra3 (f)
    result = []
    for move in moves:
        if move[0] != position.wk: result.append(f"K{pretty(move[0])}.{move[3]}")
        if move[1] != position.wr: result.append(f"R{pretty(move[1])}.{move[3]}")
    return ' '.join(result)

def showBlackMoves(moves): return ' '.join([f"K{pretty(move[2])}.{move[3]}" for move in moves])

# def computerWhite():
#
#     while True:
#         print('Position:', position.nicest())
#         moves = position.whiteMoves()
#         moves.sort(key=lambda a: a[3])
#
#         print('  White:',showWhiteMoves(moves))
#
#         move = moves[0]
#         if move[0] != position.wk: print('  White: K'+pretty(move[0]))
#         if move[1] != position.wr: print('  White: R'+pretty(move[1]))
#
#         position.set(move[0],move[1],move[2])
#
#         blackMoves = position.blackMoves()
#         blackMoves.sort(key=lambda a: a[3])
#         alts = []
#         for i in range(len(blackMoves)):
#             [wk, wr, bk, _] = blackMoves[i]
#             if position.bk != bk: alts.append(['K' + pretty(bk), i])
#
#         alts.sort()  # alfabetiskt
#         x = int(input('  Black: ' + ' '.join([f"{alts[i][0]}_{i}" for i in range(len(alts))])+' '))
#         move = blackMoves[alts[x][1]]
#         position.set(move[0],move[1],move[2])
#
# def computerBlack():
#
#     while True:
#         print('Position: ',position.nicestBlack())
#         moves = position.blackMoves()
#         alts = []
#         for i in range(len(moves)):
#             [wk, wr, bk, _] = moves[i]
#             alts.append(['K'+pretty(bk),i])
#             # if position.wr != wr: alts.append(['R'+pretty(wr),i])
#
#         alts.sort() # alfabetiskt
#
#         x = int(input('  Black: ' + ' '.join([f"{alts[i][0]}: {i}" for i in range(len(alts))])+' '))
#         move = moves[alts[x][1]]
#         position.set(move[0],move[1],move[2])
#
#         # Black makes his best move
#         blackMoves = position.blackMoves()
#         blackMoves.sort(key=lambda a: a[3])
#         move = blackMoves[-1]
#         print('  Black: (', ' '.join(['K' + pretty(item[2]) + ' ' + item[3] for item in blackMoves]), ') K'+pretty(move[2]))
#         position.set(move[0],move[1],move[2])

def showSingleMove(a,b):
    res = ""
    if a[0] != b[0]: res += "K" + pretty(a[0])
    if a[1] != b[1]: res += "R" + pretty(a[1])
    if a[2] != b[2]: res += "K" + pretty(a[2])
    return "   " if res == "" else res

def computerBoth():  # datorn gör första draget som vit
    lastMove = [position.wk,position.wr,position.bk]
    move = lastMove
    # print('       ',position.nicestWhite())
    for i in range(20):

        print('   ', showSingleMove(move,lastMove), '|', position.nicestWhite())
        whiteMoves = position.whiteMoves()
        whiteMoves.sort(key=lambda a: a[3])

        lastMove = move
        move = whiteMoves[0]
        position.set(move[0], move[1], move[2])

        print(showSingleMove(move,lastMove), '   ', '|', position.nicestBlack())
        blackMoves = position.blackMoves()
        blackMoves.sort(key=lambda a: a[3])

        if len(blackMoves) == 0: break
        lastMove = move
        move = blackMoves[-1]
        position.set(move[0], move[1], move[2])

start = time.time_ns()

computerBoth()
#computerWhite()
#computerBlack()

print((time.time_ns()-start)/10**6)
