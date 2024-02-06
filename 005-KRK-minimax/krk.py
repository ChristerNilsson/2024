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

def stable(board,letters,squares): return not board.is_check()

def createJSON(letters,N=100, antal=10000):
    start = time.time_ns()
    n = len(letters)
    resultat = {}
    pieces = []
    for letter in letters:
        index = "pnbrqkPNBRQK".index(letter)
        pieces.append(chess.Piece(index % 6 + 1, index >= 6))

    board = chess.Board()
    for i in range(antal):
        squares = [random.choice(chess.SQUARES) for i in range(n)]
        if len(set(squares)) != n: continue
        square_names = [chess.square_name(sq) for sq in squares]

        board.clear()
        for i in range(n):
            board.set_piece_at(squares[i], pieces[i])

        if not stable(board,letters,squares): continue

        if board.is_valid():
            halvdrag = tablebase.probe_dtz(board)
            if halvdrag not in resultat: resultat[halvdrag] = []
            resultat[halvdrag].append("".join(square_names))

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

    print(letters, antal, (time.time_ns()-start)/10**6)

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


n = 200000 # antal försök
# data = createJSON("KRk",100,n)
# data = createJSON("KQk",100,n)
# data = createJSON("KQkr",100,n)
# data = createJSON("KBNk",100,n)
data = createJSON("KBBk",100,n)
# data = createJSON("KNNNk",100,n)

#data = json.load(open("krk.json"))
#play()

