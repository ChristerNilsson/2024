import itertools
from copy import deepcopy

class Player:
	def __init__(self,id,name,rating):
		self.id = id
		self.name = name
		self.rating = rating
		self.score = 0
		self.balance = 0
		self.opposition = []

	def __str__(self):
		return f"id={self.id} score={self.score} rating={self.rating} opp={self.opposition}"

players = []
ratings = list(range(1825,1475,-25))
names = ratings

for i in range(len(ratings)):
	players.append(Player(i+1,names[i], ratings[i]))
z=99

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
	floater = [] # sista i udda grupp flyttas till nästa grupp.
	keys = list(groups.keys())
	keys.sort(reverse=True) # Börja med högsta gruppen
	print(keys)
	for score in keys:
		group = groups[score]
		if len(floater) == 1:
			p0 = floater.pop()
			p1 = group.pop(0)
			result.append(p0)
			result.append(p1)

		n = len(group)
		if n % 2 == 1:
			floater.append(group.pop())
			n -= 1
#		else:
#			floater = []
		g0 = group[0:n//2]
		g1 = group[n//2:n]
		for i in range(n//2):
			p0 = g0[i]
			p1 = g1[i]
			result.append(p0)
			result.append(p1)
	#result.sort(key=lambda p: p.id)
	for p in result:
		print(p)
	print("")
	return result

def ok(p0, p1):
	return p0.id not in p1.opposition

def recurse(i, players, used, result):
	# print('used',i,used)
	n = len(players)
	if i >= n:
		return result
	else:
		if i not in used:
			for j in range(i+1,n):
				if j in used: continue
				if ok(players[i],players[j]):
					p0 = deepcopy(players[i])
					p1 = deepcopy(players[j])
					p0.opposition.append(p1.id)
					p1.opposition.append(p0.id)
					return recurse(i+1, players, used + [i,j], result + [p0,p1])
		return recurse(i+1,players, used, result)

def updateResults(p0,p1):
	if abs(p0.rating - p1.rating) <= 25: # remi
		p0.score += 1
		p1.score += 1
	elif p0.rating > p1.rating: # vinst
		p0.score += 2

for rond in range(5):
	players = lotta(players)
	players = recurse(0,players, [], [])
	for i in range(0,len(players),2):
		updateResults(players[i], players[i+1])

players.sort(key=lambda p: [-p.score, -p.rating])
#players.sort(key=lambda p: p.id)

for player in players:
	print(player)
