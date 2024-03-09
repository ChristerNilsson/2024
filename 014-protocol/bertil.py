import cv2

# 28x28 facit.txt => digits.csv letters.csv

DIR = "e2e4/"

SIZE = 28

in_file      = 'data/' + DIR + f'{SIZE}x{SIZE}.jpg' # IN
facit_file   = 'data/' + DIR + 'facit.txt' # IN

digits_file  = 'data/' + DIR + 'digits.csv' # OUT
letters_file = 'data/' + DIR + 'letters.csv' # OUT

image = cv2.imread(in_file)
with open(facit_file) as f:
	facit = [line.strip() for line in f.readlines()]

height, width = image.shape[:2]

lines = []
digits = []
letters = []
LETTERPOS = [0,2,5,7]

freqDigits = {}
freqLetters = {}
for drag in range(len(facit)):
	coloff = (drag // 20) * 11
	z=99
	for xoff in [0,1,2,3, 5,6,7,8]:
		if xoff >= len(facit[drag]): break
		char = facit[drag][xoff]
		korr = ord(char) - (ord('a') if xoff in LETTERPOS else ord('1'))
		arr = [str(korr + 1)]
		if xoff in LETTERPOS:
			freqLetters[char] = freqLetters[char] + 1 if char in freqLetters else 1
		else:
			freqDigits[char] = freqDigits[char] + 1 if char in freqDigits else 1

		# for x in range(1,29):
		# 	for y in range(1,29):
		# 		pixel_value = image[(drag % 20) * 30 + y, (coloff + xoff + 1) * 30 + x][0]  # y,x
		# 		if x in [1,28] or y in [1,28]: pixel_value = 255
		# 		pixel_value = 255 - pixel_value
		# 		# pixel_value = 255 if pixel_value > 75 else 0
		# 		# if pixel_value < 50: pixel_value = 0
		# 		arr.append(str(pixel_value))

		for x in range(SIZE):
			for y in range(SIZE):
				pixel_value = image[(drag % 20) * SIZE + y, (coloff + xoff + 1) * SIZE + x][0]  # y,x
				if x in [0,1,26,27] or y in [0,1,26,27]: pixel_value = 255
				pixel_value = 255 - pixel_value
				# pixel_value = 255 if pixel_value > 75 else 0
				if pixel_value < 50: pixel_value = 0
				arr.append(str(pixel_value))

		if xoff in LETTERPOS:
			letters.append(",".join(arr)+"\n")
		else:
			digits.append(",".join(arr)+"\n")

with open(letters_file,'w') as g: g.writelines(letters)
with open(digits_file,'w') as g: g.writelines(digits)

for char in "abcdefgh": print(char,freqLetters[char])
print()
for char in "12345678": print(char,freqDigits[char])
