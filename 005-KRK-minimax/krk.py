import json
import random
import time
import chess.syzygy

TRIANGLE = [0,1,2,3,9,10,11,18,19,27]
N = 100000

tablebase = chess.syzygy.open_tablebase("syzygy")
data = None
board = chess.Board()

def ass(a, b):
    if a != b:
        print('Failed:')
        print('  ',a)
        print('  ',b)
        assert a == b

def ints(n): return list(i for i in range(64) if (n & (1 << i)) != 0)
ass([0,3,4,5],list(ints(57)))
ass([1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23, 24, 26, 28, 30, 33, 35, 37, 39, 40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62],ints(chess.BB_LIGHT_SQUARES))

def stable(board,letters,squares):
    if board.is_check() or board.is_game_over(): return False

def sqdist(i,j):
    a = i % 8
    b = i // 8
    c = j % 8
    d = j // 8
    dx = a-c
    dy = b-d
    return dx * dx + dy * dy


def printToFile(letters,resultat):
    result = {}
    keys = resultat.keys()
    keys = sorted(keys)
    for key in keys:
        problems = resultat[key]
        result[key] = " ".join(problems)
    with open(f"json/{letters}_{N}.json", 'w') as g:
        g.write(json.dumps(result).replace('", "','",\n"'))
    return result


# def createQ(letters):
#     resultat = {}
#     for wk in TRIANGLE:
#         for bk in range(64):
#             if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
#             print(letters,wk,bk)
#             for wq in range(64): uppdatera(resultat,[wk,bk,wq],letters)
#     return printToFile(letters,resultat)


# def createR(letters):
#     resultat = {}
#     for wk in TRIANGLE:
#         for bk in range(64):
#             if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
#             print(letters,wk,bk)
#             for wr in range(64): uppdatera(resultat, [wk,bk,wr], letters)
#     return printToFile(letters, resultat)

def sample(pieces): # t ex [range(64), range(64)] => [47,18]
    return [random.choice(piece) for piece in pieces]


def uppdatera(letters, resultat, squares):
    letters = "Kk" + letters
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    square_names = [chess.square_name(sq) for sq in squares]
    board.clear()
    for m in range(len(letters)):
        board.set_piece_at(squares[m], pieces[m])
    board.turn = chess.WHITE

    if board.is_valid():
        halvdrag = tablebase.probe_dtz(board)
        if halvdrag <= 0: return
        heldrag = (halvdrag+2) // 2
        if heldrag not in resultat: resultat[heldrag] = []
        if len(resultat[heldrag]) > 100: return
        resultat[heldrag].append("".join(square_names))

def getRandom(letters,pieces): # t ex "Qr", [range(64),range(64)]
    start = time.time_ns()
    n = 2 + len(letters)
    resultat = {}
    for i in range(N):
        s = sample([TRIANGLE,range(64)] + pieces)
        if sqdist(s[0], s[1]) <= 2: continue  # Kungarna måste hålla avstånd
        if len(set(s)) != n: continue   # unika rutor
        uppdatera(letters, resultat, s)
    keys = list(resultat.keys())
    keys.sort()
    print(letters, (time.time_ns()-start)/10**9,keys)
    return resultat

def randomR(letters): printToFile(letters, getRandom(letters,[range(64)]))
def randomQ(letters): printToFile(letters, getRandom(letters,[range(64)]))
def randomQR(letters): printToFile(letters, getRandom(letters,[range(64),range(64)]))
def randomBB(letters): printToFile(letters, getRandom(letters,[ints(chess.BB_DARK_SQUARES), ints(chess.BB_LIGHT_SQUARES)]))
def randomBN(letters): printToFile(letters, getRandom(letters,[ints(chess.BB_DARK_SQUARES),range(64)]))
def randomNNN(letters): printToFile(letters, getRandom(letters,[range(64),range(64),range(64)]))

