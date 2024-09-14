range = _.range
echo = console.log

bg = 'green'

abcd = []
figures = []
answers = []
facit = 0 

points = []
points.push [10,10]
points.push [50,10]
points.push [90,10]
points.push [10,50]
points.push [50,50]
points.push [90,50]
points.push [10,90]
points.push [50,90]
points.push [90,90]

corners = []
corners.push [0,3,4]
corners.push [0,1,4]
corners.push [1,2,4]
corners.push [2,4,5]
corners.push [4,5,8]
corners.push [4,7,8]
corners.push [4,6,7]
corners.push [3,4,6]

newProblem = ->
	figures = []
	for i in range 9
		figures.push _.sample range 255

	abcd = [0,0,0,0,0,0,0,0,0]
	abcd[0] = figures[0]
	abcd[1] = figures[1]
	abcd[3] = figures[2]
	abcd[4] = figures[3]

	abcd[2] = abcd[0] ^ abcd[1]
	abcd[5] = abcd[3] ^ abcd[4]
	abcd[6] = abcd[0] ^ abcd[3]
	abcd[7] = abcd[1] ^ abcd[4]
	abcd[8] = abcd[2] ^ abcd[5] # the questionmark

	answers = []
	answers.push figures[4]
	answers.push figures[5]
	answers.push figures[6]
	answers.push figures[7]
	answers.push figures[8]
	answers.push abcd[8]

	answers = _.shuffle answers
	facit = answers.indexOf abcd[8]

buttons = []
buttons.push [50,400]
buttons.push [150,400]
buttons.push [250,400]
buttons.push [50,500]
buttons.push [150,500]
buttons.push [250,500]

window.setup = ->
	createCanvas 400,650
	textAlign CENTER,CENTER
	textSize 48
	newProblem()

tri = (i,j,k) -> triangle points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]

show = (pattern) ->
	for ix in range 8
		corner = corners[ix]
		bit = 1 << ix
		if pattern & bit then tri corner[0],corner[1],corner[2]

window.draw = ->
	background bg
	stroke 'black'
	for i in range 4
		line 50,50+i*100,350,50+i*100
		line 50+i*100,350,50+i*100,50

	stroke 'white'
	for i in range 3
		for j in range 3
			push()
			translate 50+i*100,50+j*100
			if i==2 and j==2
				stroke 'black'
				text '?',50,50
			else
				show abcd[3*i+j]
			pop()

	translate 0,350

	stroke 'black'
	for i in range 3
		line 50,50+i*100,350,50+i*100
	for i in range 4
		line 50+i*100,250,50+i*100,50

	stroke 'white'
	for i in range 3
		for j in range 2
			push()
			translate 50+i*100,50+j*100
			show answers[2*i+j]
			pop()

window.mousePressed = ->
	for i in range 6
		[x,y] = buttons[i]
		if x < mouseX < x+100 and y < mouseY < y+100
			bg = if facit == i then 'green' else 'red'
			newProblem()