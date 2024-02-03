import random
import time

ALFABETA = False

CMD = [ # Center Manhattan Distance
    6, 5, 4, 3, 3, 4, 5, 6,
    5, 4, 3, 2, 2, 3, 4, 5,
    4, 3, 2, 1, 1, 2, 3, 4,
    3, 2, 1, 0, 0, 1, 2, 3,
    3, 2, 1, 0, 0, 1, 2, 3,
    4, 3, 2, 1, 1, 2, 3, 4,
    5, 4, 3, 2, 2, 3, 4, 5,
    6, 5, 4, 3, 3, 4, 5, 6
]

WK = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 7, 0, 0, 7, 0, 0,
    0, 7, 6, 6, 6, 6, 7, 0,
    0, 0, 6, 0, 0, 6, 0, 0,
    0, 0, 6, 0, 0, 6, 0, 0,
    0, 7, 6, 6, 6, 6, 7, 0,
    0, 0, 7, 0, 0, 7, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]

WR = [
    7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7,
]

XYZ = [
    7, 6, 5, 4, 4, 5, 6, 7,
    6, 5, 3, 2, 2, 3, 5, 6,
    5, 3, 0, 0, 0, 0, 3, 5,
    4, 2, 0, 0, 0, 0, 2, 4,
    4, 2, 0, 0, 0, 0, 2, 4,
    5, 3, 0, 0, 0, 0, 3, 5,
    6, 5, 3, 2, 2, 3, 5, 6,
    7, 6, 5, 4, 4, 5, 6, 7,
]

#ALFABET = "0123456789abcdefghijklmnopqrstuvwxyz"
#DRAW = '|'
#MATE = '1'

def ass(a, b):
    if a != b:
        print('Failed:')
        print('  ',a)
        print('  ',b)
        assert a == b

# def getData(filename):
#     with open(filename) as f:
#         return f.read()

# blackData = getData("KRKb.txt")
# whiteData = getData("KRKw.txt")
# ass(len(blackData), 262144)
# ass(len(whiteData), 262144)

