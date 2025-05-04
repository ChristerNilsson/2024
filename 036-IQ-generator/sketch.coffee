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
unit = 0 

newProblem = ->
	nr = (nr+1) % problems.length
	odd = _.sample [false,true]
	n = problems[nr].length # 5,12 eller 8
	while true
		figures =  _.sampleSize range(1 << n), 9

		abcd = [0,0,0,0,0,0,0,0,0]
		abcd[0] = figures[0]
		abcd[1] = figures[1]
		abcd[3] = figures[2]
		abcd[4] = figures[3]

		x = if odd then 2 ** n - 1 else 0
		echo x

		abcd[2] = abcd[0] ^ abcd[1] ^ x
		abcd[5] = abcd[3] ^ abcd[4] ^ x
		abcd[6] = abcd[0] ^ abcd[3] ^ x
		abcd[7] = abcd[1] ^ abcd[4] ^ x
		abcd[8] = abcd[2] ^ abcd[5] ^ x # the secret questionmark

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

show = (pattern) ->
	fill 'white'

	if nr==0 then strokeWeight 3
	else strokeWeight 1

	for ix in range problems[nr].length
		if pattern & (1 << ix) then problems[nr][ix]()

window.setup = ->
	createCanvas innerWidth-5,innerHeight-5
	unit = height/6.5
	for i in [3.7*unit,4.7*unit]
		for j in [0.5*unit,1.5*unit,2.5*unit]
			buttons.push [j,i]
	makeProblems()
	textAlign CENTER,CENTER
	textSize 48
	newProblem()

draw = ->
	background bg
	stroke 'black'
	xs = [0.5*unit,1.5*unit,2.5*unit,3.5*unit]
	ys = [1.5*unit,2.5*unit,3.5*unit]
	for i in range 4
		line xs[0],xs[i],xs[3],xs[i]
		line xs[i],xs[0],xs[i],xs[3]

	stroke 'white'
	for i in range 3
		for j in range 3
			push()
			translate (i+0.5)*unit,(j+0.5)*unit
			if i==2 and j==2
				stroke 'black'
				text '?',unit/2,unit/2
			else
				show abcd[3*i+j]
			pop()
	
	noStroke()
	fill 'yellow'
	text "#{correct} of #{correct+wrong}",2*unit,0.3*unit
	text round((new Date()-start)/1000,1)+"s",2*unit,3.8*unit
	fill 'white'

	push()
	translate 0,2.5*unit

	stroke 'black'
	for i in range 3
		line xs[0],ys[i],xs[3],ys[i]
	for i in range 4
		line xs[i],ys[0],xs[i],ys[2]

	stroke 'white'
	for i in range 3
		for j in range 2
			push()
			translate xs[i],ys[j]
			show answers[i+3*j]
			pop()
	pop()

window.mousePressed = ->
	if pressed then return
	pressed = true
	for i in range buttons.length
		[x,y] = buttons[i]
		if x < mouseX < x+unit and y < mouseY < y+unit
			if facit == i
				bg = 'green'
				correct += 1
			else 
				bg = 'red'
				wrong += 1
			newProblem()

window.mouseReleased = -> pressed = false 

makeProblems = ->

	points = []
	for i in [0.1*unit,0.5*unit,0.9*unit]
		for j in [0.1*unit,0.5*unit,0.9*unit]
			points.push [j,i]

	tri = (i,j,k) ->
		a = points[i]
		b = points[j]
		c = points[k]
		triangle a[0],a[1],b[0],b[1],c[0],c[1]

	problems.push [
		-> circle 0.5*unit,0.3*unit,5
		-> circle 0.25*unit,0.5*unit,5
		-> circle 0.7*unit,0.5*unit,5
		-> circle 0.5*unit,0.7*unit,5

		-> line 0.1*unit,0.5*unit,0.5*unit,0.5*unit
		-> line 0.5*unit,0.5*unit,0.9*unit,0.5*unit
		-> line 0.5*unit,0.1*unit,0.5*unit,0.5*unit
		-> line 0.5*unit,0.5*unit,0.5*unit,0.9*unit

		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 0 * HALF_PI, 1 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 1 * HALF_PI, 2 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 2 * HALF_PI, 3 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 3 * HALF_PI, 4 * HALF_PI
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
		-> circle 0.5*unit,0.5*unit,0.5*unit
		-> circle 0.3*unit,0.7*unit,0.5*unit
		-> circle 0.7*unit,0.3*unit,0.5*unit
		-> circle 0.3*unit,0.3*unit,0.5*unit
		-> circle 0.7*unit,0.7*unit,0.5*unit
	]

