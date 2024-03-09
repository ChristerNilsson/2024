echo = console.log
range = _.range

img = null
ruta = null

row = 0
col = 0

N = 30

preload = ->
	img = loadImage "Te2e4.jpg"
	
setup = ->
	createCanvas img.width,img.height
	noFill()
	textSize 36
	fill 0

	ruta = img.get N*col,N*row,N,N
	ruta.loadPixels()

# facit = """d2d4 g7g6
# c1f4 f8g7
# e2e3 g8f6
# b1d2 e878
# g1f3 d7d6
# f1d3 b7b6
# h2h3 c8b7
# g2g4 f6d5
# f4g3 d5b4
# d3e2 b8d7
# c2c3 b4c6
# h3h4 d7f6
# g4g5 f6d7
# h4h5 e7e6
# h5g6 f7g6
# e3e4 d6d5
# b2b4 d5e4
# d2e4 c6d4
# f3d4 b7e4
# d4e6 g7c3
# e1f1 d8e7
# e6f8 18f8
# a1c1 e4h1
# d1b3 g8h8
# b3c3 e8g8
# c3c7 h1e4
# e2g4 e4f5
# g4e2 f583
# f1e1 f8f5
# c1d1 f5g5
# c7d8 g7f8
# d8g5 f8b4
# d1d2 b4b1
# e2d1 b1e4
# d2e2 e4h1
# e1d2 h1c6
# e2e8 h8g7
# g5e7 g7h6
# g3f4"""

keyPressed = () ->
	if key == 'ArrowRight' then col += 1
	if key == 'ArrowLeft' then col -= 1
	if key == 'ArrowDown' then row += 1
	if key == 'ArrowUp' then row -= 1
	# if key == ' '
	# 	lines = []
	# 	for drag in range 39
	# 	    for ix in [1,6,12,17]
	# 	        letter = facit[drag][ix]
    #             if letter not in "abcdefgh" then continue
    #             row = drag % 20
    #             coloffset = 2 * (drag // 20)
    #             col = ix % 2 + coloffset
    #             index = row * 33 + [1,6,12,17][col]

    #             facitRuta = letter

    #         if facitRuta in "abcdefgh"
    #             ruta = img.get N*col,N*row,N,N
    #             ruta.loadPixels()
    #             rad = [{a:"36", b:"37",c:'38', d:"39",e:"40", f:"41",g:'42', h:"43"}[facitRuta]]
    #             for i in range 1,29
    #                 for j in range 1,29
    #                     index = N * j + i
    #                     rad.push str 255 - ruta.pixels[4*index]
    #             print rad.length
    #             lines.push rad.join(",")
	# 	saveStrings lines,'Te2e4','csv'
	# 	row = 0
	# 	col = 0
	# else
	# fetch 28x28 matrix
	ruta = img.get N*col,N*row,N,N
	ruta.loadPixels()
		# echo ruta.pixels

draw = ->
	background "gray"
	image img,0,0
	fill 'red'
	stroke 'red'

	small = []
	fill 'red'

	xa = round lerp 0,33*N,col/33
	ya = round lerp 0,20*N,row/20
	xb = round lerp 0,33*N,(col+1)/33
	yb = round lerp 0,20*N,(row+1)/20

	line xa,ya,xb,ya
	line xb,ya,xb,yb
	line xa,yb,xb,yb
	line xa,ya,xa,yb

	fill 255
	rect 620,280,280,280

	noStroke()
	if ruta.pixels
		for i in range 28
			for j in range 28
				index = N * j + i
				fill ruta.pixels[4*index]
				circle 620+i*10,280+j*10,10
