def manhattan(p,q):
    dx = abs(p[0] - q[0])
    dy = abs(p[1] - q[1])
    return dx+dy

class ChessGame:
    def __init__(self,wk,wr,bk):
        self.board = [['.' for i in range(8)] for j in range(8)]
        self.white_king = wk
        self.white_rook = wr
        self.black_king = bk

        self.board[self.white_king[0]][self.white_king[1]] = 'K'
        self.board[self.white_rook[0]][self.white_rook[1]] = 'R'
        self.board[self.black_king[0]][self.black_king[1]] = 'k'

        self.antal = 0

    def display_board(self):
        for row in self.board:
            print('   '.join(row))
        print()

    def move_piece(self, piece, new_position):
        """Flytta en pjäs till en ny position"""
        if piece == 'K':
            self.board[self.white_king[0]][self.white_king[1]] = '.'
            self.white_king = new_position
            self.board[self.white_king[0]][self.white_king[1]] = 'K'
        elif piece == 'R':
            self.board[self.white_rook[0]][self.white_rook[1]] = '.'
            self.white_rook = new_position
            self.board[self.white_rook[0]][self.white_rook[1]] = 'R'
        elif piece == 'k':
            self.board[self.black_king[0]][self.black_king[1]] = '.'
            self.black_king = new_position
            self.board[self.black_king[0]][self.black_king[1]] = 'k'

    def is_checkmate(self):
        """Kontrollera om svart kung är schackmatt"""
        bkx, bky = self.black_king
        wkx, wky = self.white_king
        wrx, wry = self.white_rook

        # Om svarta kungen är vid brädets kant och instängd av vit kung och torn, är det schackmatt
        if (bkx in [0, 7] or bky in [0, 7]) and (abs(bkx - wkx) == 2) and (abs(bky - wky) <= 1):
            if bkx == wrx or bky == wry:  # Tornet kontrollerar raden eller linjen
                return True
        return False

    def move_black_king(self):
        """Grundläggande logik för att flytta svarta kungen bort från centrum och mot kanten"""
        bkx, bky = self.black_king
        wkx, wky = self.white_king
        wrx, wry = self.white_rook

        # Flytta mot kanten, grundlogik för att simulera flykten
        if bkx < 7 and bkx + 1 != wrx and abs(bkx-wkx)>2:
            bkx += 1
        elif bkx + 1 != wrx:
            bky = bky+1 if bky < 7 else bky-1
        else:
            if bkx == 0:
                bky = bky+1 if bky<7 else bky-1
            else:
                bkx -= 1
        self.move_piece('k', (bkx, bky))

    def apply_torres_algorithm(self):
        """Implementera Torres' slutspelsalgoritm baserat på de specificerade reglerna"""
        bkx, bky = self.black_king
        wkx, wky = self.white_king
        wrx, wry = self.white_rook

        # Kontrollera om kungen och tornet är för nära varandra
        if manhattan(self.black_king,self.white_rook) <= 2:
            if wrx in [0, 7]:
                print("B Om tornet redan är på a- eller h-filen, gör inget")
            else:
                print("C Flytta tornet till en kantfil (a eller h)")
                new_file = 0 if wrx <= 3 else 7
                if new_file == wry: new_file = 7 - new_file
                self.move_piece('R', (wrx, new_file))
        else:
            dx = abs(bkx - wrx)
            if dx > 1:
                print("E Tornet flyttas vertikalt mot svarta kungen")
                self.move_piece('R', (wrx - dx+1 if wrx > bkx else wrx + dx, wry))
            elif abs(bkx - wkx) > 2:
                print("F Vita kungen flyttas vertikalt mot svarta kungen")
                self.move_piece('K', (wkx - 1 if wkx > bkx else wkx + 1, wky))
            elif abs(wkx - bkx) == 2:
                print("G Kontrollera om den horisontella distansen är noll, jämn eller udda")
                dy = abs(wky - bky)
                if dy == 0:
                    self.move_piece('R', (wrx-1, wry))
                elif dy % 2 == 1:
                    print("H Om tornet är på en kant, flytta till b- eller g-filen")
                    self.move_piece('R', (wrx, 1 if wry == 0 else 6))
                else:
                    print("I Flytta vita kungen horisontellt mot svarta kungen")
                    self.move_piece('K', (wkx, wky - 1 if wky > bky else wky + 1))
            else:
                print("J Tornet flyttas vertikalt mot svarta kungen")
                self.move_piece('R', (wrx - 1 if wrx > bkx else wrx + 1, wry))

    def play(self):

        while not self.is_checkmate():
            self.display_board()
            if self.antal == 100: break
            print("Vit flyttar...",self.antal)
            self.antal += 1
            self.apply_torres_algorithm()

            if self.is_checkmate(): break
            self.display_board()

            print("Svart flyttar...",self.antal)
            self.antal += 1
            self.move_black_king()

        print("Schackmatt!")

game = ChessGame((7,4),(7,7),(0,4))
game.play()
