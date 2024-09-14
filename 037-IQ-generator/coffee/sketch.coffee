BITS = 12

range = _.range
echo = console.log

bg = 'green'

abcd = []
figures = []
answers = []
facit = 0 

correct = 0
wrong = 0
start = new Date()

pressed = false

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

newProblem = ->
	figures = []
	for i in range 9
		figures.push _.sample range 2 ** BITS

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

	draw()

buttons = []
buttons.push [50,400]
buttons.push [150,400]
buttons.push [250,400]
buttons.push [50,500]
buttons.push [150,500]
buttons.push [250,500]

#### specialized for this problem
drawbit = (i) ->
	strokeWeight 3
	fill 'white'
	if i==0 then circle 50,30,5
	if i==1 then circle 70,50,5
	if i==2 then circle 50,70,5
	if i==3 then circle 30,50,5

	if i==4 then line 50,50,50,10
	if i==5 then line 50,50,90,50
	if i==6 then line 50,50,50,90
	if i==7 then line 50,50,10,50

	noFill()
	if i== 8 then arc 50, 50, 80, 80, 0, HALF_PI
	if i== 9 then arc 50, 50, 80, 80, HALF_PI, PI
	if i==10 then arc 50, 50, 80, 80, PI, PI + HALF_PI
	if i==11 then arc 50, 50, 80, 80, PI + HALF_PI, PI + PI
####

window.setup = ->
	createCanvas 400,650
	textAlign CENTER,CENTER
	textSize 48
	newProblem()

show = (pattern) ->
	for ix in range BITS
		if pattern & (1 << ix) then drawbit ix

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