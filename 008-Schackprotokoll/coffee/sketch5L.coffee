XN = 84 # size of a square
YN = 84
NY = 20 # number of squares vertically
XO = 1.8 * XN             # X Offset
YO = (2100 - NY * YN) / 2 - 12 # Y Offset

range = _.range

units = []

window.setup = ->
	canvas = createCanvas 2970,2100 # A4
	textAlign CENTER,CENTER
	rectMode CENTER
	units.push new Unit XO +  0*XN, YO
	units.push new Unit XO + 11*XN, YO
	units.push new Unit XO + 22*XN, YO

class Unit
	constructor : (@x,@y) ->

	draw : (i) ->
		strokeWeight 1
		for j in range NY
			@drawMove @x , @y + j * YN + 0.5 * YN, NY * i + j + 1

		for i in range 2
			@drawTitle @x + XN * [1, 6][i], @y+0.75*YN, ['white','black'][i % 2]

		for i in range 3 # ver
			strokeWeight [5, 3, 5][i]
			x = @x + [-0.5, 5.5, 10.5][i] * XN
			line x, @y, x , @y + NY * YN

		for i in range 3 # hor
			strokeWeight [5, 3, 5][i]
			y = @y + [0, 10, 20][i] * YN
			line @x-0.5*XN, y, @x + 10.5 * XN, y

		strokeWeight 3 
		y = @y + 10 * YN
		line @x-0.6*XN, y, @x + 10.6 * XN, y

	drawMove : (x,y,txt) ->
		textSize 40
		fill 'black'
		text txt, x, y + 0.1 * YN
		noFill()
		for i in range 11	
			rect x + i * XN, y, XN, YN

	drawTitle : (x,y,color) ->
		fill color
		circle x+1, y - 1.1*YN, 30

textCol = (txt,x,y,w,h,count) ->
	fill 'black'
	text txt, x, y + 1.4 * YN
	noFill()
	rect x, y + 0.5 * YN, w,h,5
	if count == 2 then rect x, y + 1.6 * YN, w, h, 5

drawForm = ->

	noFill()
	circle XO +  1 * XN, YO-1.2*YN, 30
	fill 'black'
	circle XO + 17 * XN, YO-1.2*YN, 30

	for j in range 2
		for i in range 4
			t = "Namn Klubb Rating Poäng".split(" ")[i]
			x = XO + XN * [5, 10.5, 13.5, 15.5][i]
			y = YO - 1.75*YN
			w = XN * [7, 4, 2, 2][i]
			h = YN
			textCol t, x+j*16*XN, y, w, h, 1

	for i in range 6
		t = 'Tävling Plats Klass Rond Bord Datum'.split(" ")[i]

		x = XO + XN * [2.5,7.5,10.5,12.5,14.5,18][i]
		y = YO + YN + NY*YN - 0.5*YN
		w = XN * [6, 4, 2, 2, 2, 5][i]
		h = YN
		textCol t, x, y, w, h, 1

	fill 'black'
	textSize 20
	text 'Christer Nilsson 070 - 749 6800', 2740, 1900


window.mouseClicked = -> saveCanvas 'Protocol_5L','jpg'

window.draw = ->
	background 'white'
	strokeWeight 1

	drawForm()

	for i in range 3
		units[i].draw i
