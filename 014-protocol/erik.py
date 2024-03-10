# extraherar abcdefgh från EMNIST byclass.
# extraherar 0123456789 från EMNIST byclass.

def extract(filename):
	with open(filename + '.csv') as f: lines = f.readlines()

	letters = []
	digits = []
	for line in lines:
		line = line.split(',')
		cells = [item for item in line]
		facit = int(cells[0])
		cells = cells[1:]
		if facit in range(36,44):
			letters.append(str(facit-36) + "," + ",".join(cells))
		if facit in range(10):
			digits.append(str(facit-0) + "," + ",".join(cells))

	with open(filename + '-abcdefgh.csv',   'w') as g: g.writelines(letters)
	with open(filename + '-0123456789.csv', 'w') as g: g.writelines(digits)

	print(filename,len(lines),'=>',len(letters),'letters')
	print(filename,len(lines),'=>',len(digits), 'digits')

extract('MNIST/emnist-byclass-test')
extract('MNIST/emnist-byclass-train')
