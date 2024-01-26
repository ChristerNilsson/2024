from index import Relocation, FinalScoring, HasSuccessors
import time
import random

ALFABETA = True
# ALFABETA is 10 up to 100 times faster than minimax
DEPTH = 2

LITTERA = "ABCDEF abcdef "
# N = 4  # beans per pit
C = 0  # Computer
H = 1  # Human
nodes = 0

def s2(n): return ' ' + str(n) if n<10 else str(n)

def ass(a,b):
    if a != b:
        print('Assert failure:')
        print(a)
        print(b)
        assert a == b

def dump(house,act,depth,value):
    depth = 0
    #return
    #print()
    first  = ' ' * 40 * depth + ' '.join([s2(pit) for pit in reversed(house[0:7])])
    second = ' ' * 40 * depth + '   ' + ' '.join([s2(pit) for pit in house[7:14]])
    if depth % 2 == 1:
        print(first)
        print(second, ' ', act, ' ', value)
    else:
        print(first, ' ', act, ' ', value)
        print(second)

def makeAllMoves(house, player, positions, actions=""): # offset = 0 or 7
    offset = [0,7][player]
    for i in range(offset,offset+6):
        if house[i] == 0: continue
        house1 = house.copy()
        if Relocation(house1,i):
            if house1[offset:offset+6] == [0, 0, 0, 0, 0, 0]:
                positions.append([house1, actions + LITTERA[i], house1[6] - house1[13]])
            else:
                makeAllMoves(house1, player, positions, actions + LITTERA[i])
        else:
            positions.append([house1,actions+LITTERA[i], house1[6] - house1[13]])
    return positions


def getMoves(house, player):
    moves = makeAllMoves(house, player, [], "")
    if player % 2 == 0:  # Sortering innebär cirka 2-3 ggr snabbare exekvering
        moves.sort(key=lambda move: -move[2])  # minus
    else:
        moves.sort(key=lambda move: move[2])   # plus
    # for move in moves:
    #     print(move)
    return moves


def alphaBeta(house, depthMax, player):
    if depthMax == 0:
        moves = getMoves(house,player)
        return random.choice(moves)
    elif depthMax == 1:
        moves = getMoves(house,player)
        return moves[0]
    else:
        return maxAlphaBeta(house, depthMax, 0, -999, 999, player)


def maxAlphaBeta(house, depthMax, depth, alpha, beta, player):
    global nodes
    nodes += 1
    opponent = 1 - player
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[6] - house[13]
    elif depth >= depthMax:
        return house[6] - house[13]
    else:
        moves = getMoves(house, player)
        top = None
        maxEval = -999
        for [tempHouse,act,value] in moves:
            # dump(tempHouse, act, depth, value)
            eval = minAlphaBeta(tempHouse, depthMax, depth+1, alpha, beta, opponent)
            if ALFABETA:
                if alpha < eval:
                    alpha = eval
                    top = [tempHouse, act, eval]
                if beta <= alpha: break
            else:
                if eval > maxEval:
                    maxEval = eval
                    top = [tempHouse, act, eval]
        if depth == 0: return top
        return alpha if ALFABETA else maxEval


def minAlphaBeta(house, depthMax, depth, alpha, beta, player):
    global nodes
    nodes += 1
    opponent = 1 - player
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[6] - house[13]
    elif depth >= depthMax:
        return house[6] - house[13]
    else:
        moves = getMoves(house, player)
        minEval = 999
        for [tempHouse,act,value] in moves:
            # dump(tempHouse, act, depth, value)
            eval = maxAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, opponent)
            if ALFABETA:
                if beta > eval: beta = eval
                if beta <= alpha: break
            else:
                minEval = min(minEval, eval)
        return beta if ALFABETA else minEval

start = time.time_ns()

