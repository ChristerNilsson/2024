XN = 60
YN = 64
NY = 40
XO = 65    # X Offset
YO = 200-XN # Y Offset

window.setup = ->
	canvas = createCanvas 2100,2970
	textAlign CENTER,CENTER
	rectMode CENTER
	# strokeCap PROJECT

drawMove = (x,y,txt) ->
	textSize 40
	for i in range 17		
		fill if i in [2,3,6,7,10,11,14,15] then "#eee" else "#fff"		
		rect x+i*XN,y,XN,YN
		if i == 0
			fill 'black'
			text txt,x+i*XN,y+0.1*YN

drawTitle = (x,y,color) ->
	fill color
	rect x+3.5*XN,y,8*XN,2.8*YN

	other = if color=='black' then 'white' else 'black'
	textSize 32
	y = y - 0.1*YN

	fill other
	# text color,x+3.5*XN,y-YN
	text 'DT',x,y-YN
	text 'K',x,y-0.5*YN
	text 'LS',x,y
	text 'a-h',x+1*XN,y
	text 'från',x+1.5*XN,y-0.75*YN
	text '1-8',x+2*XN,y
	text 'x',x+3*XN,y

	text 'DT',x+4*XN,y-YN
	text 'LS',x+4*XN,y
	text 'a-h',x+5*XN,y
	text 'till',x+5.5*XN,y-0.75*YN
	text '1-8',x+6*XN,y
	text 'DT',x+7*XN,y-YN
	text '†',x+7*XN,y-0.5*YN
	text 'LS',x+7*XN,y

textCol = (txt,x,y,w,h,count) ->
	fill 'black'
	text txt,x,y-0.3*YN
	noFill()
	rect x,y+0.5*YN,w,h,5
	if count==2 then rect x,y+1.5*YN,w,h,5

drawForm = ->

	for i in range 4
		t = "Namn Klubb Rating Poäng".split(" ")[i]
		x = XO + XN * [7.2,20.6,29.5,32.5][i]
		y = YO + NY * YN + 0.2 * XN
		w = [700,750,200,100][i]
		h = YN
		textCol t,x,y,w,h,2

	for i in range 6
		t = 'Tävling Plats Klass Rond Bord Datum'.split(" ")[i]
		x = XO + XN * [5.3, 13.8, 20.7, 24.6, 27,30.9][i]
		y = YO + NY * YN + YN * 3 
		w = XN * [8.2,8,5,2,2,5][i]
		textCol t,x,y,w,YN,1

	fill 'black'
	text 'Vit:',XO+XN/4,YO + NY*YN + 0.7*YN
	text 'Svart:',XO+XN/4,YO + NY*YN + 1.7*YN

window.mouseClicked = ->
	saveCanvas 'adam','jpg'

window.draw = ->
	background 'white'
	strokeWeight 1 #100/height
	noFill()

	for i in range 4
		x = [0,8*XN,17*XN,25*XN][i]
		drawTitle XO+XN+x, YO-0.7*YN,['white','black'][i%2]

	drawForm()

	for i in range 2
		for j in range NY
			drawMove XO+i*17*XN, YO+j*YN,NY*i+j+1

	for i in range 5
		strokeWeight [5,3,5,3,5][i]
		x = XO + [-0.5,8.5,16.5,25.5,33.5][i] * XN
		line x,YO-YN/2, x,YO+NY*YN-YN//2 # ver

	for i in range 5
		strokeWeight [5,3,5,3,5][i]
		y = YO + [0,10,20,30,40][i] * YN - YN/2
		line XO-0.5*XN,y, XO+33.5*XN,y # hor