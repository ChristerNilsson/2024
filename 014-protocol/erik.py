#filename = 'MNIST/emnist-mnist-test'
filename = 'data/e2e4/digits'

with open(filename + '.csv') as f:
	lines = f.readlines()

output = []
for line in lines:
	line = line.split(',')
	cells = [item for item in line]
	facit = cells[0]
	cells = cells[1:]
	matrix = [[cells[i*28+j] for i in range(28)] for j in range(28)]

	for i in range(28):
		for j in range(28):
			if i < j: continue
			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

	output.append(facit + "," + ",".join([matrix[j][i] for i in range(28) for j in range(28)]))

with open(filename + '-transposed.csv', 'w') as g:
	g.writelines(output)




