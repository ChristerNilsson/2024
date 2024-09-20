# scores skiljer sig från points för spelare 5,6 och 7
# beroende på att man använt sig av inbördes möte vid särskiljningen dem emellan
# scores: 6,5,7

# scores skiljer sig från points för spelare 10 11
# pga annan särskiljning
# scores: 11,10

# Seniorserien VT 2024 Klass 2
# https://member.schack.se/ShowTournamentServlet?id=13628&listingtype=2

# Output:
# 1 9.0 12756.0
# 2 8.5 12095.0
# 3 7.5 10640.0
# 4 6.5 9280.0
# 5 6.0 8484.5
# 6 6.0 8689.5
# 7 6.0 8446.5
# 8 4.5 6366.5
# 9 3.5 4957.0
# 10 3.0 4242.5
# 11 3.0 4257.0
# 12 2.5 3510.5

N = 12

elos = [1685,1498,1454,1458,1453,1397,1400,1381,1385,1403,1390,1412]

oppss = []
oppss.append('9 3 6 11 5 12 8 7 4 10 2')
oppss.append('7 4 10 8 9 3 6 11 5 12 1')
oppss.append('12 1 7 4 10 2 9 8 6 11 5')
oppss.append('10 2 9 3 6 11 5 12 1 7 8')
oppss.append('6 11 8 12 1 7 4 10 2 9 3')
oppss.append('5 12 1 7 4 10 2 9 3 8 11')
oppss.append('2 9 3 6 11 5 12 1 8 4 10')
oppss.append('11 10 5 2 12 9 1 3 7 6 4')
oppss.append('1 7 4 10 2 8 3 6 11 5 12')
oppss.append('4 8 2 9 3 6 11 5 12 1 7')
oppss.append('8 5 12 1 7 4 10 2 9 3 6')
oppss.append('3 6 11 5 8 1 7 4 10 2 9')

oppss = [[int(opp) for opp in opps.split(' ')] for opps in oppss]

res = []
res.append('11011111r1r')
res.append('r1111011r1r')
res.append('101r11rrr1r')
res.append('001r11r1r10')
res.append('101r0rr1rrr')
res.append('01110001rr1')
res.append('r1001r10101')
res.append('r100010r0r1')
res.append('000r00r01r1')
res.append('100r01r0000')
res.append('r11000r0000')
res.append('000r1000100')

def value(ch):
    if ch=='1': return 1
    if ch=='r': return 0.5
    return 0

def getPoints(): return [sum([value(r) for r in p]) for p in res]
def getScore():  return [sum([elos[oppss[i][j]-1] * value(res[i][j]) for j in range(N-1)]) for i in range(N)]

points = getPoints()
scores = getScore()
for i in range(N):
    print(i+1,points[i],scores[i])
