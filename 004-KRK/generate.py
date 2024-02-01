import time
import chess.syzygy

# DRAW = -98

# Detta program hämtar utvärderingar från syzygy-databasen
#   (.csv-filen innehöll felaktigheter)
#   Filerna måste finnas i katalogen syzygy.
# Tillvägagångssätt (utförs både för vit och svart) :
#   1. Skapa alla möjliga drag med vit kung i åttondelen.
#     dvs a1 b2 b2 c1 c2 c3 d1 d2 d3 d4. Detta sker via rotationer och spegling i diagonalen.
#     vit kung måste stå på någon av dessa tio rutor.
#     Om vit kung står på diagonalen, får svart kung inte stå i nordväst.
#     Om både vit och svart kung står på diagonalen får tornet inte stå i nordväst
#   2. Fråga syzygy efter utvärdering
#   3. Spara till åttondelen
#   4. Spara allt till filerna KRKw.txt och KRKb.txt
#   Samma position kan förekomma i båda filerna.
#     T ex är Ka1 Rc2 Kd1 remi i KRKb men 13 ply från matt i KRKw.
# Tolkning
#   White: Antal ply till matt (1 3 .. 31)
#   Black:
#      0 = Remi
#     -1 = Matt
#     -2 -4 .. -32 Antal ply till matt
# Filstorlek
# White: 27352 rader
# Black: 34968 rader
# .csv:  28056 rader

matrix = []

def ass(a, b):
    if a != b:
        print('Failed:')
        print(b)
        print(a)
        assert a == b

def reverseIndex(index):
    k = index % 64
    index //= 64
    j = index % 64
    index //= 64
    i = index
    return [i,j,k]

def row(p): return p // 8
def col(p): return p % 8
def pretty(piece): return "abcdefgh"[col(piece)] + "12345678"[row(piece)]

def sqDist(a,b):
    dx = col(a) - col(b)
    dy = row(a) - row(b)
    return dx*dx + dy*dy

def fen_from_board(brd,color):
    res = ""
    brd = brd[56:64] + brd[48:56] + brd[40:48] + brd[32:40] + brd[24:32] + brd[16:24] + brd[8:16] + brd[0:8]
    n = 0 # räknar tomma rutor
    for i in range(64):
        sq = brd[i]
        if sq == ".":
            n += 1
        else:
            if n != 0:
                res += str(n)
                n = 0
            res += sq
        if i % 8 == 7:
            if n != 0:
                res += str(n)
                n = 0
            if res.count("/") < 7: res += "/"
    return res + f" {color} - - 0 1"

def setPiece(piece,index):
    matrix[index] = piece

def getFen(wk,wr,bk,color):
    global matrix
    matrix = ["."] * 64
    setPiece("K",wk)
    setPiece("R",wr)
    setPiece("k",bk)
    return fen_from_board(matrix,color)
ass(getFen( 0,18,36,'w'), "8/8/8/4k3/8/2R5/8/K7 w - - 0 1")
ass(getFen( 2,18, 8,'w'), "8/8/8/8/8/2R5/k7/2K5 w - - 0 1")
ass(getFen( 0, 2, 4,'w'), "8/8/8/8/8/8/8/K1R1k3 w - - 0 1")
ass(getFen(57,59,61,'w'), "1K1R1k2/8/8/8/8/8/8/8 w - - 0 1")

def makeFile(color):
    with chess.syzygy.open_tablebase("syzygy") as tablebase:
        res = []
        for wk in range(64): # [0, 1, 2, 3, 9, 10, 11, 18, 19, 27]:
            for wr in range(64):
                if wk == wr: continue
                for bk in range(64):
                    if sqDist(wk,bk) <= 2: continue
                    if wr == bk: continue
                    fen = getFen(wk,wr,bk,color)
                    board = chess.Board(fen)
                    if board.is_valid():
                        try:
                            score = tablebase.probe_dtz(board)
                            # if score == 0: score = DRAW
                            if score >= 0:
                                if score < 10: score = "0" + str(score)
                            else:
                                score = -score
                                if score < 10:
                                    score = "-0" + str(score)
                                else:
                                    score = '-' + str(score)
                            res.append(f"{score} {pretty(wk)} {pretty(wr)} {pretty(bk)}")
                        finally:
                            pass
        res.sort()
    with open("KRK" + color + ".txt",'w') as f:
        f.write("\n".join(res))

start = time.time_ns()
print("Detta tar cirka 340 (52) sekunder")
makeFile('w')
makeFile('b')
print((time.time_ns() - start)/10**6)
