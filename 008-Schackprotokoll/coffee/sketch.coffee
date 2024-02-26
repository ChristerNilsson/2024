N = 64
NY = 40
XO = 120 # X Offset
YO = 200-N # Y Offset

# Array.prototype.clear = -> @length = 0

window.setup = ->
	canvas = createCanvas 2100,2970
	textAlign CENTER,CENTER
	rectMode CENTER
	strokeCap SQUARE

drawMove = (x,y,txt) ->
	textSize 40
	for i in range 15		
		fill if i in [2,3,6,7,9,10,13,14] then "#eee" else "#fff"		
		rect x+i*N,y,N,N
		if i==0 then fill 'black' else noFill()
		text txt,x+i*N,y+0.1*N

drawTitle = (x,y,color) ->
	fill 'black'
	textSize 32
	y = y - 0.1*N

	text color,x+3*N,y-N
	text 'KQR',x,y-N/2
	text 'BN',x,y
	text 'a-h',x+1*N,y
	text 'from',x+1.5*N,y-N/2
	text '1-8',x+2*N,y
	text 'x',x+3*N,y

	text 'QR',x+4*N,y-N/2
	text 'BN',x+4*N,y
	text 'a-h',x+5*N,y
	text 'to',x+5.5*N,y-N/2
	text '1-8',x+6*N,y

textCol = (txt,x,y,w,h,count) ->
	fill 'black'
	text txt,x,y-0.2*N
	noFill()
	rect x,y+0.5*N,w,h
	if count==2 then rect x,y+1.5*N,w,h

drawForm = ->
	textCol 'Name',  XO+6.7*N,YO + NY*N+0.2*N, 700,N,2
	textCol 'Club',  XO+17.3*N,YO + NY*N+0.2*N, 600,N,2
	textCol 'Rating',XO+25*N,YO + NY*N+0.2*N, 200,N,2
	textCol 'Result',XO+28.5*N,YO + NY*N+0.2*N, 100,N,2

	textCol 'Competiton',XO+2*N, YO + NY*N+3*N, 5*N,N,1
	textCol 'Location',  XO+7*N,YO + NY*N+3*N, 5*N,N,1
	textCol 'Date',      XO+12*N,  YO + NY*N+3*N, 5*N,N,1
	textCol 'Series',    XO+17*N,YO + NY*N+3*N, 5*N,N,1
	textCol 'Round',     XO+22*N,YO + NY*N+3*N, 5*N,N,1
	textCol 'Table',     XO+27*N,YO + NY*N+3*N, 5*N,N,1

	fill 'black'
	text 'White:',XO,YO + NY*N + 0.7*N
	text 'Black:',XO,YO + NY*N + 1.7*N



window.mouseClicked = ->
	saveCanvas 'adam','jpg'

window.draw = ->
	background 'white'
	strokeWeight 1 #100/height
	noFill()

	for i in range 4
		x = [0,7*N,15*N,22*N][i]
		drawTitle XO+N+x, YO-0.7*N,['White','Black'][i%2]

	drawForm()

	for i in range 2
		for j in range NY
			drawMove XO+i*15*N, YO+j*N,NY*i+j+1

	strokeWeight 3
	line XO+7.5*N,YO-N/2,XO+7.5*N,YO+NY*N-N//2
	line XO+22.5*N,YO-N/2,XO+22.5*N,YO+NY*N-N//2
	strokeWeight 5
	line XO+14.5*N,YO-N/2,XO+14.5*N,YO+NY*N-N//2

