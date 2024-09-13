import random

EMPTY = '.'

dump = print

def manhattan(p,q):
    px,py = unpack(p)
    qx,qy = unpack(q)
    dx = abs(px - qx)
    dy = abs(py - qy)
    return dx+dy

def unpack(index): return (index//8,index%8)
def pack(x,y): return (8 * x + y)

def moveHor(bky,wky,wry):
    if bky==0: return 1
    if bky >= 6: return bky-1
    # if bky<wry: return bky+1
    if bky+1 == wky: return bky-1
    return bky+1

def moveRookHor(wry):
    if wry <= 3: return 7
    return 0

def tempodrag(wry):
    if wry <= 3: return wry+1
    return wry-1

class ChessGame:
    def __init__(self,position):
        self.board = [EMPTY] * 64
        self.wk = pack(7-"12345678".index(position[1]), "abcdefgh".index(position[0]))
        self.wr = pack(7-"12345678".index(position[3]), "abcdefgh".index(position[2]))
        self.bk = pack(7-"12345678".index(position[5]), "abcdefgh".index(position[4]))

        self.board[self.wk] = 'K'
        self.board[self.wr] = 'R'
        self.board[self.bk] = 'k'
        self.antal = 1

    def display_board(self):
        s = ''
        for row in range(8):
            t = ''
            for col in range(8):
                t += '   ' + self.board[pack(row,col)]
            s += t + "\n"
        print(s)

    def move_piece(self, piece, new_position):
        """Flytta en pjäs till en ny position"""
        if piece == 'K':
            self.board[self.wk] = EMPTY
            self.wk = new_position
            self.board[self.wk] = 'K'
        elif piece == 'R':
            self.board[self.wr] = EMPTY
            self.wr = new_position
            self.board[self.wr] = 'R'
        elif piece == 'k':
            self.board[self.bk] = EMPTY
            self.bk = new_position
            self.board[self.bk] = 'k'

    def is_checkmate(self):
        """Kontrollera om svart kung är schackmatt"""
        bkx, bky = unpack(self.bk)
        wkx, wky = unpack(self.wk)
        wrx, wry = unpack(self.wr)

        # Om svarta kungen är vid brädets övre kant och instängd av vit kung och torn, är det schackmatt
        if bkx == 0 and wkx == 2 and (abs(bky - wky) <= 1):
            if bkx == wrx or bky == wry:  return True
        return False

    def move_black_king(self):
        """Grundläggande logik för att flytta svarta kungen bort från centrum och mot kanten"""
        bkx, bky = unpack(self.bk)
        wkx, wky = unpack(self.wk)
        wrx, wry = unpack(self.wr)

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

        self.move_piece('k', pack(bkx, bky))

    def apply_torres_algorithm(self):
        """Implementera Torres' slutspelsalgoritm baserat på de specificerade reglerna"""
        bkx, bky = unpack(self.bk)
        wkx, wky = unpack(self.wk)
        wrx, wry = unpack(self.wr)

        # Kontrollera om kungen och tornet är för nära varandra
        if manhattan(self.bk,self.wr) <= 2:
            if wrx in [0, 7]:
                pass
                dump("B Om tornet redan är på a- eller h-filen, gör inget")
            else:
                dump("C Flytta tornet i säkerhet")
                wry = moveRookHor(wry)
                self.move_piece('R', pack(wrx, wry))
        else:
            dx = abs(bkx - wrx)
            if dx > 1:
                dump("E Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - dx+1 if wrx > bkx else wrx + dx
                self.move_piece('R', pack(wrx, wry))
            elif abs(bkx - wkx) > 2:
                dump("F Vita kungen flyttas vertikalt mot svarta kungen")
                wkx = (wkx - 1 if wkx > bkx else wkx + 1)
                self.move_piece('K', pack(wkx, wky))
            elif abs(wkx - bkx) == 2:
                mh = manhattan(self.wk, self.bk)
                if wky == bky:
                    dump("G Avancera med tornet")
                    wrx = wrx - 1
                    self.move_piece('R', pack(wrx, wry))
                elif mh == 3:
                    dump("H Tempodrag")
                    wry = tempodrag(wry)
                    self.move_piece('R', pack(wrx, wry))
                else:
                    dump("I Flytta vita kungen horisontellt mot svarta kungen")
                    wky = wky - 1 if wky > bky else wky + 1
                    self.move_piece('K', pack(wkx, wky))
            else:
                dump("J Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - 1 if wrx > bkx else wrx + 1
                self.move_piece('R', pack(wrx, wry))

    def play(self):

        while not self.is_checkmate():
            self.display_board()
            if self.antal == 100: break
            dump('Drag:',self.antal)
            self.antal += 1
            self.apply_torres_algorithm()

            if self.is_checkmate(): break
            self.move_black_king()

        self.display_board()
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
