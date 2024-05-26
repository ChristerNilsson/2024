import math

# Swiss ger stort ratingavstånd
# Berger ger mindre
# Lichess ger minst

def inflate(lst):
	res = []
	for item in lst:
		res.append(0.6 * item + 800)
	return res

blixt = [1844,1892,1773,1794,1730,1731,1861,1655,1878] # 2024-05-08 (2.5 av 9)
tyresö = [1886,1769,1795,1783,1523,1624,1688] # 2024-05-03 (600:-) (2 av 7)
wasa = [1564,1463,1546,1419,1301] # 2024 VT (2 av 7)
klass3 = inflate([1271,1260,1325,1227,1314,1339,1315,1316,1273,1266,1222])
klass4 = inflate([1201,1142,1019,1049,1084]) # 2024 VT (4 av 5)
lichess = [1502,1547,1446,1430,1517,1481,1533,1523,1544,1529]

def sd(lst,avg):
	sum2 = 0
	for item in lst:
		sum2 += (item-avg) * (item-avg)
	return math.sqrt(sum2 / len(lst))

def execute(myRating,lst):
	sum3 = 0
	n = len(lst)
	summa = sum(lst)
	avg = summa/n
	for item in lst:
		sum3 += abs(item-myRating)

	return [int(summa/n), int(sd(lst,avg)),int(sum3/n)]

print(execute(1539,blixt))
print(execute(1575,tyresö))
print(execute(1539,wasa))
print(execute(1575,klass3))
print(execute(1539,klass4))
print(execute(1500,lichess))