# moves = makeAllMoves([6, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0], H, [], "")
# moves.sort(key=lambda move: -move[2])
# assert moves[0] == [[0, 1, 2, 0, 0, 0, 24, 0, 5, 4, 3, 2, 1, 0], 'FEFDFCFEFBFAFEFDFE', 24]
#
# ass('A B CA CB CD CE CF D E F', ' '.join([move[1] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], H, [])]))
#
# ass('A B C DA DB DC DE DF EA EB EC EDA EDB EDC EDE EDF EF FA FB FC FDA FDB FDC FDE FDFA FDFB FDFC FDFE FEA FEB FEC FEDA FEDB FEDC FEDE FEDF FEFA FEFB FEFC FEFDA FEFDB FEFDC FEFDE FEFDFA FEFDFB FEFDFC FEFDFE', ' '.join([move[1] for move in makeAllMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], H,[])]))
# ass("a b c da db dc de df ea eb ec eda edb edc ede edf ef fa fb fc fda fdb fdc fde fdfa fdfb fdfc fdfe fea feb fec feda fedb fedc fede fedf fefa fefb fefc fefda fefdb fefdc fefde fefdfa fefdfb fefdfc fefdfe", ' '.join([move[1] for move in makeAllMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], C,[])]))
# ass(912, len(makeAllMoves([6, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# ass(912, len(makeAllMoves([6, 5, 4, 3, 2, 1, 3, 6, 5, 4, 3, 2, 1, 3], H, [])))
#
# assert(232 == len(makeAllMoves([0, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# assert( 56 == len(makeAllMoves([0, 0, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# assert( 11 == len(makeAllMoves([0, 0, 0, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# assert(  2 == len(makeAllMoves([0, 0, 0, 0, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# assert(  1 == len(makeAllMoves([0, 0, 0, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
# assert(  0 == len(makeAllMoves([0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0], H, [])))
#
# assert('a b ca cb cd ce cf d e f' == ' '.join([move[1] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], C, [])]))
# assert(912 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 6, 5, 4, 3, 2, 1, 0], C, [])))
# assert(232 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 5, 4, 3, 2, 1, 0], C, [])))
# assert( 56 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 3, 2, 1, 0], C, [])))
# assert( 11 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 3, 2, 1, 0], C, [])))
# assert(  2 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 2, 1, 0], C, [])))
# assert(  1 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0], C, [])))
# assert(  0 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0], C, [])))
#
# ass([[0, 4, 4, 0, 1, 0,  9, 3, 3, 0, 3, 2, 1,  0], 'FEFDFA', 9],              getMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], H)[0])
# ass([[0, 1, 2, 0, 0, 0, 27, 0, 5, 4, 3, 2, 1,  3], 'FEFDFCFEFBFAFEFDFE', 24], getMoves([6, 5, 4, 3, 2, 1, 3, 6, 5, 4, 3, 2, 1, 3], H)[0])
# ass([[0, 5, 4, 3, 2, 1,  3, 0, 1, 2, 0, 0, 0, 27], 'fefdfcfefbfafefdfe', 24], getMoves([6, 5, 4, 3, 2, 1, 3, 6, 5, 4, 3, 2, 1, 3], C)[0])

#############
# ass([[5, 5, 4, 4, 4, 4, 0, 4, 4, 0, 0, 6, 6, 2], 'cd', 2], getMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], C)[0])
# ass([[5, 5, 4, 4, 4, 4, 0, 4, 4, 0, 0, 6, 6, 2], 'cd', 2], alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 1, C))
#print('Best move: ',alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], DEPTH, C),'nodes:',nodes)
#print('Best move: ', alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], DEPTH, C), 'nodes:', nodes)

# ass([], alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 2, C))
# ass([], alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 3, C))
# ass([], alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 4, C))
# ass([], alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 5, C))
# ass([], alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 6, C))

#print('\nBEST CHOICE:', alphaBeta([6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0], 10, H))
#print('\nBEST CHOICE:', alphaBeta([7, 1, 8, 0, 8, 8, 2, 8, 7, 7, 1, 7, 7, 1], 10, H))
#print('\nBEST CHOICE:', alphaBeta([0, 3, 9, 1, 9, 9, 3, 1, 9, 8, 2, 8, 8, 2], 10, H))
#print('\nBEST CHOICE:', alphaBeta([6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0], 6, H))
#print('\nBEST CHOICE:', alphaBeta([1, 0, 12, 1, 12, 12, 5, 2, 9, 0, 3, 1, 10, 4], 10, H))
#print('\nBEST CHOICE:', alphaBeta([3,2,1,3,0,14,18,4,0,2,1,3,1,20], 10, H))
#print('\nBEST CHOICE:', alphaBeta([4,3,2,4,0,0,27,0,1,1,3,5,1,21], 16, H))
#print('\nBEST CHOICE:', alphaBeta([0,5,4,5,1,0,28,0,1,1,3,0,1,23], 16, H))
#print('\nBEST CHOICE:', alphaBeta([0,0,1,7,0,0,35,0,0,2,3,0,0,24], 20, H))

