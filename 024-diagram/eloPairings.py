ALFABET = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def invert(arr):
	newArr = [0] * len(arr)
	for i in range(len(arr)):
		newArr[arr[i]] = i
	return newArr

def memberSchack(title,filename,PLAYERS,ROUNDS):
	# rounds = []
	# for r in range(ROUNDS): rounds.append([])
	with open(filename,encoding='utf8') as f:
		players = {}
		elos = {}
		for player in range(PLAYERS):
			line = f.readline().strip()
			arr=line.split('\t')
			id = int(arr[0])
			if arr[6]=='0': arr[6]='1400'
			elos[id] = int(arr[6])
			print(line)
			ids = []
			results = []
			for i in range(ROUNDS):
				line = f.readline().strip()
				if line=='F':
					ids.append(0)
					results.append(f.readline().strip())
				else:
					ids.append(int(line))
					results.append(f.readline().replace('w','').strip())
			players[id]=[ids,results]
			line = f.readline().strip()

		for i in range(1,PLAYERS+1):
			ids,results = players[i]
			summa = 0
			for r in range(ROUNDS):
				res = results[r]
				if res=='1': summa += elos[ids[r]]
				if res=='½': summa += elos[ids[r]] * 0.5
			print(i, elos[i], ids,results,summa)


		# for i in range(81):
		# 	print(ids[i])
			# id = ids[i]
			# result = results[i]
			# print(i,id,result)
			# print(ids,results)
			# elif tabs == 2:
			# 	continue
			# elif tabs == 0:
			# 	counter += 1
			# 	if counter % 2 == 1:
			# 		if line != 'F':
			# 			item = int(line)
			# 			rounds[counter//2].append([id, item])

	# arr = [[elos[i], i] for i in range(len(elos))]
	# #arr.sort()
	# #arr.reverse()
	# for i in range(len(arr)):
	# 	print(i+1,arr[i][0])
	#
	# inv = [b for a, b in arr]
	# inv = invert(inv)
	#
	# nyaronder = []
	# for rond in rounds:
	# 	nyrond = []
	# 	for [a,b] in rond:
	# 		# a = inv[a-1][0]
	# 		# b = inv[b-1][0]
	# 		nyrond.append([a,b])
	# 	nyaronder.append(nyrond)
	# rounds = nyaronder

	# dumpCanvas(title,rounds,elos, inv)

# memberSchack('Tyresö Open 2024','Tyresö Open 2024.txt',8)

memberSchack('Senior KM Klass 1','Klass 1.txt',14,13)
