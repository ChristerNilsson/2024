range = _.range
echo = console.log
pressed = false

start = new Date()

bg = 'green'

abcd = []
figures = []
answers = []
facit = 0 

correct = 0
wrong = 0

problems = []
nr = 0

newProblem = ->
	while true
		nr = _.sample range problems.length
		figures =  _.sampleSize range(1 << problems[nr].length), 9

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

		answers = _.uniq answers

		answers = _.shuffle answers
		facit = answers.indexOf abcd[8]
		if answers.length == 6 then break

	draw()

buttons = []
buttons.push [50,400]
buttons.push [150,400]
buttons.push [250,400]
buttons.push [50,500]
buttons.push [150,500]
buttons.push [250,500]

show = (pattern) ->
	fill 'white'

	if nr==0 then strokeWeight 3
	else strokeWeight 1

	for ix in range problems[nr].length
		if pattern & (1 << ix) then problems[nr][ix]()

window.setup = ->
	createCanvas 400,650
	textAlign CENTER,CENTER
	textSize 48
	newProblem()

draw = ->
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
	
	noStroke()
	fill 'yellow'
	text "#{correct} of #{correct+wrong}",200,30
	text round((new Date()-start)/1000,1),200,630
	fill 'white'

	push()
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
			show answers[i+3*j]
			pop()
	pop()

window.mousePressed = ->
	if pressed then return
	pressed = true
	for i in range 6
		[x,y] = buttons[i]
		if x < mouseX < x+100 and y < mouseY < y+100
			if facit == i
				bg = 'green'
				correct += 1
			else 
				bg = 'red'
				wrong += 1
			newProblem()

window.mouseReleased = -> pressed = false 

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

tri = (i,j,k) ->
	a = points[i]
	b = points[j]
	c = points[k]
	triangle a[0],a[1],b[0],b[1],c[0],c[1]

problems.push [
	-> circle 50,30,5
	-> circle 70,50,5
	-> circle 50,70,5
	-> circle 30,50,5

	-> line 50,50,50,10
	-> line 50,50,90,50
	-> line 50,50,50,90
	-> line 50,50,10,50

	-> noFill(); arc 50, 50, 80, 80, 0, HALF_PI
	-> noFill(); arc 50, 50, 80, 80, HALF_PI, PI
	-> noFill(); arc 50, 50, 80, 80, PI, PI + HALF_PI
	-> noFill(); arc 50, 50, 80, 80, PI + HALF_PI, PI + PI
]

problems.push [
	-> tri 0,3,4
	-> tri 0,1,4
	-> tri 1,2,4
	-> tri 2,4,5
	-> tri 4,5,8
	-> tri 4,7,8
	-> tri 4,6,7
	-> tri 3,4,6
]

problems.push [
	-> circle 50,50,40
	-> circle 30,70,40
	-> circle 70,30,40
	-> circle 30,30,40
	-> circle 70,70,40
]
