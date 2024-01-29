# Omvandla csv-filen till 3D matris, 10*64*64 + 40960 bytes.

import pandas as pd

ROOK_MOVES = [[-1, 0], [1, 0], [0, -1], [0, 1]]
KING_MOVES = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

dataset = pd.read_csv('chess_king_rook_dataset.csv')
n = len(dataset['bkf'])

index = {'zero':'0', 'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8',
         'nine':'9','ten':'a', 'eleven':'b','twelve':'c','thirteen':'d','fourteen':'e','fifteen':'f','sixteen':'g', 'draw':'r' }
result = ''.join([index[dataset['result'][i]] for i in range(n)])

wk2ten = {27: 9,   18: 7, 19: 8,   9: 4, 10: 5, 11: 6,   0: 0, 1: 1, 2: 2, 3: 3}

ten2wk = [0,1,2,3,9,10,11,18,19,27]

WK = ["abcdefgh".index(dataset['wkf'][i]) + 8 * (dataset['wkr'][i]-1) for i in range(n)]
WR = ["abcdefgh".index(dataset['wrf'][i]) + 8 * (dataset['wrr'][i]-1) for i in range(n)]
BK = ["abcdefgh".index(dataset['bkf'][i]) + 8 * (dataset['bkr'][i]-1) for i in range(n)]

matrix = [99] * 10 * 64 * 64

TRANS = [  # used to find number of rotations [row][col]
    0,0,0,0,1,1,1,1,
    0,0,0,0,1,1,1,1,
    0,0,0,0,1,1,1,1,
    0,0,0,0,1,1,1,1,
    3,3,3,3,2,2,2,2,
    3,3,3,3,2,2,2,2,
    3,3,3,3,2,2,2,2,
    3,3,3,3,2,2,2,2
]

ROTATE = [
    56,48,40,32,24,16, 8,0,
    57,49,41,33,25,17, 9,1,
    58,50,42,34,26,18,10,2,
    59,51,43,35,27,19,11,3,
    60,52,44,36,28,20,12,4,
    61,53,45,37,29,21,13,5,
    62,54,46,38,30,22,14,6,
    63,55,47,39,31,23,15,7
]

def row(p): return p // 8
def col(p): return p % 8

def spegla(piece):
    kol, rad = row(piece), col(piece)
    return rad * 8 + kol

def pos(x,y): return x+8*y

def pretty(piece): return "abcdefgh"[col(piece)] + str(1+row(piece))

def sqDist(a,b):
    dx = col(a) - col(b)
    dy = row(a) - row(b)
    return dx*dx + dy*dy

def onBoard(x,y): return 0 <= x < 8 and 0 <= y < 8

def mirror(wk,wr,bk):
    wk = spegla(wk)
    wr = spegla(wr)
    bk = spegla(bk)
    return [wk,wr,bk]

def rotate(wk,wr,bk):
    wk = ROTATE[wk]
    wr = ROTATE[wr]
    bk = ROTATE[bk]
    return [wk,wr,bk]

def getDMZ(wk,wr,bk):
    for i in range(TRANS[wk]):
        wk,wr,bk = rotate(wk,wr,bk)
    if col(wk) < row(wk): wk,wr,bk = mirror(wk,wr,bk)
    elif col(wk) == row(wk):
        if col(bk) < row(bk): wk,wr,bk = mirror(wk,wr,bk)
        elif col(bk) == row(bk):
            if col(wr) < row(wr): wk,wr,bk = mirror(wk,wr,bk)
    assert wk2ten[wk] < 10
    return matrix[4096 * wk2ten[wk] + 64 * wr + bk]

