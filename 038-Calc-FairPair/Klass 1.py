# scores skiljer sig från points för spelare 10,11 och 12
# beroende på att man använt sig av inbördes möte vid särskiljningen dem emellan
# scores: 11,12,10

# Seniorserien VT 2024 Klass 1
# https://member.schack.se/ShowTournamentServlet?id=13627&listingtype=2

# Output:
# 1 12.0 19331.5
# 2 11.0 18015.5
# 3 10.0 15983.5
# 4 9.0 14302.5
# 5 8.0 12925.5
# 6 6.5 10316.0
# 7 6.0 9654.0
# 8 5.5 8800.5
# 9 5.0 7755.5
# 10 4.5 7100.5
# 11 4.5 7369.0
# 12 4.5 7162.5
# 13 3.0 4692.5
# 14 1.5 2452.0

N = 14

elos = [1825,1697,1938,1598,1561,1644,1681,1684,1583,1559,1539,1598,1535,1532]

oppss = []
oppss.append('8 9 13 6 5 10 2 4 14 3 11 7 12')
oppss.append('3 11 7 12 8 9 1 6 5 10 13 4 14')
oppss.append('2 4 14 13 11 7 12 8 9 1 6 5 10')
oppss.append('14 3 11 7 12 8 9 1 6 5 10 2 13')
oppss.append('7 12 8 9 1 6 13 10 2 4 14 3 11')
oppss.append('12 8 9 1 13 5 10 2 4 14 3 11 7')
oppss.append('5 10 2 4 14 3 11 13 12 8 9 1 6')
oppss.append('1 6 5 10 2 4 14 3 11 7 12 13 9')
oppss.append('13 1 6 5 10 2 4 14 3 11 7 12 8')
oppss.append('11 7 12 8 9 1 6 5 13 2 4 14 3')
oppss.append('10 2 4 14 3 13 7 12 8 9 1 6 5')
oppss.append('6 5 10 2 4 14 3 11 7 13 8 9 1')
oppss.append('9 14 1 3 6 11 5 7 10 12 2 8 4')
oppss.append('4 13 3 11 7 12 8 9 1 6 5 10 2')

oppss = [[int(opp) for opp in opps.split(' ')] for opps in oppss]

res = []
res.append('111111r11r111')
res.append('1r1r11r1r1111')
res.append('01111r111rrr1')
res.append('101111r0r1101')
res.append('11r00r11r01r1')
res.append('r0101rr0r1r10')
res.append('0100rr0110101')
res.append('01rr00r001rr1')
res.append('100110r10r000')
res.append('101r00r0r0010')
res.append('0r0r00111r000')
res.append('r00r010001r10')
res.append('01000100r00r0')
res.append('000rr0r000000')

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
