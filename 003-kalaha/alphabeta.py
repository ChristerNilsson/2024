from index import Relocation, FinalScoring, Evaluate, HasSuccessors

LITTERA = "ABCDEF abcdef "

def dump(house,depth,action):
    print()
    print('* ' * depth, list(reversed(house[0:7])), action)
    print('* ' * depth, house[7:14], house[6]-house[13])


def alphaBeta(house, depthMax, player):
    alpha = -1000
    beta = 1000
    playerShop = 13 if player == 1 else 6
    return maxAlphaBeta(house, depthMax, 0, alpha, beta, playerShop, "")


def maxAlphaBeta(house, depthMax, depth, alpha, beta, playerShop, action):
    # dump(house, depth, action)
    if not HasSuccessors(house):
        FinalScoring(house)
        return Evaluate(house, playerShop, (playerShop + 7) % 14)
    elif depth >= depthMax:
        return Evaluate(house, playerShop, (playerShop + 7) % 14)
    else:
        action = ''
        for i in range(playerShop - 6, playerShop):
            if house[i] == 0:
                continue

            tempHouse = house.copy()
            # tempValue = None

            if Relocation(tempHouse, i):
                tempValue = maxAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, playerShop, action + LITTERA[i])
            else:
                tempValue = minAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, playerShop, action + LITTERA[i])

            if alpha < tempValue:
                alpha = tempValue
                action = "ABCDEF"[i]

            if alpha >= beta:
                break

        return action if depth == 0 else alpha


def minAlphaBeta(house, depthMax, depth, alpha, beta, playerShop, action):
    dump(house, depth, action)
    if not HasSuccessors(house):
        FinalScoring(house)
        return Evaluate(house, playerShop, (playerShop + 7) % 14)
    elif depth >= depthMax:
        return Evaluate(house, playerShop, (playerShop + 7) % 14)
    else:
        opponentShop = (playerShop + 7) % 14
        for i in range(opponentShop - 6, opponentShop):
            if house[i] == 0:
                continue

            tempHouse = house.copy()
            # tempValue = None

            if Relocation(tempHouse, i):
                tempValue = minAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, playerShop, action + LITTERA[i])
            else:
                tempValue = maxAlphaBeta(tempHouse, depthMax, depth + 1, alpha, beta, playerShop, action + LITTERA[i])

            if beta > tempValue:
                beta = tempValue

            if alpha >= beta:
                break
        return beta

def makeAllMoves(house, offset, actions="",positions=[]): # offset in [0,7]
    for i in range(offset,offset+6):
        if house[i] == 0: continue
        letter = LITTERA[i]
        house1 = house.copy()
        if Relocation(house1,i):
            if house1[offset:offset+6] == [0, 0, 0, 0, 0, 0]:
                positions.append([actions + letter, house1])
            else:
                makeAllMoves(house1, offset, actions+letter, positions)
        else:
            positions.append([actions+letter,house1])
    return positions


assert('A B CA CB CD CE CF D E F' == ' '.join([move[0] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 0,"", [])]))
assert(912 == len(makeAllMoves([6, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert(232 == len(makeAllMoves([0, 5, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert( 56 == len(makeAllMoves([0, 0, 4, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert( 11 == len(makeAllMoves([0, 0, 0, 3, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert(  2 == len(makeAllMoves([0, 0, 0, 0, 2, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert(  1 == len(makeAllMoves([0, 0, 0, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))
assert(  0 == len(makeAllMoves([0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0],0,"",[])))

assert('a b ca cb cd ce cf d e f' == ' '.join([move[0] for move in makeAllMoves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 7,"", [])]))
assert(912 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 6, 5, 4, 3, 2, 1, 0],7,"",[])))
assert(232 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 5, 4, 3, 2, 1, 0],7,"",[])))
assert( 56 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 3, 2, 1, 0],7,"",[])))
assert( 11 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 3, 2, 1, 0],7,"",[])))
assert(  2 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 2, 1, 0],7,"",[])))
assert(  1 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 0],7,"",[])))
assert(  0 == len(makeAllMoves([4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],7,"",[])))