class Position:
    def __init__(self, wk, wr, bk):  # 64
        self.wk = wk
        self.wr = wr
        self.bk = bk
        self.result = getDMZ(wk, wr, bk)

    def nice(self): return pretty(self.wk) + ' ' + pretty(self.wr) + ' ' + pretty(self.bk)

    def state(self): return [self.nice(), self.result]

    def whiteMoves(self):
        res = []

        x0 = col(self.wk)
        y0 = row(self.wk)
        for [dx,dy] in KING_MOVES: # WK
            x = x0+dx
            y = y0+dy
            wk = pos(x,y)
            if onBoard(x,y) and wk != self.wr and sqDist(self.bk, wk) > 2:
                res.append([wk,self.wr,self.bk, getDMZ(wk,self.wr,self.bk)])

        x0 = col(self.wr)
        y0 = row(self.wr)
        for [dx,dy] in ROOK_MOVES: # WR
            x = x0+dx
            y = y0+dy
            wr = pos(x,y)
            while onBoard(x,y) and wr != self.wk and wr != self.bk:
                res.append([self.wk,wr,self.bk, getDMZ(self.wk,wr,self.bk)])
                x += dx
                y += dy
                wr = pos(x,y)

        return res

    def blackMoves(self):
        res = []
        x0 = col(self.bk)
        y0 = row(self.bk)
        for [dx,dy] in KING_MOVES: # BK
            x = x0+dx
            y = y0+dy
            bk = pos(x,y)
            if onBoard(x,y) and sqDist(self.wk, bk) > 2:
                res.append([self.wk,self.wr,bk, getDMZ(self.wk,self.wr,bk)])
        return res

for ix in range(n):
    i = wk2ten[WK[ix]]
    j = WR[ix]
    k = BK[ix]
    index = 4096 * i + 64 * j + k
    matrix[index] = result[ix]

def ass(a, b):
    if a != b:
        print('Failed:', b, a)
        assert a == b

ass(TRANS[10], 0)
ass(TRANS[ 7], 1)
ass(TRANS[45], 2)
ass(TRANS[33], 3)

ass(ROTATE[27],35)
ass(ROTATE[35],36)
ass(ROTATE[36],28)
ass(ROTATE[28],27)

ass(Position( 0, 8, 2).state(), ['a1 a2 c1','7'])
ass(Position( 0, 8,13).state(), ['a1 a2 f2','d'])
ass(Position( 0,16, 2).state(), ['a1 a3 c1','b'])
ass(Position( 0,17,10).state(), ['a1 b3 c2','r'])
ass(Position( 1,54,38).state(), ['b1 g7 g5','g'])
ass(Position( 2, 8, 4).state(), ['c1 a2 e1','5'])
#
ass(Position( 2,16, 0).state(), ['c1 a3 a1', '0'])
ass(Position( 2,17, 0).state(), ['c1 b3 a1', '2'])
ass(Position( 2,18, 8).state(), ['c1 c3 a2', '1'])
ass(Position( 2,25, 0).state(), ['c1 b4 a1', '3'])
ass(Position( 3,45,42).state(), ['d1 f6 c6', 'f'])
ass(Position( 3,54,44).state(), ['d1 g7 e6', 'f'])
#
ass(Position( 5,39,56).state(), ['f1 h5 a8','d'])
ass(Position( 9,27, 7).state(), ['b2 d4 h1','9'])
ass(Position(10,33, 8).state(), ['c2 b5 a2','4'])
ass(Position(13,17,10).state(), ['f2 b3 c2', 'r'])
ass(Position(17,32, 2).state(), ['b3 a5 c1', 'c'])
ass(Position(24,54,37).state(), ['a4 g7 f5', 'f'])
ass(Position(29,17,10).state(), ['f4 b3 c2', 'r'])
ass(Position(36,17,46).state(), ['e5 b3 g6', '8'])
ass(Position(42,53,13).state(), ['c6 f7 f2', 'd'])
ass(Position(42,53,60).state(), ['c6 f7 e8', 'r'])
ass(Position(49,17,10).state(), ['b7 b3 c2', 'r'])
ass(Position(49,17,46).state(), ['b7 b3 g6', 'd'])
ass(Position(60,17,10).state(), ['e8 b3 c2', 'r'])

ass(Position( 3,5,19).state(), ['d1 f1 d3', 'f'])   # RM
print(Position( 3,5,19).whiteMoves())