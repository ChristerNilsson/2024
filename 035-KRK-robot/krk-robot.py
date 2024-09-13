EMPTY = '.'

def manhattan(p,q):
    px,py = unpack(p)
    qx,qy = unpack(q)
    dx = abs(px - qx)
    dy = abs(py - qy)
    return dx+dy

def unpack(index): return (index//8,index%8)
def pack(x,y): return (8 * x + y)

class ChessGame:
    def __init__(self,position):
        self.board = [EMPTY] * 64
        self.wk = pack(7-"12345678".index(position[1]), "abcdefgh".index(position[0]))
        self.wr = pack(7-"12345678".index(position[3]), "abcdefgh".index(position[2]))
        self.bk = pack(7-"12345678".index(position[5]), "abcdefgh".index(position[4]))

        self.board[self.wk] = 'K'
        self.board[self.wr] = 'R'
        self.board[self.bk] = 'k'
        self.antal = 0

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

        # Om svarta kungen är vid brädets kant och instängd av vit kung och torn, är det schackmatt
        if (bkx in [0, 7] or bky in [0, 7]) and (abs(bkx - wkx) == 2) and (abs(bky - wky) <= 1):
            if bkx == wrx or bky == wry:  return True
        return False

    def move_black_king(self):
        """Grundläggande logik för att flytta svarta kungen bort från centrum och mot kanten"""
        bkx, bky = unpack(self.bk)
        wkx, wky = unpack(self.wk)
        wrx, wry = unpack(self.wr)

        # Flytta mot kanten, grundlogik för att simulera flykten
        if bkx < 7 and bkx + 1 != wrx and abs(bkx-wkx) > 2:
            bkx += 1
        elif bkx + 1 != wrx:
            bky += 1 if bky < 7 else -1
        else:
            if bkx == 0:
                bky += 1 if bky < 7 else -1
            else:
                bkx -= 1
        self.move_piece('k', pack(bkx, bky))

    def apply_torres_algorithm(self):
        """Implementera Torres' slutspelsalgoritm baserat på de specificerade reglerna"""
        bkx, bky = unpack(self.bk)
        wkx, wky = unpack(self.wk)
        wrx, wry = unpack(self.wr)

        # Kontrollera om kungen och tornet är för nära varandra
        if manhattan(self.bk,self.wr) <= 2:
            if wrx in [0, 7]:
                print("B Om tornet redan är på a- eller h-filen, gör inget")
            else:
                print("C Flytta tornet i säkerhet")
                new_file = 0 if wrx <= 3 else 7
                if new_file == wry: new_file = 7 - new_file
                self.move_piece('R', pack(wrx, new_file))
        else:
            dx = abs(bkx - wrx)
            if dx > 1:
                print("E Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - dx+1 if wrx > bkx else wrx + dx
                self.move_piece('R', pack(wrx, wry))
            elif abs(bkx - wkx) > 2:
                print("F Vita kungen flyttas vertikalt mot svarta kungen")
                wkx = (wkx - 1 if wkx > bkx else wkx + 1)
                self.move_piece('K', pack(wkx, wky))
            elif abs(wkx - bkx) == 2:
                # "G Kontrollera om den horisontella distansen är noll, jämn eller udda")
                dy = abs(wky - bky)
                if dy == 0:
                    wrx = wrx - 1
                    self.move_piece('R', pack(wrx, wry))
                elif dy % 2 == 1:
                    print("H Tempodrag")
                    wry = 1 if wry == 0 else 6
                    self.move_piece('R', pack(wrx, wry))
                else:
                    print("I Flytta vita kungen horisontellt mot svarta kungen")
                    wky = wky - 1 if wky > bky else wky + 1
                    self.move_piece('K', pack(wkx, wky))
            else:
                print("J Tornet flyttas vertikalt mot svarta kungen")
                wrx = wrx - 1 if wrx > bkx else wrx + 1
                self.move_piece('R', pack(wrx, wry))

    def play(self):

        while not self.is_checkmate():
            self.display_board()
            if self.antal == 100: break
            print("White",self.antal)
            self.antal += 1
            self.apply_torres_algorithm()

            if self.is_checkmate(): break
            self.display_board()

            print("Black",self.antal)
            self.antal += 1
            self.move_black_king()

        self.display_board()
        print("Schackmatt!")

# game = ChessGame("d1h1d8") # KRk
game = ChessGame("a1b2c3") # KRk
game.play()
