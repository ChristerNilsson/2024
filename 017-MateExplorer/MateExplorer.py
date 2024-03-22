import chess
import chess.pgn
import chess.engine
import time

ENGINE = "C:\Program Files\stockfish\stockfish-windows-x86-64-avx2.exe"

MULTIPV = 2
TIME = 100 # ms

engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
engine.configure({"Skill Level":20}) # Verkar inte ha någon effekt, 0 ska ge non randomness

fen = "3r2k1/2pq1rp1/pp5p/4p3/3n1P1P/B1NP1p1b/PPPQ1P1K/R3R2B b - - 0 23"
#fen = "3r2k1/2pq2p1/pp5p/4p3/3nRr1P/B1NP1p1b/PPPQ1P1K/R6B b - - 1 24"
board = chess.Board(fen)
fullmove_number = board.fullmove_number
cLines = 0
cNodes = 0
lastRow = []

def analyze(g,moves=[]):
	level = len(moves)
	global cLines
	global cNodes
	global lastRow
	n = 1 if level % 2 == 0 else MULTIPV
	info = engine.analyse(board, chess.engine.Limit(time=TIME/1000), multipv=MULTIPV)
	if len(info) == 1 and info[0]['depth'] == 0:
		output = []
		i = 0
		while i < len(lastRow) and lastRow[i] == moves[i]:
			output.append("|")
			i += 1
		for i in range(i,len(moves)):
			s = '|' if i < len(lastRow) and lastRow[i] == moves[i] else moves[i]
			output.append(s)

		output = [move.ljust(6,' ') for move in output]
		pr("".join(output))
		cLines += 1
		lastRow = moves
		return
	cNodes += 1

	for move in info:
		if move['depth'] > 0:
			pv = move['pv'][0]
			san = board.san(chess.Move.from_uci(pv.uci()))
			board.push(pv)
			analyze(g,moves + [san])
			board.pop()
		n -= 1
		if n == 0: break

def pr(s):
	g.write(s+"\n")
	print(s)

start = time.time_ns()
with open(f"kampe_{fullmove_number}_{MULTIPV}_{TIME}.txt", "w") as g:
	pr(fen)
	s = ""
	for i in range(20):
		letter = 'B' if i % 2 == 0 else 'W'
		s += f"{(2*fullmove_number + 1 + i)//2}{letter}".ljust(6," ")
	pr(s)
	analyze(g)
	pr("")
	pr(f"{cLines} lines and {cNodes} nodes in {int((time.time_ns()-start)/10**6)} ms")

engine.quit()