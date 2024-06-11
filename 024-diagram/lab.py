# def berakna_elo_diff(vinnare, forlorare, k=32):
# 	elo_diff = forlorare - vinnare
# 	expected_score = 1 / (1 + 10 ** (elo_diff / 400))
# 	elo_change = k * (1 - expected_score)
# 	return elo_change
#
# for i in range(-500,501,100):
# 	print(i,berakna_elo_diff(1500,1500+i,20))
# print("")
# for i in range(-500, 501, 100):
# 	print(i,berakna_elo_diff(1500+i,1500,20))

import random

def elo_probabilities(R_W, R_B, draw=0.2):
	E_W = 1 / (1 + 10 ** ((R_B - R_W) / 400))
	win = E_W - draw / 2
	loss = (1 - E_W) - draw / 2
	r = random.random()
	if r < loss: return 0
	if r < loss+draw: return 1
	return 2

	return [loss, draw, win]

arr=[0,0,0]
for i in range(1000):
	p = elo_probabilities(1400, 1100)
	arr[p]+=1
print(arr)

