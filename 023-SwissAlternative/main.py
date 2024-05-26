import itertools
from copy import deepcopy
import time

UTSKRIFT = False

# Denna swisslottning är inte identisk med FIDE:s.

# Metod:
# Sortera spelarna fallande på poäng och rating.
# Gruppera på poäng.
# För varje grupp:
#   Hämta eventuell sinker från föregående grupp.
#   Halvera gruppen. Vid udda antal blir den sista en sinker till nästa grupp.
#   Para ihop de två halvgrupperna typ blixtlås.
# Låt vanlig backtrackande Monrad hantera resten.

class Player:
	def __init__(self,id,name,rating):
		self.id = id
		self.name = name
		self.rating = rating
		self.score = 0
		self.bal = 0
		self.opp = []
		self.colors = ""

	def __str__(self):
		return f"id={self.id} score={self.score} rating={self.rating} opp={self.opp} col={self.colors} bal={self.bal}"

players = []
ratings = list(range(1825,1475,-25))
# ratings = [2245,2108,2004,1996,1985,1980,1979,1974,1973,1956,1954,1938,1934,1890,1889,1882,1851,1849,1849,1842,1838,1825,1803,1801,1798,1773,1754,1734,1693,1677,1663,1599,1585,1572,1539,1531,1472,1465,1400,1400] # rapid
names = ratings
N = len(ratings)

for i in range(len(ratings)):
	players.append(Player(i+1, names[i], ratings[i]))

def gruppera(players):
	hash = {}
	players.sort(key=lambda p: [-p.score,-p.rating])

	for player in players:
		key = player.score
		if key not in hash: hash[key] = []
		hash[key].append(player)
	return hash

def lotta(players):
	groups = gruppera(players)
	result = []
	sinker = [] # sista i udda grupp flyttas till nästa grupp.
	keys = list(groups.keys())
	keys.sort(reverse=True) # Börja med högsta gruppen
	if UTSKRIFT: print('Grupper:',keys)
	for score in keys:
		group = groups[score]
		if len(sinker) == 1:
			p0 = sinker.pop()
			p1 = group.pop(0)
			result.append(p0)
			result.append(p1)

		n = len(group)
		if n % 2 == 1:
			sinker.append(group.pop())
			n -= 1
		g0 = group[0:n//2]
		g1 = group[n//2:n]
		for i in range(n//2):
			p0 = g0[i]
			p1 = g1[i]
			result.append(p0)
			result.append(p1)
	#result.sort(key=lambda p: p.id)
	if UTSKRIFT:
		for p in result:
			print(p)
		print("")
	return result

def ok(p0, p1): return p0.id not in p1.opposition and abs(p0.bal + p1.bal) <= 1
def other(col): return 'w' if col == 'b' else 'b'
def balans(col): return 1 if col == 'w' else -1

def flip(p0,p1):
	col0 = p0.colors[-1]
	col1 = col0
	col0 = other(col0)
	p0.colors += col0
	p1.colors += col1
	p0.bal += balans(col0)
	p1.bal += balans(col1)

def assignColors(p0,p1):
	if len(p0.colors) == 0:
		col1 = "bw"[p0.id % 2]
		col0 = other(col1) # "bw"[1 - p0.id % 2]
		p0.colors += col0
		p1.colors += col1
		bal = 1 if col0 == 'w' else -1
		p0.bal += bal
		p1.bal -= bal
	else:
		bal = p0.bal + p1.bal
		if bal == 0:
			flip(p0,p1)
		elif abs(bal) == 2:
			if abs(p0.bal) == 2:
				flip(p0,p1)
			else:
				flip(p1,p0)
		else:
			print('TODO')

def metBefore(a,b): return b.id in a.opp

def pair(persons, pairing=[]):
	if len(pairing) == N:
		for i in range(0,len(pairing),2):
			p1 = pairing[i]
			p2 = pairing[i+1]
			p1.opp.append(p2.id)
			p2.opp.append(p1.id)
			assignColors(p1,p2)
		return pairing
	a = persons[0]
	ids = [p.id for p in pairing]
	for b in persons:
		if a == b: continue # man kan inte möta sig själv
		if metBefore(a,b): continue # a och b får ej ha mötts tidigare
		if a.id in ids: continue
		if b.id in ids: continue
		bal = abs(a.bal + b.bal)
		if bal >= 1: continue # Spelarna kan inte ha samma färg.

		newPersons = [p for p in persons if p not in [a,b]]
		newPairing = pairing + [a,b]
		result = pair(newPersons,newPairing)
		if len(result) == N: return result
	return []

def updateResults(p0,p1):
	if abs(p0.rating - p1.rating) <= 25: # remi
		p0.score += 1
		p1.score += 1
	elif p0.rating > p1.rating: # vinst
		p0.score += 2
	elif p1.rating > p0.rating: # vinst
		p1.score += 2

# def updateResultsRapid(p0, p1):
# 	remis = [[12,32],[11,21],[16,35]] #,[14,34]]
# 	losers = [[10,12],[19,29]]
# 	if [p0.id,p1.id] in remis or [p1.id,p0.id] in remis:
# 		p0.score += 1
# 		p1.score += 1
# 	elif [p0.id, p1.id] in losers or [p1.id, p0.id] in losers:
# 		if p0.ratings < p1.ratings: p0.score += 2
# 		if p1.ratings < p0.ratings: p1.score += 2
# 	elif p0.rating > p1.rating:  # vinst
# 		p0.score += 2
# 	elif p1.rating > p0.rating:  # vinst
# 		p1.score += 2

start = time.time_ns()
for rond in range(5):
	players = lotta(players)
	players = pair(players)
	for i in range(0,len(players),2):
		updateResults(players[i], players[i+1])
	players.sort(key=lambda p: [-p.score, -p.rating])
#players.sort(key=lambda p: p.id)
print('cpu:',(time.time_ns() - start)/10**6)

print("Resultat", len(players))
for player in players:
	print(player)
