range = _.range

tolerances = [1,2,5,10] # %
cT = 'brown red gold silver'.split ' '
colors = 'SILVER GOLD BLACK BROWN RED ORANGE YELLOW GREEN BLUE VIOLET LIGHTGREY WHITE'.split ' '
multipliers = [0.01,0.1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
mm = "x0.01 x0.1 x1 x10 x100 x1K x10K x100K x1M x10M x100M x1G".split ' '

band = 0
first = 1
secon = 2
multiplier = 1
tolerance = 2

bPos = [88,108,120,142]
y = 37

fillRect = (x,y,w,h,col) ->
	fill col
	rect x,y,w,h

fillCircle = (x,y) ->
	fill 'WHITE'
	circle x,y,4

drawCircle = (x,y,col) ->
	fill col
	circle x,y,8

drawString = (txt,x,y) -> text txt,x-1,y+9

pretty = (x,diff) ->
	units = "ohm K M G".split ' '
	dekad = Math.floor Math.log10(x) / 3
	if dekad < 0 then dekad = 0
	unit = " " + units[dekad]
	[round((x-diff)/1000**dekad,2)+unit,round(x/1000**dekad,2)+unit,round((x+diff)/1000**dekad,2)+unit]

window.setup = ->
	createCanvas 240,137
	noStroke()
	rectMode CENTER

drawResistor = ->
	push()
	fill 'white'
	xm = (bPos[0]+bPos[3])/2
	textAlign CENTER,CENTER
	drawString "Resistor CALC",xm,5
	rect xm,y,100,2
	circle bPos[0],y,26
	rect xm,y,32,15
	circle bPos[3],y,26
	fillRect bPos[0],y,6,25, colors[first+2]
	fillRect bPos[1],y,6,14, colors[secon+2]
	fillRect bPos[2],y,6,14, colors[multiplier]
	fillRect bPos[3],y,6,25, cT[tolerance]
	fillCircle bPos[band],58
	pop()

window.draw = ->

	background 'black'
	fill 'white'

	drawResistor()

	for i in range 12
		if i < 10
			fillRect 8,6+i*13,11,13,colors[i+2]
			fillRect 22+5,6+i*13,11,13,colors[i+2]

			col = if i in [0,6] then 'WHITE' else 'BLACK'
			fill col
			drawString i, 5,i*13+2
			drawString i,25,i*13+2
			fill 'WHITE'

		col = if i == 0 then 'WHITE' else colors[i]
		drawCircle 235, i*11+9, col
		fill 'WHITE'
		drawString mm[i],194, i*11+4

	fillCircle 17, first*13 + 5
	fillCircle 36, secon*13 + 5
	fillCircle 188, multiplier*11 + 9

	for i in range 4 # tolerance
		fillRect 62 + i*34,117+6,34,12,cT[i]
		fill 'BLACK'
		drawString tolerances[i] + "%",54+(i*34),119

	fillCircle 61+tolerance*34,133
	fill 'WHITE'

	res = (first*10+secon) * multipliers[multiplier]
	diff = res * tolerances[tolerance]/100.00
	[minn,value,maxx] = pretty res,diff
	fill 'WHITE'

	drawString "#{first}#{secon} x 10    = #{value}",48,76,2
	drawString multiplier-2,85+2,72
	drawString "Max: " + maxx,48,94-4
	drawString "Min: " + minn,48,106-2

window.keyPressed = ->
	if key == 'ArrowRight' then band = (band + 1) %% cT.length
	if key == 'ArrowLeft' then band = (band - 1) %% cT.length

	delta = 0
	if key == 'ArrowUp' then delta = -1
	if key == 'ArrowDown' then delta = 1
	if band == 0 then first = (first + delta) %% 10
	if band == 1 then secon = (secon + delta) %% 10
	if band == 2 then multiplier = (multiplier + delta) %% multipliers.length
	if band == 3 then tolerance = (tolerance + delta) %% tolerances.length
