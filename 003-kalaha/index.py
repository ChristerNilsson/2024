def Relocation(house, pickedHouse): # returns True if last bean in Shop
	playerShop = 13 if pickedHouse > 6 else 6
	opponentShop = 6 if pickedHouse > 6 else 13

	index = pickedHouse
	seeds = house[pickedHouse]
	house[index] = 0
	while seeds > 0:
		index = (index + 1) % 14
		if index == opponentShop: continue
		house[index] += 1
		seeds -= 1

	if index == playerShop: return True

	if house[index] == 1 and house[12 - index] != 0 and (playerShop - 6) <= index < playerShop:
		house[playerShop] += house[12 - index] + 1
		house[index] = house[12 - index] = 0
	return False


def FinalScoring(house):
	for i in range(6):
		house[6] += house[i]
		house[13] += house[7 + i]
		house[i] = house[7 + i] = 0


def Evaluate(house, player1, player2):
	return house[player1] - house[player2]


def HasSuccessors(house):
	player1 = False
	player2 = False
	for i in range(6):
		if house[i] != 0:
			player1 = True
		if house[7 + i] != 0:
			player2 = True
	return player1 and player2
