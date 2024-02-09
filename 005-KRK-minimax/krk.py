import json
import random
import time
import chess.syzygy

tablebase = chess.syzygy.open_tablebase("syzygy")
data = None

def ass(a, b):
    if a != b:
        print('Failed:')
        print('  ',a)
        print('  ',b)
        assert a == b

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

def createJSON4(letters,N=100):
    start = time.time_ns()
    n = len(letters)
    resultat = {}
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    board = chess.Board()
    for i in [2,10,18,19]: # wk
        for j in range(64): # # wb
            print(i, j)
            for k in range(64):  # wn
                for l in [0,1,2,3, 8,9,10,11, 16,17,18,19, 24,25,26,27]: # bk
                    squares = [i,j,k,l]
                    if len(set(squares)) != n: continue
                    if sqdist(i,l) < 2: continue # Kungarna måste hålla avstånd
                    square_names = [chess.square_name(sq) for sq in squares]
                    board.clear()
                    for m in range(n):
                        board.set_piece_at(squares[m], pieces[m])

                    # if not stable(board,letters,squares): continue

                    if board.is_valid():
                        halvdrag = tablebase.probe_dtz(board)
                        if halvdrag not in resultat: resultat[halvdrag] = []
                        resultat[halvdrag].append("".join(square_names))

    # visa resultat sammanfattat. dvs len på varje nivå.
    for key in resultat.keys():
        print(key,len(resultat[key]))

    result = {}
    keys = resultat.keys()
    keys = sorted(keys)
    for key in keys:
        problems = resultat[key]
        n = len(problems)
        if n > 0:
            n = min(n, N)
            result[key] = (" ".join(random.sample(problems, n)))

    with open(f"{letters}.json", 'w') as g:
        g.write(json.dumps(result).replace('", "','",\n"'))

    print(letters, (time.time_ns()-start)/10**6)

    return result

def integers(n): return (i for i in range(64) if (n & (1 << i)) != 0)
ass([0,3,4,5],list(integers(57)))
ass([1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23, 24, 26, 28, 30, 33, 35, 37, 39, 40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62],list(integers(chess.BB_LIGHT_SQUARES)))

def createBB(letters,N=100):
    start = time.time_ns()
    n = len(letters)
    resultat = {}
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    board = chess.Board()
    for i in [2,10,18,19]: # wk
        for j in integers(chess.BB_LIGHT_SQUARES): # # wb
            print(i, j)
            for k in integers(chess.BB_DARK_SQUARES):  # wb
                for l in [0,1,2,3, 8,9,10,11, 16,17,18,19, 24,25,26,27]: # bk
                    squares = [i,j,k,l]
                    if len(set(squares)) != n: continue
                    if sqdist(i,l) < 2: continue # Kungarna måste hålla avstånd
                    square_names = [chess.square_name(sq) for sq in squares]
                    board.clear()
                    for m in range(n):
                        board.set_piece_at(squares[m], pieces[m])

                    if not stable(board,letters,squares): continue

                    if board.is_valid():
                        halvdrag = tablebase.probe_dtz(board)
                        if halvdrag == 0: continue
                        if halvdrag % 2 == 0: halvdrag += 1
                        heldrag = (halvdrag+1)//2
                        if heldrag not in resultat: resultat[heldrag] = []
                        resultat[heldrag].append("".join(square_names))

    # visa resultat sammanfattat. dvs len på varje nivå.
    for key in resultat.keys():
        print(key,len(resultat[key]))

    result = {}
    keys = resultat.keys()
    keys = sorted(keys)
    for key in keys:
        problems = resultat[key]
        n = len(problems)
        if n > 0:
            n = min(n, N)
            result[key] = (" ".join(random.sample(problems, n)))

    with open(f"json/{letters}.json", 'w') as g:
        g.write(json.dumps(result).replace('", "','",\n"'))

    print(letters, (time.time_ns()-start)/10**6)

    return result


