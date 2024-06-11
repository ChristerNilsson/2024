import subprocess
import random

class Player:

	def __init__ (self,original):
		self.original = original
	def __str__(self):
		return f"{self.id}"

	def unpack(self):
		n = 0
		s = self.original
		while len(s) != n:
			n = len(s)
			s = s.replace('   ', '  ')
		player = s.split('  ')
		self.opponents = []
		self.colors = ''
		self.scores = []
		self.score = 0
		self.bal = 0
		for rond in range(7, len(player)):
			arr = player[rond].split(' ')
			self.opponents.append(int(arr[0]))
			self.colors += arr[1]
			self.scores.append(arr[2])
			self.score += "0=1".index(arr[2])/2
		print(self.opponents, self.colors, self.scores,self.score)

	def update(self,o,c,r):
		self.opponents.append(o)
		self.colors += c
		self.scores.append("0=1"[r])
		self.score += r/2

	def write(self):
		res = self.original[0:72]
		res += str(self.score).rjust(11,' ')
		res += "0".rjust(6,' ')
		for i in range(len(self.opponents)):
			res += f"{self.opponents[i]} {self.colors[i]} {self.scores[i]}".rjust(10, ' ')
		return res


def ok (p0, p1) : return p0.id != p1.id and p0.id not in p1.opponents and abs(p0.bal + p1.bal) <= 1 # eller 2
N = 7

def pair (persons,pairing=[]):
	if len(pairing) == N: return pairing
	a  = persons[0]
	for b in persons:
		if not ok(a,b): continue
		newPersons = [p for p in persons if p not in [a,b]]
		if len(pairing) % 2== 0:
			newPairing = pairing + [[a,b]]
		else:
			newPairing = pairing + [[b, a]]
		result = pair(newPersons,newPairing)
		if len(result) == N: return result
	return []

def createMonrad(players,filename):
	pairs = pair(players)
	with open(filename,'w') as g:
		g.write(f"7\n")
		for a,b in pairs:
			g.write(f"{a.id} {b.id}\n")


def call_program(command):
	try:
		result = subprocess.run(command, capture_output=True, text=True, check=True)
		print("Return code for", command[1], ':', result.returncode)

		# return result.stdout, result.stderr, result.returncode
	except subprocess.CalledProcessError as e:
		print(f"Program failed with exit code {e.returncode}")
		print("Error output:", e.stderr)

call_program(["xxx.bat","klass1_6"])

players = []

for rond in range(1,2):

	with open(f"klass1/{rond}.trfx") as f:
		s = f.read().split('\n')
		for s in s[1:15]:
			players.append(Player(s))
		for i in range(len(players)):
			players[i].id = i+1

	for player in players:
		player.unpack()

	createMonrad(players, f"klass1/monrad_{rond}.txt")
	#
	# with open(f"klass1/{rond}.txt") as f:
	# 	pairs = f.read().split('\n')
	# 	pairs = pairs[1:8]
	# 	arrs = []
	# 	for pair in pairs:
	# 		arrs.append([int(x) for x in pair.split(' ')])
	# 	pairs = arrs
	#
	# for player in players:
	# 	player.unpack()
	#
	# for white,black in pairs:
	# 	result = random.choice([0,1,2])
	# 	print(white,black,result,len(players))
	# 	players[white-1].update(black,'w',result)
	# 	players[black-1].update(white,'b',2-result)
	# 	print(players[white-1])
	# 	print(players[black-1])
	#
	# with open(f"klass1/{rond + 1}.trfx",'w') as g:
	# 	for player in players:
	# 		g.write(player.write()+'\n')
	# 	g.write('XXR 9\n')

	# skapa dutch_1.txt


	# Läs .trfx och .txt
	# Skapa nästa trfx fil
	# call_program(["xxx.bat","klass1_2"])
	# call_program(["xxx.bat","klass1_3"])
	# call_program(["xxx.bat","klass1_4"])
	# call_program(["xxx.bat","klass1_5"])
	# call_program(["xxx.bat","klass1_6"])

