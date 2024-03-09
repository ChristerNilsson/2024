echo = console.log
range = _.range

index = 0 
rader = []
rad = []

SIZE = 20

readCSV = ->
	fileInput = document.getElementById 'csvFileInput'
	file = fileInput.files[0]

	if file
		reader = new FileReader()
		reader.onload = (event) ->
			rader = event.target.result.split '\n'
			rad = readRad index
		reader.readAsText file
	else
		echo 'No file selected'

readRad = (index) -> 
	try
		res = (int(cell) for cell in rader[index].split ',')
		echo res
		return res
	catch
		echo "problem med",index
	return (5 for i in range(785))

setup = ->
	createCanvas 580,580
	noFill()
	textSize 36
	fill 0
	frameRate 10
	textAlign CENTER,CENTER

draw = ->
	background "gray"

	if keyIsDown(LEFT_ARROW)
		index -= 1
		if index < 0 then index = 0
		rad = readRad index

	if keyIsDown(RIGHT_ARROW)
		index += 1
		rad = readRad index

	fill 0
	textSize 10
	if index >= rader.length then return
	for i in range 28
		for j in range 28
			try
				fill rad[1 + 28 * i + j]
			catch 
			ellipse SIZE + SIZE * i, SIZE + SIZE * j, SIZE
			fill 255-rad[1 + 28 * i + j]
			text rad[1 + 28 * i + j], SIZE + SIZE * i, SIZE + SIZE * j
	fill 'yellow'
	text rad[0],5,30
	text str(1 + index // 2) + "WB"[index % 2], 5,70
	text index,width-5,10
