def dutch_pairing(players):
	"""
	Parar ihop spelare enligt Dutch-systemet.
	Varje spelare representeras som en dictionary med nycklarna:
	- 'id': unikt ID för spelaren
	- 'rating': spelarens rating
	- 'color': antal gånger spelaren spelat med vit respektive svart
	- 'score': spelarens aktuella poäng
	- 'opponents': lista av spelare (ID) som spelaren redan mött
	"""

	def pair_group(group):
		"""
		Para ihop spelare i en given grupp.
		"""
		if len(group) < 2:
			return []

		# Dela gruppen i två halvor
		mid = len(group) // 2
		top_half = group[:mid]
		bottom_half = group[mid:]

		pairs = []
		used = set()

		for i in range(len(top_half)):
			for j in range(len(bottom_half)):
				if top_half[i]['id'] not in bottom_half[j]['opponents'] and bottom_half[j]['id'] not in used:
					pairs.append((top_half[i], bottom_half[j]))
					used.add(bottom_half[j]['id'])
					break

		return pairs

	def recursive_pairing(players):
		"""
		Rekursiv funktion som parar ihop spelare baserat på deras poäng.
		"""
		if len(players) < 2:
			return []

		# Sortera spelarna först efter poäng, sedan efter rating
		players.sort(key=lambda x: (-x['score'], -x['rating']))

		# Skapa poänggrupper
		score_groups = {}
		for player in players:
			score_groups.setdefault(player['score'], []).append(player)

		all_pairs = []

		for group in score_groups.values():
			pairs = pair_group(group)
			all_pairs.extend(pairs)

		return all_pairs

	return recursive_pairing(players)


# Exempelanvändning
players = [
	{'id': 1, 'rating': 2400, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 2, 'rating': 2300, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 3, 'rating': 2200, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 4, 'rating': 2100, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 5, 'rating': 2000, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 6, 'rating': 1900, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 7, 'rating': 1800, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
	{'id': 8, 'rating': 1700, 'color': {'white': 0, 'black': 0}, 'score': 0, 'opponents': []},
]

players = [
	{'id': 1, 'rating': 2400, 'color': {'white': 1, 'black': 0}, 'score': 1, 'opponents': [5]},
	{'id': 2, 'rating': 2300, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [6]},
	{'id': 3, 'rating': 2200, 'color': {'white': 1, 'black': 0}, 'score': 1, 'opponents': [7]},
	{'id': 4, 'rating': 2100, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [8]},
	{'id': 5, 'rating': 2000, 'color': {'white': 0, 'black': 1}, 'score': 0, 'opponents': [1]},
	{'id': 6, 'rating': 1900, 'color': {'white': 1, 'black': 0}, 'score': 0, 'opponents': [2]},
	{'id': 7, 'rating': 1800, 'color': {'white': 0, 'black': 1}, 'score': 0, 'opponents': [3]},
	{'id': 8, 'rating': 1700, 'color': {'white': 1, 'black': 0}, 'score': 0, 'opponents': [4]},
]

players = [
	{'id': 1, 'rating': 2400, 'color': {'white': 1, 'black': 0}, 'score': 2, 'opponents': [5,3]},
	{'id': 2, 'rating': 2300, 'color': {'white': 0, 'black': 1}, 'score': 2, 'opponents': [6,4]},
	{'id': 3, 'rating': 2200, 'color': {'white': 1, 'black': 0}, 'score': 1, 'opponents': [7,1]},
	{'id': 4, 'rating': 2100, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [8,2]},
	{'id': 5, 'rating': 2000, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [1,7]},
	{'id': 6, 'rating': 1900, 'color': {'white': 1, 'black': 0}, 'score': 1, 'opponents': [2,8]},
	{'id': 7, 'rating': 1800, 'color': {'white': 0, 'black': 1}, 'score': 0, 'opponents': [3,5]},
	{'id': 8, 'rating': 1700, 'color': {'white': 1, 'black': 0}, 'score': 0, 'opponents': [4,6]},
]

players = [
	{'id': 1, 'rating': 2400, 'color': {'white': 1, 'black': 0}, 'score': 3, 'opponents': [5,3,2]},
	{'id': 2, 'rating': 2300, 'color': {'white': 0, 'black': 1}, 'score': 2, 'opponents': [6,4,1]},
	{'id': 3, 'rating': 2200, 'color': {'white': 1, 'black': 0}, 'score': 2, 'opponents': [7,1,5]},
	{'id': 4, 'rating': 2100, 'color': {'white': 0, 'black': 1}, 'score': 2, 'opponents': [8,2,6]},
	{'id': 5, 'rating': 2000, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [1,7,3]},
	{'id': 6, 'rating': 1900, 'color': {'white': 1, 'black': 0}, 'score': 1, 'opponents': [2,8,4]},
	{'id': 7, 'rating': 1800, 'color': {'white': 0, 'black': 1}, 'score': 1, 'opponents': [3,5,8]},
	{'id': 8, 'rating': 1700, 'color': {'white': 1, 'black': 0}, 'score': 0, 'opponents': [4,6,7]},
]

pairs = dutch_pairing(players)
for pair in pairs:
	print(f"Player {pair[0]['id']} vs Player {pair[1]['id']}")
