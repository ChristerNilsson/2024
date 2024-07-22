import {swiss_data} from './swiss.js'
import {elo_data} from './elo.js'

range = _.range
print = console.log

[ELO,SWISS,DISTANCE,GAP,X,Y] = [1,2,4,8,16,32]

t_active = 0

tournaments = []

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
		@title += " avg=" + @average.toFixed 0

	drawX : ->
		push()
		stroke 'darkgray'
		for p in @points
			x = p[0]
			line 2450-x, 0, 2450-x, height * 2
		pop()

	drawY : ->
		push()
		stroke 'darkgray'
		for p in @points
			x = p[0]
			line 0, 2450-x, width*2, 2450-x
		pop()

	draw :  ->
		i = 0
		if t_active & GAP
			push()
			stroke 'black'
			strokeWeight sqrt(2) * @average
			line 0,0,1200,1200
			strokeWeight 1
			stroke 'white'
			line 0,0,1200,1200
			pop()

		fill @color
		stroke 'black'
		text @title, 950, @y0
		for [x,y] in @points
			size = 2 * sqrt abs x-y
			circle 2450-x, 2450-y, 2 + size
			xm = mouseX / (height/1100)
			ym = mouseY / (height/1100)
			if x-size/2 < 2450-xm < x+size/2 and y-size/2 < 2450-ym < y+size/2 
				push()
				fill 'black'
				text "#{x} vs #{y} => #{abs x-y}", 950, 150 + 50*i
				i += 1
				pop()

window.setup = -> 
	createCanvas windowWidth-4,windowHeight-4
	rectMode CENTER
	textAlign CENTER,CENTER
	textSize 32
	tournaments.push new Tournament "Swiss Pairing",[255,0,0,128], 100, swiss_data
	tournaments.push new Tournament "ELO Pairing",  [0,255,0,128],  50, elo_data

window.draw = ->
	background 'gray'
	scale height/1100

	if t_active 

		if t_active & DISTANCE
			for i in range -13,13
				stroke 'yellow'
				line 0,0+i*100,1200,1200+i*100
		if t_active & X       then tournaments[0].drawX()
		if t_active & Y       then tournaments[0].drawY()
		if t_active & SWISS   then tournaments[0].draw()
		if t_active & ELO     then tournaments[1].draw()
	else
		fill 'black'
		noStroke()
		text "e = elo",       width/2,100
		text "s = swiss",     width/2,200
		text "d = distance",  width/2,300
		text "g = gap",       width/2,400
		text "x = players x", width/2,500
		text "y = players y", width/2,600

window.mousePressed = -> t_active = 0

window.keyPressed = -> 
	if key == 'e' then t_active ^= ELO
	if key == 's' then t_active ^= SWISS
	if key == 'd' then t_active ^= DISTANCE
	if key == 'g' then t_active ^= GAP
	if key == 'x' then t_active ^= X
	if key == 'y' then t_active ^= Y

window.windowResized = -> resizeCanvas windowWidth-4, windowHeight-4
