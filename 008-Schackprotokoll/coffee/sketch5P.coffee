XN = 82 # size of a square
YN = 82
NY = 30 # number of squares vertically
XO = 65 + 1.5 * XN  # X Offset
YO = 200 - 0.5 * YN # Y Offset

range = _.range

window.setup = ->
	canvas = createCanvas 2100,2970 # A4
	textAlign CENTER,CENTER
	rectMode CENTER

drawMove = (x,y,txt) ->
	textSize 40
	fill 'black'
	text txt, x, y + 0.1 * YN
	noFill()
	for i in range 11	
		rect x + i * XN, y, XN, YN

drawTitle = (x,y,color) ->
	fill color
	rect x+1, y - YN, 5 * XN + 2, YN

	other = if color == 'black' then 'white' else 'black'
	textSize 32
	y = y - 0.1 * YN

	fill other
	färg = if color == 'black' then 'Svart' else 'Vit'
	text färg, x, y - 0.8 * YN

textCol = (txt,x,y,w,h,count) ->
	fill 'black'
	text txt, x, y - 0.3 * YN
	noFill()
	rect x, y + 0.5 * YN, w,h,5
	if count == 2 then rect x, y + 1.6 * YN, w, h, 5

drawForm = ->

	for i in range 4
		t = "Namn Klubb Rating Poäng".split(" ")[i]
		x = XO + XN * [5.2, 13.2, 18.2, 20.5][i]
		y = YO + YN * (NY+0.2)
		w = XN * [8.5, 7, 2.5, 1.6][i]
		h = YN
		textCol t, x, y, w, h, 2

	for i in range 6
		t = 'Tävling Plats Klass Rond Bord Datum'.split(" ")[i]
		x = XO + XN * [2.5, 7.7, 11.4, 14.1, 16.3,19.5][i]
		y = YO + YN * (NY+3)
		w = XN * [6, 4, 3, 2, 2, 4][i]
		h = YN
		textCol t, x, y, w, YN, 1

	fill 'black'
	text 'Vit:',   XO + 0.25*XN, YO + (NY+0.7) * YN
	text 'Svart:', XO + 0.25*XN, YO + (NY+1.7) * YN

window.mouseClicked = ->
	saveCanvas 'adam','jpg'

window.draw = ->
	background 'white'
	strokeWeight 1

	for i in range 4
		x = XO + XN * [3, 8, 14, 19][i]
		drawTitle x, YO, ['white','black'][i % 2]

	drawForm()

	for i in range 2
		for j in range NY
			drawMove XO + i * 11 * XN, YO + j * YN, NY * i + j + 1

	for i in range 5 # ver
		strokeWeight [5, 3, 5, 3, 5][i]
		x = XO + [-0.5, 5.5, 10.5, 16.5, 21.5][i] * XN
		line x, YO - YN / 2, x , YO + NY * YN - YN / 2

	for i in range 5 # hor
		strokeWeight [5, 3, 5, 3, 5][i]
		y = YO + [0, 10, 20, 30, 40][i] * YN - YN/2
		line XO - 0.5 * XN, y, XO + 21.5 * XN, y