import random

EMPTY = '.'

dump = print

def manhattan(p,q):
    px,py = unpack(p)
    qx,qy = unpack(q)
    dx = abs(px - qx)
    dy = abs(py - qy)
    return dx+dy

def unpack(index): return index//8,index%8
def pack(x,y): return 8 * x + y

def moveHor(bky,wky,wry):
    if bky == 0: return 1
    if bky >= 6: return bky-1
    if bky+1 == wky: return bky-1
    return bky+1

def moveRookHor(wry):
    if wry <= 3: return 7
    return 0

def tempodrag(wry):
    if wry <= 3: return wry+1
    return wry-1

class ChessGame:
    def __init__(_,position):
        _.board = [EMPTY] * 64
        _.wk = pack(7-"12345678".index(position[1]), "abcdefgh".index(position[0]))
        _.wr = pack(7-"12345678".index(position[3]), "abcdefgh".index(position[2]))
        _.bk = pack(7-"12345678".index(position[5]), "abcdefgh".index(position[4]))

        _.board[_.wk] = 'K'
        _.board[_.wr] = 'R'
        _.board[_.bk] = 'k'
        _.antal = 1

    def display_board(_):
        s = ''
        for row in range(8):
            t = ''
            for col in range(8):
                t += '   ' + _.board[pack(row,col)]
            s += t + "\n"
        print(s)

    def move_piece(_, piece, new_position):
        """Flytta en pjäs till en ny position"""
        if piece == 'K':
            _.board[_.wk] = EMPTY
            _.wk = new_position
            _.board[_.wk] = 'K'
        elif piece == 'R':
            _.board[_.wr] = EMPTY
            _.wr = new_position
            _.board[_.wr] = 'R'
        elif piece == 'k':
            _.board[_.bk] = EMPTY
            _.bk = new_position
            _.board[_.bk] = 'k'

    def is_checkmate(_):
        """Kontrollera om svart kung är schackmatt"""
        bkx, bky = unpack(_.bk)
        wkx, wky = unpack(_.wk)
        wrx, wry = unpack(_.wr)

        # Om svarta kungen är vid brädets övre kant och instängd av vit kung och torn, är det schackmatt
        if bkx == 0 and wkx == 2 and (abs(bky - wky) <= 1):
            if bkx == wrx or bky == wry:  return True
        return False

    def move_black_king(_):
        """Grundläggande logik för att flytta svarta kungen bort från centrum och mot kanten"""
        bkx, bky = unpack(_.bk)
        wkx, wky = unpack(_.wk)
        wrx, wry = unpack(_.wr)

        # Flytta mot kanten, grundlogik för att simulera flykten
        if bkx == 0:
            bky = moveHor(bky,wky,wry)
        elif bkx < 7 and bkx + 1 != wrx and abs(bkx-wkx) > 2:
            bkx += 1
        elif bkx + 1 != wrx:
            bkx -= 1
            if bky<wry: bky += 1
            else: bky -= 1
        else:
            bky = moveHor(bky,wky,wry)

        _.move_piece('k', pack(bkx, bky))

    def apply_torres_algorithm(_):
        """Implementera Torres' slutspelsalgoritm baserat på de specificerade reglerna"""
        bkx, bky = unpack(_.bk)
        wkx, wky = unpack(_.wk)
        wrx, wry = unpack(_.wr)

        # Kontrollera om kungen och tornet är för nära varandra
        if manhattan(_.bk,_.wr) <= 2:
            if wrx in [0, 7]:
                pass
                dump("B Om tornet redan är på a- eller h-filen, gör inget")
            else:
                dump("C Flytta tornet i säkerhet")
                wry = moveRookHor(wry)
                _.move_piece('R', pack(wrx, wry))
        else:
            dx = abs(bkx - wrx)
            if dx > 1:
                dump("E Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - dx+1 if wrx > bkx else wrx + dx
                _.move_piece('R', pack(wrx, wry))
            elif abs(bkx - wkx) > 2:
                dump("F Vita kungen flyttas vertikalt mot svarta kungen")
                wkx = (wkx - 1 if wkx > bkx else wkx + 1)
                _.move_piece('K', pack(wkx, wky))
            elif abs(wkx - bkx) == 2:
                mh = manhattan(_.wk, _.bk)
                if wky == bky:
                    dump("G Avancera med tornet")
                    wrx = wrx - 1
                    _.move_piece('R', pack(wrx, wry))
                elif mh == 3:
                    dump("H Tempodrag")
                    wry = tempodrag(wry)
                    _.move_piece('R', pack(wrx, wry))
                else:
                    dump("I Flytta vita kungen horisontellt mot svarta kungen")
                    wky = wky - 1 if wky > bky else wky + 1
                    _.move_piece('K', pack(wkx, wky))
            else:
                dump("J Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - 1 if wrx > bkx else wrx + 1
                _.move_piece('R', pack(wrx, wry))

    def play(_):

        while not _.is_checkmate():
            _.display_board()
            if _.antal == 100: break
            dump('Drag:',_.antal)
            _.antal += 1
            _.apply_torres_algorithm()

            if _.is_checkmate(): break
            _.move_black_king()

        _.display_board()
        #print("Schackmatt!")

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
# a1b2c3 48 drag (32 i teorin)
# e1d3f5 29 drag
# d2f3h4 37 drag
# b4a5h7 15 drag
# c2d6a7 14 drag
game = ChessGame("h1d2g3") # 53 drag
#game = ChessGame("a1e2b3") # 49 drag

#game = ChessGame("d1h1d8") # KRk
#game = ChessGame("a1b2c3") # KRk
#game = ChessGame("h1a3b4") # KRk
game.play()
