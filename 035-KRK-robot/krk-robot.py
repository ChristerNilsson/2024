import random
EMPTY = '.'
dump = print

def manhattan(p,q): # Square,Square
    dx = abs(p.x - q.x)
    dy = abs(p.y - q.y)
    return dx + dy

def pack(x,y): return 8 * y + x

def moveHor(bk,wk,wr):
    if bk.x == 0: return 1
    if bk.x >= 6: return bk.x-1
    if bk.x+1 == wk.x: return bk.x-1
    return bk.x+1

def moveRookHor(wr):
    if wr.x <= 3: return 7
    return 0

def tempodrag(wr):
    if wr.x <= 3: return wr.x+1
    return wr.x-1

class Square:
    def __init__(_,x,y):
        _.x = x
        _.y = y
    def index(_):
        res = pack(_.x,_.y)
        return res

def sq(square): return "abcdefgh"[square.x] + "12345678"[7 - square.y]

class ChessGame:
    def __init__(_,position):
        _.board = [EMPTY] * 64

        _.wk = Square("abcdefgh".index(position[0]), 7-"12345678".index(position[1]))
        _.wr = Square("abcdefgh".index(position[2]), 7-"12345678".index(position[3]))
        _.bk = Square("abcdefgh".index(position[4]), 7-"12345678".index(position[5]))

        _.board[_.wk.index()] = 'K'
        _.board[_.wr.index()] = 'R'
        _.board[_.bk.index()] = 'k'

        _.antal = 1

    # def position(_): return "abcdefgh"[_.wk.x] + "12345678"[7-_.wk.y] + "abcdefgh"[_.wr.x] + "12345678"[7-_.wr.y] + "abcdefgh"[_.bk.x] + "12345678"[7-_.bk.y]
    def position(_): return sq(_.wk) + sq(_.wr) + sq(_.bk)

    def display_board(_):
        s = ''
        for row in range(8):
            t = ''
            for col in range(8):
                t += '   ' + _.board[pack(col,row)]
            s += t + "\n"
        return s

    def move_piece(_, piece, x,y):
        """Flytta en pjäs till en ny position"""
        letter = _.board[piece.index()]
        _.board[piece.index()] = EMPTY
        piece.x = x
        piece.y = y
        _.board[piece.index()] = letter

    def is_checkmate(_):
        # Om svarta kungen är vid brädets övre kant och instängd av vit kung och torn, är det schackmatt
        if _.bk.y == 0 and _.wk.y == 2 and (abs(_.bk.x - _.wk.x) <= 1):
            if _.bk.y == _.wr.y or _.bk.x == _.wr.x:  return True
        return False

    def move_black_king(_):
        """Grundläggande logik för att flytta svarta kungen bort från centrum och mot kanten"""
        # Flytta mot kanten, grundlogik för att simulera flykten
        x = _.bk.x
        y = _.bk.y
        if _.bk.y == 0:
            x = moveHor(_.bk,_.wk,_.wr)
        elif _.bk.y < 7 and _.bk.y + 1 != _.wr.y and abs(_.bk.y - _.wk.y) > 2:
            y += 1
        elif _.bk.y + 1 != _.wr.y:
            y -= 1
            if _.bk.x < _.wr.x: x += 1
            else: x -= 1
        else:
            x = moveHor(_.bk,_.wk,_.wr)

        _.move_piece(_.bk, x,y)

    def apply_torres_algorithm(_):
        """Implementera Torres' slutspelsalgoritm baserat på de specificerade reglerna"""

        # Kontrollera om kungen och tornet är för nära varandra
        if manhattan(_.bk,_.wr) <= 2:
            # if _.wr.x in [0, 7]:
            #     dump("B Om tornet redan är på a- eller h-filen, gör inget")
            # else:
            dump("C Flytta tornet i säkerhet")
            x = moveRookHor(_.wr)
            y = _.wr.y
            _.move_piece(_.wr, x, y)
        else:
            dy = abs(_.bk.y - _.wr.y)
            if dy > 1 and abs(_.bk.x - _.wr.x) > 1:
                dump("E Tornet flyttas vertikalt mot svarta kungen")
                x = _.wr.x
                y = _.wr.y - dy+1 if _.wr.y > _.bk.y else _.wr.y + dy
                _.move_piece(_.wr, x,y)
            elif abs(_.bk.y - _.wk.y) > 2:
                dump("F Vita kungen flyttas vertikalt mot svarta kungen")
                x = _.wk.x
                y = (_.wk.y - 1 if _.wk.y > _.bk.y else _.wk.y + 1)
                _.move_piece(_.wk, x,y)
            elif abs(_.wk.y - _.bk.y) == 2:
                mh = manhattan(_.wk, _.bk)
                if _.wk.x == _.bk.x:
                    dump("G Avancera med tornet")
                    x = _.wr.x
                    y = _.wr.y - 1
                    _.move_piece(_.wr, x, y)
                elif mh == 3:
                    dump("H Tempodrag")
                    x = tempodrag(_.wr)
                    y = _.wr.y
                    _.move_piece(_.wr, x,y)
                else:
                    dump("I Flytta vita kungen horisontellt mot svarta kungen")
                    x = _.wk.x - 1 if _.wk.x > _.bk.x else _.wk.x + 1
                    y = _.wk.y
                    _.move_piece(_.wk, x,y)
            else:
                dump("J Tornet flyttas vertikalt mot svarta kungen")
                x = _.wr.x
                y = _.wr.y - 1 if _.wr.y > _.bk.y else _.wr.y + 1
                _.move_piece(_.wr, x,y)

    def play(_):

        while not _.is_checkmate():
            print(_.display_board())
            if _.antal == 100: break
            dump('Drag:',_.antal)
            _.antal += 1
            _.apply_torres_algorithm()

            if _.is_checkmate(): break
            _.move_black_king()

        print(_.display_board())
        print("Schackmatt!")

def slump():
    arr = []
    for col in "abcdefgh":
        for row in "12345678":
            arr.append(col+row)
    return random.choice(arr) + random.choice(arr) + random.choice(arr)

# while True:
#     position = slump()
#     if position[1] < position[3] < position[5]:
#         game = ChessGame(position) # KRk
#         game.play()
#         if game.antal >= 53:
#             print(position,game.antal)

# e7c1d5 efter rotation

#  29 drag
# d2f3h4 37 drag
#game = ChessGame("h1d2g3") # 52 drag
#game = ChessGame("a1e2b3") # 49 drag
#game = ChessGame("a1b2c3") # 48 drag
#game = ChessGame("h1a3b4") # 41 drag
#game = ChessGame("e1d3f5") # 29 drag
# game = ChessGame("e1d3e8") #
#game = ChessGame("e1d3e5") #
#game = ChessGame("b4a5h7") # 15 drag
#game = ChessGame("c2d6a7") # 14 drag
#game = ChessGame("d1h1d8") # 11 drag

# game.play()

def check(a,b,description):
    game = ChessGame(a)
    before = game.display_board()
    game.apply_torres_algorithm()
    after  = game.display_board()
    b = game.position()
    if a==b: return
    print('assert failure:',description)
    print(before)
    print(after)

check('e1d3e8','e1d6e8',"Tornet bör avancera")