#print('BEST CHOICE:', alphaBeta([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 8, C))
#print('BEST CHOICE:', alphaBeta([6,5,4,3, 2, 1, 0, 3, 6,5,4, 3, 2, 1, 0], 2, C))

# Level 1 (118-kalaha) Resultat: 41-7 Styrka 6
#print('\nBEST CHOICE:', alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 6, H))
#print('\nBEST CHOICE:', alphaBeta([5,0,0,7,6,6,2,5,5,0,5,5,0,2], 6, H))
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,7,7,3,1,2,3,8,7,0,10], 6, H))
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,0,8,4,1,4,4,9,8,0,10], 6, H))

# Level 1 (118-kalaha) Resultat: 35-13 Styrka 4
#print('\nBEST CHOICE:', alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([5,0,0,6,6,6,2,5,5,4,4,4,0,1], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,7,7,3,1,2,3,7,7,0,11], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([1,1,1,1,0,8,4,2,3,4,1,9,1,12], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([2,1,1,0,0,0,5,1,5,1,3,11,1,17], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([3,0,2,1,0,0,9,0,1,3,2,0,1,26], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,1,3,2,0,0,9,0,0,4,2,0,0,27], 4, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,4,2,0,0,9,0,0,0,3,0,1,29], 4, 1))  # 0=computer 1=human

# Level 2 (118-kalaha) Resultat:  31-17 Styrka 2
#print('\nBEST CHOICE:', alphaBeta([], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,1,7,7,6,6,1,4,4,0,5,5,0,2], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([1,2,0,8,7,7,2,5,5,1,0,6,1,3], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,2,0,0,8,8,3,1,2,4,3,9,0,8], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([2,3,1,0,0,10,4,3,4,1,2,1,2,15], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([2,3,0,0,0,10,7,3,0,0,3,2,3,15], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([4,5,2,1,0,0,8,4,1,1,1,2,1,18], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([4,0,0,2,0,0,10,4,0,1,0,0,0,27], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,1,1,3,0,0,12,0,0,2,1,1,0,27], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,2,0,1,0,14,0,0,0,2,2,0,27], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,1,2,0,14,0,0,0,0,1,1,29], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,3,0,14,0,0,0,0,0,1,30], 2, 1))  # 0=computer 1=human

# Level 3 (118-kalaha) Resultat:  20-28 Styrka 2
#print('\nBEST CHOICE:', alphaBeta([], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,1,7,6,6,6,1,4,4,0,5,0,6,2], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,7,7,7,2,1,6,2,6,0,6,4], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([1,1,1,0,8,8,3,2,7,3,1,1,7,5], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,3,3,1,9,9,3,2,7,3,1,1,0,6], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,5,3,1,9,9,3,2,0,4,2,2,1,7], 2, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,5,0,1,10,10,3,0,1,0,0,0,0,18], 2, 1))  # 0=computer 1=human

#print((time.time_ns()-start)/10**6)


house= [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
# house = [6, 5, 4, 3, 2, 1, 3, 6, 5, 4, 3, 2, 1, 3]

moves = getMoves(house, C)

def show(house):
    first  =         ' '.join([s2(pit) for pit in reversed(house[0:7])])
    second = '   ' + ' '.join([s2(pit) for pit in house[7:14]])
    print(first, '    F E D C B A')
    print(second, ' a b c d e f')

player = C
depth = 10
while True:
    show(house)
    if player == C:
        nodes = 0
        [house,actions,value] = alphaBeta(house,depth,player)
        print('Computer:',actions,f'value:{value} nodes:{nodes}')
        show(house)
        player = 1 - player

    while True:
        letter = input('You: ')
        i = LITTERA.index(letter)
        if house[i] > 0: break

    while Relocation(house,i):
        show(house)
        if not HasSuccessors(house):
            FinalScoring(house)
            break
        else:
            letter = input('You: ')
            i = LITTERA.index(letter)
    player = 1 - player
