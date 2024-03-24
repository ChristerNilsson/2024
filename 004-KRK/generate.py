import time
import chess.syzygy

matrix = []

def ass(a, b):
    if a != b:
        print('Failed:')
        print(b)
        print(a)
        assert a == b

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

def setPiece(piece,index): matrix[index] = piece

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
    antal = {}
    details = []
    with chess.syzygy.open_tablebase("syzygy") as tablebase:
        undef = {'b':"-", 'w':"|"}[color]
        res = [undef] * 64 * 64 * 64
        for wk in range(64):
            for wr in range(64):
                if wk == wr: continue
                for bk in range(64):
                    if sqDist(wk,bk) <= 2: continue
                    if wr == bk: continue
                    fen = getFen(wk,wr,bk,color)
                    board = chess.Board(fen)
                    score = " " # undefined
                    if board.is_valid():
                        try:
                            score = tablebase.probe_dtz(board)
                        finally:
                            pass
                        if score == " ":
                            letter = undef
                        else:
                            letter = "|123456789abcdefghijklmnopqrstuvwxyz"[abs(score)]
                        index = 64 * 64 * wk + 64 * wr + bk
                        res[index] = letter
                        details.append(f"{pretty(wk)} {pretty(wr)} {pretty(bk)} {score} {letter}")
                        antal[letter] = antal[letter] + 1 if letter in antal else 1

    with open("KRK" + color + ".txt",'w') as f: f.write("".join(res))
    with open("KRK" + color + "_details.txt",'w') as f: f.write("\n".join(details))

    print(antal)

start = time.time_ns()
print("Detta tar cirka fem minuter")

makeFile('b')
makeFile('w')

print((time.time_ns() - start)/10**6)
