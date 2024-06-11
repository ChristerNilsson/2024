class Player:
	def __init__(self, id, rating, points, opponents):
		self.id = id
		self.rating = rating
		self.points = points
		self.opponents = opponents
	def __str__(self):
		return str(self.id)


def group_players_by_points(players):
	points_dict = {}
	for player in players:
		if player.points not in points_dict:
			points_dict[player.points] = []
		points_dict[player.points].append(player)
	return points_dict


def split_group(group):
	half = len(group) // 2
	return group[:half], group[half:]


def pair_players_within_group(group):
	pairs = []
	floaters = []
	if len(group) % 2 != 0:
		floaters.append(group.pop())

	for i in range(0, len(group), 2):
		pairs.append((group[i], group[i + 1]))

	return pairs, floaters

def pair_groups(upper_half,lower_half):
	n = len(upper_half)
	pairs = []
	for i in range(n):
		pairs.append((upper_half[i],lower_half[i]))
	return pairs

def pair_players_dutch(players):
	if len(players) <= 1:
		return [], players

	points_dict = group_players_by_points(players)

	all_pairs = []
	remaining_floaters = []

	for points in sorted(points_dict.keys(), reverse=True):
		group = points_dict[points]
		upper_half, lower_half = split_group(group)
		pairs = pair_groups(upper_half,lower_half)
		#pairs_upper, floaters_upper = pair_players_within_group(upper_half)
		#pairs_lower, floaters_lower = pair_players_within_group(lower_half)

		all_pairs.extend(pairs)
		# all_pairs.extend(pairs_lower)

		# remaining_floaters.extend(floaters_upper)
		# remaining_floaters.extend(floaters_lower)

	# Recursively pair floaters with remaining players
	floater_pairs, remaining_floaters = pair_players_dutch(remaining_floaters)
	all_pairs.extend(floater_pairs)

	return all_pairs, remaining_floaters


# Example usage:
players = [
	Player(1, 1500, 0, []),
	Player(2, 1400, 0, []),
	Player(3, 1550, 0, []),
	Player(4, 1300, 0, []),
	Player(5, 1600, 0, []),
	Player(6, 1350, 0, []),
	Player(7, 1300, 0, []),
	Player(8, 1250, 0, []),
]
players = [
	Player(1, 1500, 1, [5]),
	Player(2, 1400, 1, [6]),
	Player(3, 1550, 1, [7]),
	Player(4, 1300, 1, [8]),
	Player(5, 1600, 0, [1]),
	Player(6, 1350, 0, [2]),
	Player(7, 1300, 0, [3]),
	Player(8, 1250, 0, [4]),
]
players = [
	Player(1, 1500, 2, [5,3]),
	Player(2, 1400, 2, [6,4]),
	Player(3, 1550, 1, [7,1]),
	Player(4, 1300, 1, [8,2]),
	Player(5, 1600, 1, [1,7]),
	Player(6, 1350, 1, [2,8]),
	Player(7, 1300, 0, [3,5]),
	Player(8, 1250, 0, [4,6]),
]
players = [
	Player(1, 1500, 3, [5,3,2]),
	Player(2, 1400, 2, [6,4,1]),
	Player(3, 1550, 2, [7,1,5]),
	Player(4, 1300, 2, [8,2,6]),
	Player(5, 1600, 1, [1,7,3]),
	Player(6, 1350, 1, [2,8,4]),
	Player(7, 1300, 1, [3,5,8]),
	Player(8, 1250, 0, [4,6,7]),
]
players = [
	Player(1, 1500, 4, [5,3,2,4]),
	Player(2, 1400, 3, [6,4,1,3]),
	Player(3, 1550, 2, [7,1,5,2]),
	Player(4, 1300, 2, [8,2,6,1]),
	Player(5, 1600, 2, [1,7,3,8]),
	Player(6, 1350, 2, [2,8,4,7]),
	Player(7, 1300, 1, [3,5,8,6]),
	Player(8, 1250, 0, [4,6,7,5]),
]
players = [
	Player(1, 1500, 5, [5,3,2,4,6]),
	Player(2, 1400, 4, [6,4,1,3,5]),
	Player(3, 1550, 3, [7,1,5,2,8]),
	Player(4, 1300, 3, [8,2,6,1,7]),
	Player(5, 1600, 2, [1,7,3,8,2]),
	Player(6, 1350, 2, [2,8,4,7,1]),
	Player(7, 1300, 1, [3,5,8,6,4]),
	Player(8, 1250, 0, [4,6,7,5,3]),
]

pairs, floaters = pair_players_dutch(players)

for p1, p2 in pairs:
	print(f"Pair: Player {p1.id} vs Player {p2.id}")

for floater in floaters:
	print(f"Floater: Player {floater.id}")
