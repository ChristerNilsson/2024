import time

import chess.syzygy

def row(p): return p // 8
def col(p): return p % 8
def pretty(piece): return "abcdefgh"[col(piece)] + str(1+row(piece))

def fen_from_board(brd):
    res = ""
    brd.reverse()
    for row in brd:
        n = 0
        for sq in row:
            if sq == ".": n += 1
            else:
                if n != 0: res += str(n)
                res += sq
                n = 0
        if n != 0: res += str(n)
        res += "/" if res.count("/") < 7 else ""
    res += " w - - 0 1\n"
    return res

def setPiece(matrix,piece,col,row):
    matrix[row][col] = piece

def getFen(wk,wr,bk,color):
    matrix = [["."]*8 for i in range(8)]
    setPiece(matrix,"K",row(wk),col(wk))
    setPiece(matrix,"R",row(wr),col(wr))
    setPiece(matrix,"k",row(bk),col(bk))
    return fen_from_board(matrix)

start = time.time_ns()
with chess.syzygy.open_tablebase("syzygy") as tablebase:
    res = []
    for wk in [0, 1, 2, 3, 9, 10, 11, 18, 19, 27]:
        for wr in range(64):
            for bk in range(64):
                fen = getFen(wk,wr,bk,'w')
                board = chess.Board(fen)
                if board.is_valid():
                    try:
                        score = tablebase.probe_dtz(board)
                        res.append(score)
                    finally:
                        pass

print((time.time_ns() - start)/10**6)
print(len(res))

#####################################################

