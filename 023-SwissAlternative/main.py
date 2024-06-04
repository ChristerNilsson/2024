import time
import math

UTSKRIFT = False

class Player:
	def __init__(self,id,name,rating):
		self.id = id
		self.name = name
		self.rating = rating
		self.score = 0
		self.bal = 0
		self.opp = []
		self.col = ""
		self.res = ""

	def __str__(self):
		return f"rating={self.rating} col={self.col} res={self.res} bal={self.bal} opp={self.opp} id={self.id} score={self.score/10}" # sameness={self.sameness()}"

	def calc(self):
		sp = 0
		key = self.col[-1] + self.res[-1]
		self.score += {'w1': 10-sp, 'b1': 10, 'w½': 5-sp, 'b½': 5+sp, 'w0': 0, 'b0': sp}[key]

	# def sameness(self):
	# 	res = 0
	# 	for i in self.opp:
	# 		diff = i - self.id
	# 		res += diff*diff
	# 	return math.sqrt(res)

players = []
ratings = list(range(2000,1000,-20))
names = ratings
N = len(ratings)
print(N)

for i in range(len(ratings)):
	players.append(Player(i+1, names[i], ratings[i]))

def gruppera(players):
	hash = {}
	players.sort(key=lambda p: [-p.score,-p.rating])

	for player in players:
		key = player.score
		if key not in hash: hash[key] = []
		hash[key].append(player)
	print(len(hash),list(hash.keys()))
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
			result.append(sinker.pop())
			result.append(group.pop(0))
		n = len(group)
		if n % 2 == 1:
			sinker.append(group.pop())
			n -= 1
		g0 = group[0:n//2]
		g1 = group[n//2:n]
		for i in range(n//2):
			result.append(g0[i])
			result.append(g1[i])
	#result.sort(key=lambda p: p.id)
	if True or UTSKRIFT:
		for p in result:
			print(p)
		print("")
	return result

def ok(p0, p1): return p0.id != p1.id and p0.id not in p1.opp and abs(p0.bal + p1.bal) <= 2 # eller 2
def other(col): return 'w' if col == 'b' else 'b'
def balans(col): return 1 if col == 'w' else -1

def flip(p0,p1): # p0 byter färg, p0 anpassar sig
	col0 = p0.col[-1]
	col1 = col0
	col0 = other(col0)
	p0.col += col0
	p1.col += col1
	p0.bal += balans(col0)
	p1.bal += balans(col1)

def assignColors(p0,p1):
	if len(p0.col) == 0:
		col1 = "bw"[p0.id % 2]
		col0 = other(col1)
		p0.col += col0
		p1.col += col1
		p0.bal += balans(col0)
		p1.bal += balans(col1)
	else:
		bal = p0.bal + p1.bal
		if bal == 0:
			flip(p0,p1)
		elif abs(bal) == 2:
			if abs(p0.bal) == 2:
				flip(p0,p1)
			else:
				flip(p1,p0)

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
		if a.id in ids: continue
		if b.id in ids: continue
		if not ok(a,b): continue

		newPersons = [p for p in persons if p not in [a,b]]
		newPairing = pairing + [a,b]
		result = pair(newPersons,newPairing)
		if len(result) == N: return result
	return []

def updateResults(p0,p1):
	if abs(p0.rating - p1.rating) <= 25: # remi
		p0.res += '½'
		p1.res += '½'
	elif p0.rating > p1.rating: # vinst
		p0.res += '1'
		p1.res += '0'
	elif p1.rating > p0.rating: # vinst
		p0.res += '0'
		p1.res += '1'

start = time.time_ns()
for rond in range(10):
	players = lotta(players)
	players = pair(players)
	for i in range(0,len(players),2):
		updateResults(players[i], players[i+1])
		players[i].calc()
		players[i + 1].calc()
	players.sort(key=lambda p: [-p.score, -p.rating])
	# for player in players:
	# 	print(player)
print('cpu:',(time.time_ns() - start)/10**6)

print("Resultat", len(players))
for player in players:
	print(player)
