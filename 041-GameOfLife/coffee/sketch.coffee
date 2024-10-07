make2DArray = (cols, rows) -> ((floor random 2 for i in [0...rows]) for j in [0...cols])

grid = [[]]
cols = 0
rows = 0
resolution = 5

window.setup = ->
	createCanvas windowWidth-5, windowHeight-5
	cols = width // resolution
	rows = height // resolution
	grid = make2DArray cols,rows

window.draw = ->
	background 0
	for i in [0...cols]
		for j in [0...rows]
			x = i * resolution
			y = j * resolution
			if grid[i][j] == 1 then rect x, y, resolution - 1, resolution - 1

	next = make2DArray cols, rows

	for i in [0...cols]
		for j in [0...rows]
			state = grid[i][j]
			neighbors = countNeighbors grid, i, j

			next[i][j] = state
			if state == 0 && neighbors == 3 then next[i][j] = 1
			if state == 1 && (neighbors < 2 || neighbors > 3) then next[i][j] = 0

	grid = next

countNeighbors = (grid, x, y) ->
	sum = -grid[x][y]
	for i in [-1,0,1]
		for j in [-1,0,1]
			col = (x + i) %% cols
			row = (y + j) %% rows
			sum += grid[col][row]
	sum
