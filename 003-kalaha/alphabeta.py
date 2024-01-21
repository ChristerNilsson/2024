from index import Relocation, FinalScoring, HasSuccessors
import time
import random

LITTERA = "ABCDEF abcdef "
N = 4  # beans per pit
nodes = 0

def s2(n): return ' ' + str(n) if n<10 else str(n)

def dump(house):
    print()
    print('  ' + ' '.join([s2(pit) for pit in reversed(house[0:6])]))
    print(s2(house[6]),'               ',s2(house[13]))
    print('  ' + ' '.join([s2(pit) for pit in house[7:13]]))


def makeAllMoves(house, player, positions, actions=""): # offset = 0 or 7
    offset = [0,7][player]
    myAcc = [6,13][player]
    for i in range(offset,offset+6):
        if house[i] == 0: continue
        house1 = house.copy()
        if Relocation(house1,i):
            if house1[offset:offset+6] == [0, 0, 0, 0, 0, 0]:
                positions.append([house1, actions + LITTERA[i], house1[myAcc] - house1[19-myAcc]])
            else:
                makeAllMoves(house1, player, positions, actions + LITTERA[i])
        else:
            positions.append([house1,actions+LITTERA[i], house1[myAcc]-house1[19-myAcc]])
    return positions


def getMoves(house, player):
    moves = makeAllMoves(house, player, [], "")
    moves.sort(key=lambda move: -move[2])
    return moves


def alphaBeta(house, depthMax, player):
    return maxAlphaBeta(house, depthMax, 0, -999, 999, player)


def maxAlphaBeta(house, depthMax, depth, alpha, beta, player):  # player = 0 or 1
    global nodes
    nodes += 1
    opponent = 1 - player
    myAcc = [6,13][player]
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[myAcc] - house[19-myAcc]
    elif depth >= depthMax:
        return house[myAcc] - house[19-myAcc]
    else:
        moves = getMoves(house, player)
        top = None
        for [tempHouse,act,value] in moves:
            tempValue = minAlphaBeta(tempHouse, depthMax, depth+1, alpha, beta, opponent)
            if alpha < tempValue:
                alpha = tempValue
                top = [tempHouse,act,value]
            if alpha >= beta:
                break
        return top if depth == 0 else alpha


def minAlphaBeta(house, depthMax, depth, alpha, beta, player): # 0 or 1
    global nodes
    nodes += 1
    opponent = 1 - player
    myAcc = [6,13][player]
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[myAcc] - house[19 - myAcc]
    elif depth >= depthMax:
        return house[myAcc] - house[19 - myAcc]
    else:
        moves = getMoves(house, player)
        for [tempHouse,act,value] in moves:
            tempValue = maxAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, opponent)
            if beta > tempValue:
                beta = tempValue
            if alpha >= beta:
                break
        return beta


start = time.time_ns()

# assert('A B CA CB CD CE CF D E F' == ' '.join([move[0] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 0)]))
#assert('A B C DA DB DC DE DF EA EB EC EDA EDB EDC EDE EDF EF FA FB FC FDA FDB FDC FDE FDFA FDFB FDFC FDFE FEA FEB FEC FEDA FEDB FEDC FEDE FEDF FEFA FEFB FEFC FEFDA FEFDB FEFDC FEFDE FEFDFA FEFDFB FEFDFC FEFDFE' == ' '.join([move[0] for move in makeAllMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 0,"",[])]))
#assert("a b c da db dc de df ea eb ec eda edb edc ede edf ef fa fb fc fda fdb fdc fde fdfa fdfb fdfc fdfe fea feb fec feda fedb fedc fede fedf fefa fefb fefc fefda fefdb fefdc fefde fefdfa fefdfb fefdfc fefdfe" == ' '.join([move[0] for move in makeAllMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 7,"",[])]))
# assert(912 == len(makeAllMoves([6, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert(232 == len(makeAllMoves([0, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert( 56 == len(makeAllMoves([0, 0, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert( 11 == len(makeAllMoves([0, 0, 0, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert(  2 == len(makeAllMoves([0, 0, 0, 0, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert(  1 == len(makeAllMoves([0, 0, 0, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
# assert(  0 == len(makeAllMoves([0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))

#assert('a b ca cb cd ce cf d e f' == ' '.join([move[0] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 7,"", [])]))
# assert(912 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 6, 5, 4, 3, 2, 1, 0],7,"",[])))
# assert(232 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 5, 4, 3, 2, 1, 0],7,"",[])))
# assert( 56 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 3, 2, 1, 0],7,"",[])))
# assert( 11 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 3, 2, 1, 0],7,"",[])))
# assert(  2 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 2, 1, 0],7,"",[])))
# assert(  1 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0],7,"",[])))
# assert(  0 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],7,"",[])))

# moves = getMoves([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 0)  # 0 or 1
# print(len(moves))
# for move in moves:
#     print(move)


#print('\nBEST CHOICE:', alphaBeta([6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0], 7, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0], 10, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([7, 1, 8, 0, 8, 8, 2, 8, 7, 7, 1, 7, 7, 1], 10, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0, 3, 9, 1, 9, 9, 3, 1, 9, 8, 2, 8, 8, 2], 10, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([6, 0, 7, 7, 7, 7, 1, 7, 6, 6, 6, 6, 6, 0], 6, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([1, 0, 12, 1, 12, 12, 5, 2, 9, 0, 3, 1, 10, 4], 10, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([3,2,1,3,0,14,18,4,0,2,1,3,1,20], 10, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([4,3,2,4,0,0,27,0,1,1,3,5,1,21], 16, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,5,4,5,1,0,28,0,1,1,3,0,1,23], 16, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,1,7,0,0,35,0,0,2,3,0,0,24], 20, 1))  # 0=computer 1=human

#print('BEST CHOICE:', alphaBeta([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 8, 0))  # 0=computer 1=human
#print('BEST CHOICE:', alphaBeta([6,5,4,3, 2, 1, 0, 3, 6,5,4, 3, 2, 1, 0], 2, 0))  # 0=computer 1=human

# Level 1 (118-kalaha) Resultat: 41-7 Styrka 6
#print('\nBEST CHOICE:', alphaBeta([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 6, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([5,0,0,7,6,6,2,5,5,0,5,5,0,2], 6, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,7,7,3,1,2,3,8,7,0,10], 6, 1))  # 0=computer 1=human
#print('\nBEST CHOICE:', alphaBeta([0,0,0,0,0,8,4,1,4,4,9,8,0,10], 6, 1))  # 0=computer 1=human

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
#house = [6, 5, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0]
player = 0
while True:
    dump(house)
    if player == 0:
        nodes = 0
        [house,actions,value] = alphaBeta(house,8,player)
        print('Computer:',actions,f'({value}) {nodes}')
        dump(house)
        player = 1 - player

    while True:
        letter = input('You: ')
        i = LITTERA.index(letter)
        if house[i] > 0: break

    while Relocation(house,i):
        dump(house)
        if not HasSuccessors(house):
            FinalScoring(house)
            break
        else:
            letter = input('You: ')
            i = LITTERA.index(letter)
    player = 1 - player
