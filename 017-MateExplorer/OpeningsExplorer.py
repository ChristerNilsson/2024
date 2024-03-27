import chess
import chess.pgn
import chess.engine
import time
import io

# todo Skapa båda färgerna samtidigt?

ENGINE = "C:\Program Files\stockfish\stockfish-windows-x86-64-avx2.exe"

MULTIPV = 2  # förgreningsfaktor för motspelaren
MS = 100  # ms

cLines = 0
cNodes = 0
lastRow = []

def run(color,levels,pgn):
	global cLines
	global cNodes
	global lastRow

	cLines = 0
	cNodes = 0
	lastRow = []

	def progress(i):
		return f'({i} of {int(MULTIPV ** (levels // 2))})'

	def pr(s, i=""):
		g.write(s + "\n")
		print(s, i)

	def header():
		höger = f"{color}{MULTIPV} L{levels} {MS}ms"
		n = (levels + 1) * 6 - len(pgn) - len(höger)
		pr(pgn + ' ' * n + höger)

		s = ""
		for i in range(levels):
			if move_number % 2 == 0:
				letter = 'WB'[i % 2]
				s += f"{(move_number + i) // 2}{letter}".ljust(6, " ")
			else:
				letter = 'BW'[i % 2]
				s += f"{(move_number + i + 2) // 2}{letter}".ljust(6, " ")
		pr(s + "    cp")

	def footer():
		pr("")
		pr(f"{cLines} lines and {cNodes} moves in {int((time.time_ns() - start) / 10 ** 9)} s")

	def printa(moves,level,info):
		global cLines
		global lastRow
		output = []
		i = 0
		while i < len(lastRow) and lastRow[i] == moves[i]:
			output.append("|")
			i += 1
		for i in range(i, level):
			s = moves[i]
			output.append(s)

		output = [move.ljust(6, ' ') for move in output]
		pr("".join(output) + str(score(info[0])).rjust(6, " "), progress(cLines))
		cLines += 1
		lastRow = moves

	def analyze(g, moves=[]):
		level = len(moves)
		global cNodes

		if move_number % 2 == 0:
			n = 1 if "WB"[level % 2] == color else MULTIPV
		else:
			n = 1 if "WB"[level % 2] != color else MULTIPV
		info = engine.analyse(board, chess.engine.Limit(time=MS / 1000), multipv=n)

		cNodes += 1

		if level >= levels:
			printa(moves,level,info)
			return

		for move in info:
			pv = move['pv'][0]
			san = board.san(chess.Move.from_uci(pv.uci()))
			board.push(pv)
			analyze(g, moves + [san])
			board.pop()

	game = chess.pgn.read_game(io.StringIO(pgn))
	board = game.board()
	for move in game.mainline_moves():
		board.push(move)

	filename = f"{pgn} {color}{MULTIPV} L{levels} {MS}ms"

	move_number = len(board.move_stack)

	start = time.time_ns()
	with open("openings\\" + filename + ".txt", "w") as g:
		header()
		analyze(g)
		footer()

def score(info):
	value = info['score'].pov(True)
	if type(value) == chess.engine.Cp: return value.cp
	return "#" + str(value.mate())

engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
engine.configure({"Skill Level":20}) # Verkar inte ha någon effekt, 0 ska ge non randomness

run("B", 8, "1.")

# run("B", 9, "1. b3") # Larsen
# run("B", 9, "1. b4")
# run("B", 9, "1. c4") # Engelskt
# run("B", 8, "1. d4 c5") # Benoni
# run("B", 9, "1. e3")
# run("B", 9, "1. e4")
# run("B", 8, "1. e4 d5") # Skandinaviskt
# run("B", 9, "1. h4")

#run("W", 9, "1. e4 c5") # Sicilianskt
# run("W", 8, "1. e4 e5 2. Nf3 Nc6 3. Bc4")
# run("W", 8, "1. e4 e5 2. Nf3 Nc6 3. Bb5") # Spanskt
# run("W", 8, "1. e4 e5 2. Nf3 Nf6") # Ryskt

engine.quit()