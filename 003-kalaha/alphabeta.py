from index import Relocation, FinalScoring, Evaluate, HasSuccessors

LITTERA = "ABCDEF abcdef "
N = 4  # beans per pit

def dump(house,depth,action):
    return
    # print(' *' * depth, house[6]-house[13], action)
    # print()
    # print(' *' * depth, list(reversed(house[0:7])),action)
    # print(' *' * depth, house[7:14], house[6]-house[13])


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
            positions.append([house1,actions+LITTERA[i], house1[6]-house1[13]])
    return positions


def getMoves(house, player): # offset = 0 or 1
    moves = makeAllMoves(house, player, [], "")
    moves.sort(key=lambda move: -move[2])
    return moves


def alphaBeta(house, depthMax, player):
    if player == 0:
        curr = maxAlphaBeta(house, depthMax, 0, player)
    else:
        curr = minAlphaBeta(house, depthMax, 0, player)
    dump(house,0,"")
    return curr

def maxAlphaBeta(house, depthMax, depth, player):  # player = 0 or 1
    # dump(house, depth, "")
    opponent = 1 - player
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[6] - house[13]
    elif depth >= depthMax:
        return house[6] - house[13]
    else:
        # startPit = 0 if playerShop == 6 else 7
        moves = getMoves(house, player)
        # print(len(moves))
        best = -999
        top = None
        for [tempHouse,act,value] in moves:
            curr = minAlphaBeta(tempHouse, depthMax, depth+1, opponent)
            dump(tempHouse,depth,act)
            if curr > best:
                best = curr
                top = [tempHouse,act,value]
        return top if depth == 0 else best

def minAlphaBeta(house, depthMax, depth, player): # 0 or 1
    # dump(house, depth, "")
    opponent = 1 - player # Shop = (playerShop + 7) % 14
    if not HasSuccessors(house):
        FinalScoring(house)
        return house[6] - house[13]
    elif depth >= depthMax:
        return house[6] - house[13]
    else:
        # startPit = 0 if playerShop == 6 else 7
        moves = getMoves(house, player)
        # print(len(moves))
        best = 999
        for [tempHouse,act,value] in moves:
            curr = maxAlphaBeta(tempHouse, depthMax, depth + 1, opponent)
            dump(tempHouse,depth,act)
            if curr < best:
                best = curr
        return best

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
#
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

#print('\nBEST CHOICE:', alphaBeta([N, N, N, N, N, N, 0, N, N, N, N, N, N, 0], 6, 0))  # 0=computer 1=human

print('BEST CHOICE:', alphaBeta([3, 3, 3, 3, 2, 1, 0, 3, 3, 3, 3, 2, 1, 0], 6, 0))  # 0=computer 1=human
