import {swiss_data} from './swiss.js'
import {elo_data} from './elo.js'

range = _.range
print = console.log

[ELO,SWISS,DISTANCE,GAP,X,Y,GRID] = [1,2,4,8,16,32,64]

t_active = 0

tournaments = []

states = [0, GRID, GRID+X, GRID+DISTANCE, GRID+SWISS, GRID+SWISS+DISTANCE+GAP, GRID+X+ELO, GRID+X+DISTANCE+ELO+GAP, GRID+X+DISTANCE+SWISS+ELO]
messages = []
messages.push "|"
messages.push "1. Each axis contains elo rating for one player|between 1400 and 2400 elos. Press Space"
messages.push "2. There are 78 players, these are their elos.|Notice the Normal Distribution, more people in the middle."
messages.push "3. The main diagonal represents a gap of zero elos.|The distance step is 100 elos."
messages.push "4. Swiss Pairing with eight rounds. Tyresö Open 2024|Hover the mouse. Where is the largest/smallest gap?"  
messages.push "5. The Gap contains half of the games|"
messages.push "6. ELO Pairing with eight rounds.|"
messages.push "7. Most Elo games have a low Gap.|The top seven and bottom seven players are all meeting each other."
messages.push "8. You seldom meet your Elo neighbours using Swiss|Press one of the letters below or Space!"

state = 0

class Tournament
	constructor : (@title, @color, @y0, @data) ->
		lines = @data.split "\n"	
		@points = []
		total = 0
		for line in lines
			cells = line.split "\t"
			x = parseInt cells[0]
			y = parseInt cells[1]
			if x==1400 or y==1400 then continue
			total += abs x-y
			@points.push [x,y]
		@average = total / @points.length
		@title += " (average elo gap = #{@average.toFixed 0})"

	drawX : ->
		push()
		stroke 'darkgray'
		for p in @points
			x = p[0]
			line x-1350, 50, x-1350, 1050
		pop()

	drawY : ->
		push()
		stroke 'darkgray'
		for p in @points
			x = p[0]
			line 50, 2450-x, 1050, 2450-x
		pop()

	drawGrid : ->
		push()
		fill 'black'
		stroke 'black'
		textAlign CENTER
		for i in range 1400,2500,100
			text i//100,   i-1350,  1080
			text 38-i//100,    20,i-1350
			line 2450-i,     50, 2450-i, 1050
			line     50, 2450-i, 1050,   2450-i
		pop()

	drawGap : ->
		if t_active & GAP
			if t_active & ELO then d = 73
			if t_active & SWISS then d = 155
			push()
			stroke 'black'
			strokeWeight sqrt(2) * @average
			line 1100-d,d,d,1100-d
			strokeWeight 1
			fill 'black'
			rect 50,1050,50+@average,1050-@average
			rect 1050,50,1050-@average,50+@average
			pop()

	drawDistance : ->
		stroke 'yellow'
		for i in range 10
			x0 = 50+i*100
			y1 = i*100+50
			line x0,1050,1050,y1
			line x0,  50,  50,y1

	draw :  ->
		i = 0
		fill @color
		stroke 'black'
		textAlign LEFT
		text @title, 950+150, @y0
		for [x,y] in @points
			size = 2 * sqrt abs x-y
			circle x-1350, 2450-y, 2 + size
			xm = mouseX / (height/1100)
			ym = mouseY / (height/1100)
			if x-size/2 < 1350+xm < x+size/2 and y-size/2 < 2450-ym < y+size/2 
				push()
				fill 'black'
				text "#{x} vs #{y} => #{abs x-y}", 950+150, 50 + @y0 + 50*i
				i += 1
				pop()

window.setup = -> 
	createCanvas windowWidth-4,windowHeight-4
	rectMode CORNERS
	strokeCap SQUARE
	textAlign CENTER,CENTER
	textSize 32
	tournaments.push new Tournament "Swiss Pairing",[255,0,0,128], 50, swiss_data
	tournaments.push new Tournament "ELO Pairing",  [0,255,0,128], 550, elo_data

window.draw = ->
	background 'gray'
	scale height/1100

	if t_active 

		if t_active & GAP 
			if t_active & SWISS then tournaments[0].drawGap()
			if t_active & ELO   then tournaments[1].drawGap()
		if t_active & X         then tournaments[0].drawX()
		if t_active & Y         then tournaments[0].drawY()
		if t_active & GRID      then tournaments[0].drawGrid()
		if t_active & DISTANCE  then tournaments[0].drawDistance()
		if t_active & SWISS     then tournaments[0].draw()
		if t_active & ELO       then tournaments[1].draw()
	else
		fill 'black'
		noStroke()
		text "e = elo",       width/2,100
		text "s = swiss",     width/2,200
		text "d = distance",  width/2,300
		text "g = gap",       width/2,400
		text "x = players x", width/2,500
		text "y = players y", width/2,600
		text "r = grid",      width/2,700
		text "Space = guided tour", width/2,800

	noStroke()
	for i in range 7
		fill if t_active & 2**i then 'white' else 'black'
		text 'esdgxyr'[i],1300+i*20,1080

	push()
	textAlign LEFT
	arr = messages[state].split '|'
	text arr[0],1100,800
	text arr[1],1100,900
	pop()

window.mousePressed = -> t_active = 0

window.keyPressed = -> 
	if key == ' ' 
		state = (state + 1) % states.length
		t_active = states[state]
	if key == 'e' then t_active ^= ELO
	if key == 's' then t_active ^= SWISS
	if key == 'd' then t_active ^= DISTANCE
	if key == 'g' then t_active ^= GAP
	if key == 'x' then t_active ^= X
	if key == 'y' then t_active ^= Y
	if key == 'r' then t_active ^= GRID

window.windowResized = -> resizeCanvas windowWidth-4, windowHeight-4