ROOK_MOVES = [[-1, 0], [0, -1], [0, 1], [1, 0]]
KING_MOVES = [[-1, -1], [-1, 0], [-1, 1],  [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def row(p): return p // 8
def col(p): return p % 8
def pos(x,y): return x+8*y
def pretty(piece): return "abcdefgh"[col(piece)] + str(1+row(piece))
def onBoard(x,y): return 0 <= x < 8 and 0 <= y < 8
# def getWhiteScore(index): return whiteData[index]
# def getBlackScore(index): return blackData[index]
# def forwardIndex(wk,wr,bk): return 64 * 64 * wk + 64 * wr + bk

def getIndex(s):
    col = "abcdefgh".index(s[0])
    row = "12345678".index(s[1])
    return 8 * row + col

# def reverseIndex(index):
#     k = index % 64
#     index //= 64
#     j = index % 64
#     index //= 64
#     i = index
#     return [i,j,k]

illegalSquaresBlack = []
illegalSquaresWhite = []

def sqDist(a,b):
    dx = col(a) - col(b)
    dy = row(a) - row(b)
    return dx*dx + dy*dy

def minDist(a,b):
    dx = abs(col(a) - col(b))
    dy = abs(row(a) - row(b))
    return min(dx,dy)

def maxDist(a,b): # chebyshev
    dx = abs(col(a) - col(b))
    dy = abs(row(a) - row(b))
    return max(dx,dy)

def manhattan(a,b):
    dx = abs(col(a) - col(b))
    dy = abs(row(a) - row(b))
    return dx+dy

# def getRandomPosition(n):
#     ass(n % 2, 1)
#     letter = ALFABET[n]
#     indexes = [i for i in range(len(whiteData)) if whiteData[i] == letter]
#
#     i = random.choice(indexes)
#     #i = 146745
#
#     [wk,wr,bk] = reverseIndex(i)
#     print('Random position:',i)
#     return Position(wk,wr,bk)

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

def onBoard(x,y): return 0 <= x <= 7 and 0 <= y <= 7

class Position:
    def __init__(self, wk, wr, bk):  # 64
        self.set(wk,wr,bk)

    def __eq__(self,p):
        return self.wk == p.wk and self.wr == p.wr and self.bk == p.bk

    def __str__(self):
        return f"{self.wk} {self.wr} {self.bk}"

    def set(self,wk,wr,bk):
        self.wk = wk
        self.wr = wr
        self.bk = bk
        # self.index = forwardIndex(wk,wr,bk) # används för att slå i whiteData och blackData

    # def nice(self): return pretty(self.wk) + ' ' + pretty(self.wr) + ' ' + pretty(self.bk)
    def nicestWhite(self): return "K"+pretty(self.wk) + ' R' + pretty(self.wr) + ' K' + pretty(self.bk) # + ' (' + str(self.whiteScore()) + ')'
    def nicestBlack(self): return "K"+pretty(self.wk) + ' R' + pretty(self.wr) + ' K' + pretty(self.bk) # + ' (' + str(self.blackScore()) + ')'
    # def whiteScore(self): return getWhiteScore(self.index)
    # def blackScore(self): return getBlackScore(self.index)

    def whiteMoves(self):
        res = []
        illegalSquares = illegalSquaresWhite(self.wk,self.wr,self.bk)

        x0 = col(self.wk)
        y0 = row(self.wk)
        for [dx,dy] in KING_MOVES: # WK
            x,y = x0+dx, y0+dy
            wk = pos(x,y)
            if onBoard(x,y) and wk != self.wr and wk not in illegalSquares:
                #index = forwardIndex(wk, self.wr, self.bk)
                res.append(Position(wk,self.wr,self.bk)) # , getBlackScore(index)])

        x0 = col(self.wr)
        y0 = row(self.wr)
        for [dx,dy] in ROOK_MOVES: # WR
            x,y = x0+dx, y0+dy
            wr = pos(x,y)
            while onBoard(x,y) and wr != self.wk and wr != self.bk:
                #index = forwardIndex(self.wk, wr, self.bk)
                res.append(Position(self.wk,wr,self.bk)) #, getBlackScore(index)])
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
                #index = forwardIndex(self.wk, self.wr, bk)
                # index = 64 * 64 * self.wk + 64 * self.wr + bk
                res.append(Position(self.wk,self.wr,bk))
        return res


    def realEstate(self,x,y,illegal,visited):
        if 8*y+x in illegal: return
        if (x,y) in visited: return
        if not onBoard(x,y): return
        visited[(x,y)] = True
        for [dx,dy] in ROOK_MOVES:
            self.realEstate(x+dx, y+dy, illegal, visited)

    def evaluation(self, player):
        illegal = illegalSquaresBlack(self.wk,self.wr,self.bk)
        key = (self.wk,self.wr,self.bk)
        if key not in hash:
            visited = {} # hash halverar söktiden
            self.realEstate(col(self.bk), row(self.bk), illegal, visited)
            hash[key] = len(visited)

        # res += -sqDist(self.wk, self.bk)  # WB
        # res += abs(1 - minDist(self.wk, self.wr))  # WR
        # res += abs(1 - minDist(self.wr, self.bk))  # RB

        res = - 2 * hash[key] + WK[self.wk] + WR[self.wr] - CMD[self.bk] - 3 * manhattan(self.wk,self.bk)
        #res = - hash[key]

        return res if player == 0 else -res


# position = getRandomPosition(31) # odd number of moves

# def showWhiteMoves(moves): # Ka6 (e) Ra3 (f)
#     result = []
#     for move in moves:
#         if move[0] != position.wk: result.append(f"K{pretty(move[0])}.{move[3]}")
#         if move[1] != position.wr: result.append(f"R{pretty(move[1])}.{move[3]}")
#     return ' '.join(result)

# def showBlackMoves(moves): return ' '.join([f"K{pretty(move[2])}.{move[3]}" for move in moves])

# def showSingleMove(a,b):
#     res = ""
#     if a[0] != b[0]: res += "K" + pretty(a[0])
#     if a[1] != b[1]: res += "R" + pretty(a[1])
#     if a[2] != b[2]: res += "K" + pretty(a[2])
#     return "   " if res == "" else res

def computerBoth(position,level):  # datorn gör första draget som vit
    lastMove = [position.wk,position.wr,position.bk]
    move = lastMove
    result = []
    # print('       ',position.nicestWhite())
    for i in range(30):

        # print('   ', showSingleMove(move,lastMove), '|', position.nicestWhite())
        print(i,'   ', position.nicestWhite())
        result.append(position.nicestWhite())

        lastMove = move
        move = alphaBeta(position,level,0)
        # whiteMoves = position.whiteMoves()
        # whiteMoves.sort(key=lambda a: a[3])

        # lastMove = move
        # move = whiteMoves[0]
        position.set(move.wk, move.wr, move.bk)

        print( position.nicestBlack())
        result.append(position.nicestBlack())
        # blackMoves = position.blackMoves()
        # blackMoves.sort(key=lambda a: a[3])

        # if len(blackMoves) == 0: break
        lastMove = move
        # move = blackMoves[-1]
        move = alphaBeta(position,level,1)
        position.set(move.wk, move.wr, move.bk)
        # position.set(move[0], move[1], move[2])
    return result

# computerBoth()

# def makeAllMoves(house, player, positions, actions=""): # offset = 0 or 7
#     offset = [0,7][player]
#     for i in range(offset,offset+6):
#         if house[i] == 0: continue
#         house1 = house.copy()
#         if Relocation(house1,i):
#             if house1[offset:offset+6] == [0, 0, 0, 0, 0, 0]:
#                 positions.append([house1, actions + LITTERA[i], house1[6] - house1[13]])
#             else:
#                 makeAllMoves(house1, player, positions, actions + LITTERA[i])
#         else:
#             positions.append([house1,actions+LITTERA[i], house1[6] - house1[13]])
#     return positions

def getMoves(position, player):
    return position.whiteMoves() if player == 0 else position.blackMoves()

def alphaBeta(position, depthMax, player):
    return maxAlphaBeta(position, depthMax, 0, -999, 999, player)

def maxAlphaBeta(position, depthMax, depth, alpha, beta, player):
    opponent = 1 - player
    moves = getMoves(position, player)
    if depth >= depthMax or len(moves) == 0:
         return position.evaluation(player)
    else:
        top = None
        maxEval = -999
        for tempPos in moves:
            eval = minAlphaBeta(tempPos, depthMax, depth+1, alpha, beta, opponent)
            if ALFABETA:
                if alpha < eval:
                    alpha = eval
                    top = tempPos
                if beta <= alpha: break
            else:
                if eval > maxEval:
                    maxEval = eval
                    top = tempPos
        if depth == 0: return top
        return alpha if ALFABETA else maxEval


def minAlphaBeta(position, depthMax, depth, alpha, beta, player):
    opponent = 1 - player
    moves = getMoves(position, player)
    if depth >= depthMax or len(moves) == 0:
         return position.evaluation(player)
    else:
        minEval = 999
        for tempPos in moves:
            eval = maxAlphaBeta(tempPos, depthMax, depth + 1, alpha, beta, opponent)
            if ALFABETA:
                if beta > eval: beta = eval
                if beta <= alpha: break
            else:
                minEval = min(minEval, eval)
        return beta if ALFABETA else minEval

# ass(alphaBeta(Position(4,7,60),2,0), Position(4,55,60))
# ass(alphaBeta(Position(4,55,60),4,1), Position(4,55,59))
# ass(alphaBeta(Position(4,55,59),4,0), Position(11,55,59))
# ass(alphaBeta(Position(11,55,59),4,1), Position(11,55,58))
# ass(alphaBeta(Position(11,55,58),4,0), Position(18,55,58))
# ass(alphaBeta(Position(18,55,58),4,0), Position(26,55,58))
#ass(alphaBeta(Position(26,55,58),4,0), Position(34,55,58))
#ass(alphaBeta(Position(34,55,58),4,0), Position(42,55,58))
#ass(alphaBeta(Position(42,55,58),4,0), Position(42,63,58))
#ass(alphaBeta(Position(42,63,58),4,0), Position(42,59,58))
#ass(alphaBeta(Position(42,59,58),4,0), Position(42,60,58))

position = Position(4,7,60)
#position = Position(15,7,28)
# position = getRandomPosition(31) # odd number of moves

start = time.time_ns()
hash = {}

problems = [[15, 22, 36],[7, 13, 35],[0, 46, 36],[63, 40, 37],[7, 16, 34],[62, 21, 44],[0, 23, 35],[0, 41, 36],[63, 0, 28],[56, 15, 29]] # 31 ply
for [wk,wr,bk] in problems:
    position = Position(wk,wr,bk)
    solution = computerBoth(position,4)
    print(len(solution))
# print(len(hash))
print((time.time_ns() - start)/10**6)
# print(z.wk,z.wr,z.bk)