# def createQR(letters):
#     resultat = {}
#     for wk in TRIANGLE:
#         for bk in range(64):
#             if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
#             print(letters,wk, bk)
#             for wq in range(64):
#                 for br in range(64): uppdatera(resultat, [wk,bk,wq,br], letters)
#     return printToFile(letters, resultat)
#
# def createBB(letters):
#     resultat = {}
#     for wk in TRIANGLE:
#         for bk in [0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27]:
#             if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
#             print(letters,wk,bk)
#             for b0 in ints(chess.BB_LIGHT_SQUARES):
#                 for b1 in ints(chess.BB_DARK_SQUARES): uppdatera(resultat, [wk, bk, b0, b1], letters)
#     return printToFile(letters, resultat)
#
#
# def createBN(letters):
#     resultat = {}
#     for wk in TRIANGLE:
#         for bk in range(64):
#             print(letters,wk,bk)
#             if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
#             for wb in ints(chess.BB_DARK_SQUARES):
#                 for wn in range(64): uppdatera(resultat, [wk, bk, wb, wn], letters)
#     return printToFile(letters, resultat)
#
#
# def createNNN(letters):
#     resultat = {}
#     #EDGE3 = [0,1,2,3,4,5,6,7,8,16,24,32,40,48,56,57,58,59,60,61,62,63,55,47,39,31,23,15]
#     for wk in TRIANGLE:
#         for bk in range(64): #[8,16,24,32,40,48,56,57,58,59,60,61,62,63,55,47,39,31,23,15]: #EDGE3:
#             print(letters,wk, bk)
#             if sqdist(wk,bk) <= 2: continue
#             for n0 in range(64):
#                 for n1 in range(n0+1,64):
#                     for n2 in range(n1+1,64): uppdatera(resultat, [wk,bk,n0,n1,n2], letters)
#     return printToFile(letters, resultat)


def loadProblem(level,board):
    problems = data[str(level)]
    problem = random.choice(problems.split(' '))
    board.clear()
    board.set_piece_at(chess.parse_square(problem[0:2]), chess.Piece(chess.KING, chess.WHITE))
    board.set_piece_at(chess.parse_square(problem[2:4]), chess.Piece(chess.ROOK, chess.WHITE))
    board.set_piece_at(chess.parse_square(problem[4:6]), chess.Piece(chess.KING, chess.BLACK))

level = 1

def showBoard(board):
    print()
    print(str(board).replace(".", "·").replace(" ", "  "))

def play():

    board = chess.Board()
    loadProblem(level, board)

    def levelDown():
        global level
        print("You lost one level")
        level -= 1
        if level == 0: level = 1
        loadProblem(level, board)
        return level

    def levelUp():
        global level
        print("You gained one level")
        level += 1
        if level == 17: level = 16
        loadProblem(level, board)


    while True:

        # White
        showBoard()
        moves = list(board.legal_moves)
        uci = 'xxxx'
        ucis = [move.uci() for move in moves]
        while True:
            uci = input(f"Level {level} White: ")
            if uci == "":
                levelDown()
                continue
            if uci in ucis:
                break
            else:
                print("Enter one of " + " ".join(ucis))
        board.push(chess.Move.from_uci(uci))

        # Black
        showBoard(board)
        print("Black")
        moves = list(board.legal_moves)
        if len(moves) == 0:
            levelUp()
        else:
            positions = []
            for move in moves:
                board.push(move)
                positions.append([tablebase.probe_dtz(board),move])
                board.pop()
            positions.sort()
            if positions[0][0] == 0: # Draw
                levelDown()
                continue
            # print("Score:",positions[0][0])
            board.push(positions[0][1])

# start = time.time_ns()

print("N =",N)

data = randomQ("Q")
data = randomR("R")
data = randomQR("Qr")

data = randomBB("BB")
data = randomBN("BN")
data = randomNNN("NNN")

# print((time.time_ns()-start)/10**6)

#data = json.load(open("krk.json"))
#play()

