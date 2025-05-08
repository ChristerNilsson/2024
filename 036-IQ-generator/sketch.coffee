range = _.range
echo = console.log
pressed = false

start = new Date()

landscape = true

bg = 'grey'

abcd = []
figures = []
answers = []

correct = 0
wrong = 0

expected = -1
actual = -1
feedback = false

problems = []
nr = -1
unit = 0 

newProblem = ->
	feedback = false
	expected = -1
	actual = -1
	nr = (nr+1) % problems.length
	odd = _.sample [false,true]
	n = problems[nr].length # 5,12 eller 8
	while true
		figures = _.sampleSize range(1 << n), 9

		abcd = [0,0,0,0,0,0,0,0,0]
		abcd[0] = figures[0]
		abcd[1] = figures[1]
		abcd[3] = figures[2]
		abcd[4] = figures[3]

		x = if odd then 2 ** n - 1 else 0

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
		
		expected = answers.indexOf abcd[8]
		if answers.length == 6 then break

buttons = []

show = (pattern,i=-1,expected,actual) ->
	stroke 'black'
	if actual == -1 then fill 'white'
	else if expected == i
		fill 'green'
		rect 0,0,unit,unit
	else if actual == i
		fill 'red'
		rect 0,0,unit,unit

	strokeWeight if nr==1 then 1 else 0.03 * unit
	stroke 'white'
	fill 'white'

	for ix in range problems[nr].length
		if pattern & (1 << ix) then problems[nr][ix]()

window.setup = ->
	createCanvas innerWidth-5,innerHeight-5
	unit = width/7.5

	for j in [1*unit,2*unit]
		for i in [4*unit,5*unit,6*unit]
			buttons.push [i,j]
	makeProblems()
	textAlign CENTER,CENTER
	textSize 0.5 * unit
	newProblem()

window.draw = ->
	background 'grey'
	stroke 'black'
	strokeWeight 0.03 * unit

	# Rita 4x4 linjer
	xs = [0.5*unit,1.5*unit,2.5*unit,3.5*unit]
	ys = [1.5*unit,2.5*unit,3.5*unit]
	for i in range 4
		line xs[0],xs[i],xs[3],xs[i]
		line xs[i],xs[0],xs[i],xs[3]

	stroke 'white'

	# Rita 3x3 problem
	for i in range 3
		for j in range 3
			push()
			translate (i+0.5)*unit,(j+0.5)*unit
			if i==2 and j==2
				fill 'white'
				textSize unit
				text '?',unit/2,0.55 * unit
			else
				noStroke()
				show abcd[i+3*j],-1,-1,-1
			pop()
	
	noStroke()
	fill 'yellow'
	text "#{correct} of #{correct+wrong}",5.5*unit,0.7*unit
	text round((new Date()-start)/1000)+"s", 5.5*unit,3.3*unit
	fill 'white'

	# Answers
	push()
	translate 3.5*unit,0

	# Rita 3x4 linjer
	stroke 'black'
	strokeWeight 0.03 * unit
	xs = [0.5*unit,1.5*unit,2.5*unit,3.5*unit]
	ys = [1.0*unit,2.0*unit,3.0*unit]
	for i in range 4
		line xs[i],ys[0],xs[i],ys[2]
	for i in range 3
		line xs[0],ys[i],xs[3],ys[i]

	# Rita 3x2 svar
	stroke 'white'
	for i in range 3
		for j in range 2
			push()
			translate xs[i], ys[j] 
			show answers[i+3*j], i+3*j,expected,actual
			pop()
	pop()

window.mousePressed = ->
	if pressed then return
	pressed = true
	if feedback
		newProblem()
		return
	for i in range buttons.length
		[x,y] = buttons[i]
		if x < mouseX < x+unit and y < mouseY < y+unit
			actual = i
			if expected == actual
				correct += 1
				newProblem()
			else 
				wrong += 1
				feedback = true

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
		-> circle 0.5*unit,0.5*unit,0.5*unit
		-> circle 0.3*unit,0.7*unit,0.5*unit
		-> circle 0.7*unit,0.3*unit,0.5*unit
		-> circle 0.3*unit,0.3*unit,0.5*unit
		-> circle 0.7*unit,0.7*unit,0.5*unit
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
		-> circle 0.5*unit,0.3*unit,9
		-> circle 0.25*unit,0.5*unit,9
		-> circle 0.7*unit,0.5*unit,9
		-> circle 0.5*unit,0.7*unit,9

		-> line 0.1*unit,0.5*unit,0.5*unit,0.5*unit
		-> line 0.5*unit,0.5*unit,0.9*unit,0.5*unit
		-> line 0.5*unit,0.1*unit,0.5*unit,0.5*unit
		-> line 0.5*unit,0.5*unit,0.5*unit,0.9*unit

		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 0 * HALF_PI, 1 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 1 * HALF_PI, 2 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 2 * HALF_PI, 3 * HALF_PI
		-> noFill(); arc 0.5*unit, 0.5*unit, 0.8*unit, 0.8*unit, 3 * HALF_PI, 4 * HALF_PI
	]