# ROOK_MOVES = [[-1, 0], [0, -1], [0, 1], [1, 0]]
# KING_MOVES = [[-1, -1], [-1, 0], [-1, 1],  [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
#
# whiteScore = [99] * 40960
# blackScore = [99] * 40960
#
# level = 0
#
# wk2ten = {27: 9,   18: 7, 19: 8,   9: 4, 10: 5, 11: 6,   0: 0, 1: 1, 2: 2, 3: 3}
#
# TRANS = [  # used to find number of rotations [row][col]
#     0,0,0,0,1,1,1,1,
#     0,0,0,0,1,1,1,1,
#     0,0,0,0,1,1,1,1,
#     0,0,0,0,1,1,1,1,
#     3,3,3,3,2,2,2,2,
#     3,3,3,3,2,2,2,2,
#     3,3,3,3,2,2,2,2,
#     3,3,3,3,2,2,2,2
# ]
#
# ROTATE = [
#     56,48,40,32,24,16, 8,0,
#     57,49,41,33,25,17, 9,1,
#     58,50,42,34,26,18,10,2,
#     59,51,43,35,27,19,11,3,
#     60,52,44,36,28,20,12,4,
#     61,53,45,37,29,21,13,5,
#     62,54,46,38,30,22,14,6,
#     63,55,47,39,31,23,15,7
# ]
#
# # def getDMZ(wk,wr,bk):
# #     return matrix[4096 * wk2ten[wk] + 64 * wr + bk]
#
# def nice(p):
#     [wk,wr,bk] = p
#     return pretty(wk) + ' ' + pretty(wr) + ' ' + pretty(bk)
#
#
# def spegla(piece):
#     kol, rad = row(piece), col(piece)
#     return rad * 8 + kol
#
# def mirror(wk,wr,bk):
#     wk = spegla(wk)
#     wr = spegla(wr)
#     bk = spegla(bk)
#     return [wk,wr,bk]
#
# def rotate(wk,wr,bk):
#     wk = ROTATE[wk]
#     wr = ROTATE[wr]
#     bk = ROTATE[bk]
#     return [wk,wr,bk]
#
# def getIndex(p):
#     [wk, wr, bk] = p
#     for i in range(TRANS[wk]):
#         wk,wr,bk = rotate(wk,wr,bk)
#     if col(wk) < row(wk): wk,wr,bk = mirror(wk,wr,bk)
#     elif col(wk) == row(wk):
#         if col(bk) < row(bk): wk,wr,bk = mirror(wk,wr,bk)
#         elif col(bk) == row(bk):
#             if col(wr) < row(wr): wk,wr,bk = mirror(wk,wr,bk)
#     assert wk2ten[wk] < 10
#     return 4096 * wk2ten[wk] + 64 * wr + bk
#
# def pos(x,y): return x+8*y
#
# def sqDist(a,b):
#     dx = col(a) - col(b)
#     dy = row(a) - row(b)
#     return dx*dx + dy*dy
#
# def onBoard(x,y): return 0 <= x < 8 and 0 <= y < 8
#
# def ass(a, b):
#     if a != b:
#         print('Failed:', b, a)
#         assert a == b
#
# # def pos(p): return 8 * row(p) + col(p)
# def order(a,b,c): return a < b < c or c < b < a
# ass(order(0,2,4),True)
# ass(order(0,4,2),False)
# ass(order(2,0,4),False)
# ass(order(2,4,0),False)
# ass(order(4,0,2),False)
# ass(order(4,2,0),True)
#
# def check(p):
#     [wk, wr, bk] = p
#     if row(wk) == row(wr) == row(bk): return not order(col(bk),col(wk),col(wr))
#     if col(wk) == col(wr) == col(bk): return not order(row(bk),row(wk),row(wr))
#     return row(wr) == row(bk) or col(wr) == col(bk)
# ass(check([0,2,4]),True)
# ass(check([0,4,2]),True)
# ass(check([2,0,4]),False)
# ass(check([2,4,0]),False)
# ass(check([4,0,2]),True)
# ass(check([4,2,0]),True)
# ass(check([0,18,36]),False)
# ass(check([56,4,2]),True)
# ass(check([56,20,4]),True)
#
# def moveWhiteRook(p):
#     [wk, wr, bk] = p
#     res = []
#     x0 = col(wr)
#     y0 = row(wr)
#     for [dx, dy] in ROOK_MOVES:  # WR
#         x, y = x0 + dx, y0 + dy
#         sq = pos(x, y)
#         while onBoard(x, y) and sq != wk and sq != bk:
#             if not check([wk,sq,bk]):
#                 res.append([wk, sq, bk])  # , 0getDMZ(wk, sq, bk)])
#             x, y = x + dx, y + dy
#             sq = pos(x, y)
#     return res
# ass(moveWhiteRook([2,16,0]), [[2, 17, 0], [2, 18, 0], [2, 19, 0], [2, 20, 0], [2, 21, 0], [2, 22, 0], [2, 23, 0]])
# ass(moveWhiteRook([0,18,4]), [[0, 17, 4], [0, 16, 4], [0, 10, 4], [0, 26, 4], [0, 34, 4], [0, 42, 4], [0, 50, 4], [0, 58, 4], [0, 19, 4], [0, 21, 4], [0, 22, 4], [0, 23, 4]])
#
# def moveWhiteKing(p):
#     [wk, wr, bk] = p
#     res = []
#     x0 = col(wk)
#     y0 = row(wk)
#     for [dx, dy] in KING_MOVES:  # WK
#         x, y = x0 + dx, y0 + dy
#         sq = pos(x, y)
#         if onBoard(x, y) and sq != wr and sqDist(sq,bk) > 2 and not check([sq,wr,bk]):
#             res.append([sq, wr, bk]) #, getDMZ(wk, self.wr, self.bk)])
#     return res
# ass(moveWhiteKing([18,27,16]), [[10, 27, 16], [26, 27, 16], [11, 27, 16], [19, 27, 16]])
# ass(moveWhiteKing([18,19,16]), [])
#
# def moveBlackKing(p):
#     [wk, wr, bk] = p
#     res = []
#     x0 = col(bk)
#     y0 = row(bk)
#     for [dx, dy] in KING_MOVES:  # WK
#         x, y = x0 + dx, y0 + dy
#         sq = pos(x, y)
#         if onBoard(x, y) and sqDist(sq,wk) > 2: # and not check([sq,wr,bk]):
#             res.append([wk, wr, sq]) #, getDMZ(wk, self.wr, self.bk)])
#     return res
# ass(moveBlackKing([18,27,16]), [[18, 27, 8], [18, 27, 24]])
# ass(moveBlackKing([0,27,18]), [[0, 27, 17], [0, 27, 25], [0, 27, 10], [0, 27, 26], [0, 27, 11], [0, 27, 19], [0, 27, 27]])
#
# def getMoves(p): # p = [wk,wr,bk]
#     res = []
#     if level % 2 == 0:
#         res = res + moveWhiteRook(p)
#         if not check(p):
#             res = res + moveWhiteKing(p)
#     else:
#         res = res + moveBlackKing(p)
#     return res
# ass(moveBlackKing([18,27,16]), [[18, 27, 8], [18, 27, 24]])
# ass(getMoves([18,27,16]), [[18, 26, 16], [18, 25, 16], [18, 19, 16], [18, 11, 16], [18, 3, 16], [18, 35, 16], [18, 43, 16], [18, 51, 16], [18, 59, 16], [18, 28, 16], [18, 29, 16], [18, 30, 16], [18, 31, 16], [10, 27, 16], [26, 27, 16], [11, 27, 16], [19, 27, 16]])
#
# front0 = [
#     [2, 16, 0], # c,1,a,3,a,1,zero
#     [2, 24, 0], # c,1,a,4,a,1,zero
#     [2, 32, 0], # c,1,a,5,a,1,zero
#     [2, 40, 0], # c,1,a,6,a,1,zero
#     [2, 48, 0], # c,1,a,7,a,1,zero
#     [2, 56, 0], # c,1,a,8,a,1,zero
#     [10, 16, 0], # c,2,a,3,a,1,zero
#     [10, 24, 0], # c,2,a,4,a,1,zero
#     [10, 24, 8], # c,2,a,4,a,2,zero
#     [10, 32, 0], # c,2,a,5,a,1,zero
#     [10, 32, 0], # c,2,a,5,a,2,zero
#     [10, 40, 0], # c,2,a,6,a,1,zero
#     [10, 40, 16], # c,2,a,6,a,2,zero
#     [10, 48, 0],  # c,2,a,7,a,1,zero
#     [10, 48, 8],  # c,2,a,7,a,2,zero
#     [10, 56, 0],  # c,2,a,8,a,1,zero
#     [10, 56, 8],  # c,2,a,8,a,2,zero
#     [18, 0, 3],   # c,3,a,1,c,1,zero
#     [18, 4, 2],   # c,3,e,1,c,1,zero
#     [18, 5, 2],   # c,3,f,1,c,1,zero
#     [18, 6, 2],   # c,3,g,1,c,1,zero
#     [18, 7, 2],   # c,3,h,1,c,1,zero
#     [19, 0, 3],   # d,3,a,1,d,1,zero
#     [19, 1, 3],   # d,3,b,1,d,1,zero
#     [19, 5, 3],   # d,3,f,1,d,1,zero
#     [19, 6, 3],   # d,3,g,1,d,1,zero
#     [19, 7, 3],   # d,3,h,1,d,1,zero
# ]
#
# print(front0)
# for level in range(17):
#     front1 = []
#     for item in front0:
#         moves = getMoves(item)
#         for move in moves:
#             if move[0] not in [0, 1, 2, 3, 9, 10, 11, 18, 19, 27]: continue
#             index = getIndex(move)
#             if level % 2 == 0:
#                 if level + 1 < whiteScore[index]:
#                     whiteScore[index] = level + 1
#                     front1.append(move)
#             else:
#                 if level + 1 < whiteScore[index]:
#                     blackScore[index] = level + 1
#                     front1.append(move)
#             # print(f"score[{move}] = {level+1}")
#     front0 = front1
#     print(level,len(front0))
#
# for wk in [0, 1, 2, 3, 9, 10, 11, 18, 19, 27]:
#     for wr in range(64):
#         for bk in range(64):
#             index = 4096 * wk2ten[wk] + 64 * wr + bk
#             if whiteScore[index] != 99: print(pretty(wk), pretty(wr),pretty(bk),whiteScore[index])
#             #if blackScore[index] != 99: print(pretty(wk), pretty(wr),pretty(bk),blackScore[index])
