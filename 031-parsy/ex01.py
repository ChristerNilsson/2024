from parsy import regex, seq, string
import re

# original från Bertil:
# ^.{8,}?(?P<tz>Z$| ?(?P<sign>\+|-)(?P<hours>[0-9]{2}):?(?P<minutes>[0-9]{2})$

# efter hyfsning:
# \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|(\+|-)\d{2}:\d{2})

# En stor fördel med parsy jmf med regexp är att man inte behöver gruppera för att få ut datat.
# Då kan man istället för ?(?P<sign>\+|-) skriva (\+|-)

def ass(a,b):
	if a!=b:
		print('Ass failed!')
		print('  ',a)
		print('  ',b)

def assOK(a):
	if not a:
		assert(False)

#### parsy ####

def test(re,input): return re.parse(input)

year   = regex(r"\d{4}").map(int)
month  = regex(r"\d{2}").map(int)
day    = regex(r"\d{2}").map(int)

hour   = regex(r"\d{2}").map(int)
minute = regex(r"\d{2}").map(int)
second = regex(r"\d{2}").map(int)

dash  = string("-")
colon = string(":")
T     = string("T")
Z     = string("Z")
plus  = string("+")
minus = string("-")

datum = seq(year, dash, month, dash, day)
klockslag = seq(hour, colon, minute, colon, second)
offset = Z | seq(plus, hour, colon, minute) | seq(minus, hour, colon, minute)

fulldate = seq(datum, T, klockslag, offset)

ass(test(fulldate, "2024-08-24T12:34:56Z")      , [[2024, '-', 8, '-', 24], 'T', [12, ':', 34, ':', 56], 'Z'])
ass(test(fulldate, "2024-08-24T12:34:56+02:00") , [[2024, '-', 8, '-', 24], 'T', [12, ':', 34, ':', 56], ['+', 2, ':', 0]])
ass(test(fulldate, "2024-08-24T12:34:56-05:30") , [[2024, '-', 8, '-', 24], 'T', [12, ':', 34, ':', 56], ['-', 5, ':', 30]])

#### Regexp ####

years   = "\d{4}"
months  = "\d{2}"
days    = "\d{2}"

hours   = "\d{2}"
minutes = "\d{2}"
seconds = "\d{2}"

def alts(a,b): return f"({a}|{b})"
sign = alts('\+','-')

offset = alts('Z', sign + hours + ':' + minutes)

rex = f"{years}-{months}-{days}T{hours}:{minutes}:{seconds}{offset}"
assert rex == "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|(\+|-)\d{2}:\d{2})"

assOK(re.search(rex, "2024-08-24T12:34:56Z"))
assOK(re.search(rex, "2024-08-24T12:34:56+02:00"))
assOK(re.search(rex, "2024-08-24T12:34:56-05:30"))
