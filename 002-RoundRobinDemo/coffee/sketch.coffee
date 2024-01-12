range = _.range
print = console.log

players = []
factor = 0
rond = 0

names = "Adam Bert Carl Dan Erik Fred Gert Hans Ivar Jarl Klas Lars Mats Nils Olof Per".split ' '

xs = [100,200,300,400,400,300,200,100,100,200,300,400,400,300,200,100]
ys = [100,100,100,100,500,500,500,500,400,400,400,400,200,200,200,200]

places = [] # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P
places.push [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15]
places.push [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15, 0]
places.push [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14, 0, 1,15]
places.push [ 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15, 1, 2, 0]
places.push [ 4, 5, 6, 7, 8, 9,10,11,12,13,14, 0, 1, 2, 3,15]
places.push [ 5, 6, 7, 8, 9,10,11,12,13,14,15, 1, 2, 3, 4, 0]
places.push [ 6, 7, 8, 9,10,11,12,13,14, 0, 1, 2, 3, 4, 5,15]
places.push [ 7, 8, 9,10,11,12,13,14,15, 1, 2, 3, 4, 5, 6, 0]
places.push [ 8, 9,10,11,12,13,14, 0, 1, 2, 3, 4, 5, 6, 7,15]
places.push [ 9,10,11,12,13,14,15, 1, 2, 3, 4, 5, 6, 7, 8, 0]
places.push [10,11,12,13,14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,15]
places.push [11,12,13,14,15, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 0]
places.push [12,13,14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,15]
places.push [13,14,15, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12, 0]
places.push [14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,15]

class Player
	constructor : (@name,@index) ->
		@index1 = @index
	draw : ->
		x = (1-factor/100)*xs[@index] + factor/100*xs[@index1]
		y = (1-factor/100)*ys[@index] + factor/100*ys[@index1]
		if factor == 100 then @index = @index1
		fill 'yellow'
		circle x,y,50
		fill 'black'
		text @name,x,y+2

window.setup = -> 
	createCanvas 500,600
	rectMode CENTER
	textAlign CENTER,CENTER
	for i in range names.length
		players.push new Player names[i], i


window.draw = ->
	background 'gray'
	textSize 30
	text 'Rond ' + rond,250,300
	for i in range 4
		t = i+1
		for j in range 2
			fill ['white','black'][(i+j)%2]
			rect (i+1)*100,(j+1)*100,100,100
			rect (i+1)*100,(j+4)*100,100,100
		fill 'red'
		text t+0,(i+1)*100,150+2
		text 9-t,(i+1)*100,450+2
	if factor < 100 then factor += 1
	for player in players
		textSize 16
		player.draw()

window.mousePressed = ->
	n = players.length
	rond = (rond+1) % (n-1)
	for i in range n
		players[i].index1 = places[rond][i]
	factor = 0 
