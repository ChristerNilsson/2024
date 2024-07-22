import {swiss_data} from './swiss.js'
import {elo_data} from './elo.js'

range = _.range
print = console.log

t_elo = false
t_swiss = false
t_distance = false
t_gap = false
t_players = false

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

	drawLines : ->
		push()
		stroke 'darkgray'
		for p in @points
			x = p[0]
			# y = p[1]
			line 2450-x, 0, 2450-x, height * 2
			# line 0, 2450-y, width, 2450-y
		pop()

	draw :  ->
		i = 0
		if t_gap
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

	if t_elo or t_swiss or t_distance or t_gap or t_players

		if t_distance
			for i in range -13,13
				stroke 'yellow'
				line 0,0+i*100,1200,1200+i*100
		if t_players then tournaments[0].drawLines()
		if t_swiss then tournaments[0].draw()
		if t_elo then tournaments[1].draw()
	else
		fill 'black'
		noStroke()
		text "e = elo",width/2,100
		text "s = swiss",width/2,200
		text "d = distance",width/2,300
		text "g = gap",width/2,400
		text "p = players",width/2,500

window.keyPressed   = -> 
	if key == 'e' then t_elo = not t_elo
	if key == 's' then t_swiss = not t_swiss
	if key == 'd' then t_distance = not t_distance
	if key == 'g' then t_gap = not t_gap
	if key == 'p' then t_players = not t_players

window.windowResized = -> resizeCanvas windowWidth-4, windowHeight-4
