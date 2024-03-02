# Detta program användes när man ska kalibrera fyra hörn
# Avläs koordinaterna med F12

img = null
points = []

# 0 1
# 3 2
games = {}
games.S5254_1 = {white:"Thomas Paulin", black:"Christer Nilsson", result:"1-0", corners: "136 241 3321 247 3322 2165 134 2163", klass:4, rond:5 }
games.e2e4_1 = {white:"Thomas Paulin", black:"Christer Nilsson", result:"1-0", corners: "138 241 3323 248 3321 2169 132 2162", klass:4, rond:5 }

preload = -> img = loadImage 'data/5254.jpg'
#preload = -> img = loadImage 'data/e2e4.jpg'

setup = ->
	createCanvas img.width, img.height
	noFill()
	fill 0
	strokeWeight 1
	textSize 44
	textAlign LEFT,TOP
	rectMode CENTER

draw = ->
	image img, 0,0
	fill 0
	stroke "white"
	# circle mouseX,mouseY,R
	rect mouseX-10,mouseY-10, 20,3
	rect mouseX-10,mouseY-10, 3,20
	# fill "white"
	point mouseX+10,mouseY+10
	fill "black"
	text points.length,mouseX+30,mouseY+30
	stroke 'red'
	fill 'red'

	corners = games.S5254_1.corners.split " "
	# corners = games.e2e4_1.corners.split " "
	
	[x0,y0,x1,y1,x2,y2,x3,y3] = corners
	line x0,y0,x1,y1
	line x1,y1,x2,y2
	line x2,y2,x3,y3
	line x3,y3,x0,y0

mousePressed = ->
	points.push "#{round(mouseX-10)} #{round(mouseY-10)}"
	if points.length == 4 
		console.log points.join " "