def createBN(letters,N=100):
    start = time.time_ns()
    n = len(letters)
    resultat = {}
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    board = chess.Board()
    for i in [2,10,18,19]: # wk
        for j in integers(chess.BB_DARK_SQUARES): # # wb
            print(i, j)
            for k in range(64):  # wn
                for l in range(64): # bk
                    squares = [i,j,k,l]
                    if len(set(squares)) != n: continue
                    if sqdist(i,l) < 2: continue # Kungarna måste hålla avstånd
                    square_names = [chess.square_name(sq) for sq in squares]
                    board.clear()
                    for m in range(n):
                        board.set_piece_at(squares[m], pieces[m])

                    if not stable(board,letters,squares): continue

                    if board.is_valid():
                        halvdrag = tablebase.probe_dtz(board)
                        if halvdrag == 0: continue
                        if halvdrag % 2 == 0: halvdrag += 1
                        heldrag = (halvdrag+1)//2
                        # print('  ',halvdrag,heldrag)
                        if heldrag not in resultat: resultat[heldrag] = []
                        resultat[heldrag].append("".join(square_names))

    # visa resultat sammanfattat. dvs len på varje nivå.
    for key in resultat.keys():
        print(key,len(resultat[key]))

    result = {}
    keys = resultat.keys()
    keys = sorted(keys)
    for key in keys:
        problems = resultat[key]
        n = len(problems)
        if n > 0:
            n = min(n, N)
            result[key] = (" ".join(random.sample(problems, n)))

    with open(f"json/{letters}.json", 'w') as g:
        g.write(json.dumps(result).replace('", "','",\n"'))

    print(letters, (time.time_ns()-start)/10**6)

    return result



def createNNN(letters):
    start = time.time_ns()
    n = len(letters)
    resultat = {}
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    EDGE3 = [0,1,2,3,4,5,6,7,8,16,24,32,40,48,56,57,58,59,60,61,62,63,55,47,39,31,23,15]

    board = chess.Board()
    antal = 0
    for wk in [19,18,27]: # wk
        for bk in EDGE3: # wn
            if sqdist(wk, bk) <= 2: continue  # Kungarna måste hålla avstånd
            print(wk, bk)
            for i in range(64):
                if sqdist(i, bk) == 5: continue  # Svart kung får ej vara i schack
                for j in range(i+1,64):
                    if sqdist(j, bk) == 5: continue  # Svart kung får ej vara i schack
                    for k in range(j+1,64):
                        if sqdist(k,bk) == 5: continue # Svart kung får ej vara i schack
                        squares = [wk,bk,i,j,k]
                        if len(set(squares)) != n: continue
                        square_names = [chess.square_name(sq) for sq in squares]
                        board.clear()
                        for o in range(n):
                            board.set_piece_at(squares[o], pieces[o])

                        # if not stable(board,letters,squares): continue

                        # if board.is_valid():
                        halvdrag = tablebase.probe_dtz(board)
                        # print(halvdrag,"".join(square_names))
                        if halvdrag == 1:
                            antal += 1
                            print(wk,bk,halvdrag, "".join(square_names),antal)

                        # if halvdrag == 0:
                        #     if board.is_checkmate():
                        #         print(board,"".join(square_names))
                            if halvdrag not in resultat: resultat[halvdrag] = []
                            resultat[halvdrag].append("".join(square_names))
                        #if (len(resultat[halvdrag]) <= 5):
                        #    print(halvdrag, resultat[halvdrag])

    # visa resultat sammanfattat. dvs len på varje nivå.
    for key in resultat.keys():
        print(key,len(resultat[key]))

    result = {}
    keys = resultat.keys()
    keys = sorted(keys)
    for key in keys:
        problems = resultat[key]
        # n = len(problems)
        result[key] = (" ".join(problems))
        # if n > 0:
            # n = min(n, N)
            # result[key] = (" ".join(random.sample(problems, n)))

    with open(f"{letters}.json", 'w') as g:
        g.write(json.dumps(result).replace('", "','",\n"'))

    print(letters, (time.time_ns()-start)/10**6)

    return result



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


# n = 200000 # antal försök
# data = createJSON("KRk",100,n)
# data = createJSON("KQk",100,n)
# data = createJSON("KQkr",100,n)

#data = createBN("KBNk",100)
#data = createBB("KBBk",100)
data = createNNN("KkNNN")

#data = json.load(open("krk.json"))
#play()

