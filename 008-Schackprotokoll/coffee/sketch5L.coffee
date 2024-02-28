XN = 84 # size of a square
YN = 84
NY = 20 # number of squares vertically
XO = 1.8 * XN             # X Offset
YO = (2100 - NY * YN) / 2 # Y Offset

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
			@drawTitle @x + XN * [3, 8][i], @y+0.75*YN, ['white','black'][i % 2]

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
		line @x-XN, y, @x + 11 * XN, y


	drawMove : (x,y,txt) ->
		textSize 40
		fill 'black'
		text txt, x, y + 0.1 * YN
		noFill()
		for i in range 11	
			rect x + i * XN, y, XN, YN

	drawTitle : (x,y,color) ->
		fill color
		rect x+1, y - YN, 5 * XN + 2, 0.5*YN

		other = if color == 'black' then 'white' else 'black'
		textSize 32
		y = y - 0.1 * YN

		fill other
		färg = if color == 'black' then 'Svart' else 'Vit'
		text färg, x, y - 0.85 * YN

textCol = (txt,x,y,w,h,count) ->
	fill 'black'
	text txt, x, y - 0.3 * YN
	noFill()
	rect x, y + 0.5 * YN, w,h,5
	if count == 2 then rect x, y + 1.6 * YN, w, h, 5

drawForm = ->

	noFill()
	circle XO +  0 * XN, YO-1.2*YN, 0.4*XN
	fill 'black'
	circle XO + 16.5 * XN, YO-1.2*YN, 0.4*XN

	for j in range 2
		for i in range 4
			t = "Namn Klubb Rating Poäng".split(" ")[i]
			x = XO + XN * [3.75, 9.2, 12.65, 15.1][i]
			y = YO - 1.75*YN
			w = XN * [6.5, 4, 2.5, 1.8][i]
			h = YN
			textCol t, x+j*16.5*XN, y, w, h, 1

	for i in range 6
		t = 'Tävling Plats Klass Rond Bord Datum'.split(" ")[i]

		x = XO + XN * [2.5,7.7,10.7,12.4,14.1,17.6][i]
		y = YO + YN * 0.7 + NY*YN
		w = XN * [6, 4, 1.5, 1.5, 1.5, 5][i]
		h = YN
		textCol t, x, y, w, h, 1


window.mouseClicked = -> saveCanvas 'Protocol_5L','jpg'

window.draw = ->
	background 'white'
	strokeWeight 1

	drawForm()

	for i in range 3
		units[i].draw i
