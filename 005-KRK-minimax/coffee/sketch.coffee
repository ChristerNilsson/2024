SIZE = 40
YOFFSET = 40

BASE = 'Q' # Hämtas från URL. 

board = null
chess = new Chess()
level = 1 # fullMoves
moveNumber = 0 # chess.moveNumber verkar inte finnas, får räkna själv

range = _.range
echo = console.log

title = null
pgn = null

images = {}

clickedFrom = -1
clickedTo = -1

problemBase = null 

buttons = []

chess2board = ->
    for index in range 64
        sq = chess.board()[7 - index // 8][index % 8]
        board.squares[index].piece = if sq then sq.color + sq.type.toUpperCase() else ''

setStatus = ->
    textSize 18
    fill 'black'
    title = if BASE=='Qr' then "Win in " else "Mate in "
    text title+level, width/2,25
    s = if moveNumber == 0 then "Endbase Exerciser by Christer 2024" else extractLastMove chess.pgn()
    text s,width/2,380

getProblem = (delta) ->
    KkBASE = "Kk" + BASE
    level += delta
    moveNumber = 0
    if level < 1 then level = 1
    if not level in problemBase then level -= 1
    problems = problemBase[level].split ' '
    problem = _.sample problems
    indexes = (problem.slice 2*i,2*i+2 for i in range KkBASE.length)
    chess.clear()
    for i in range KkBASE.length
        letter = KkBASE[i]
        color = if letter in "KQRBNP" then 'w' else 'b'
        chess.put {type:letter.toLowerCase(), color:color}, indexes[i]
        chess2board()
        setStatus()

preload = ->
    if window.location.href.includes "?base=" then BASE = window.location.href.split("=")[1]
    echo BASE
    problemBase = loadJSON "json/#{BASE}.json"
    for letter in "KQRBNP"
        black = 'b'+letter
        white = 'w'+letter
        images[black] = loadImage "img/#{black}.png"
        images[white] = loadImage "img/#{white}.png"

setup = ->
    createCanvas 8*SIZE, 700

    textAlign CENTER,CENTER

    board = new Board()
    title = createDiv()
    title.position 25, 12.5*SIZE
    pgn = createDiv ''
    pgn.position 25, 13*SIZE
    getProblem 0

    buttons.push new Button 'Q',width/2,0,100,40
    buttons.push new Button 'R',width/2,50,100,40
    buttons.push new Button 'Qr',width/2,100,100,40
    buttons.push new Button 'BB',width/2,150,100,40
    buttons.push new Button 'BN',width/2,200,100,40
    buttons.push new Button 'NNN',width/2,250,100,40

class Button
    constructor : (@piece,@x,@y,@w,@h) ->
        @images = []
        for letter in @piece
            color = if letter in "KQRBNP" then 'w' else 'b'
            piece = letter.toUpperCase()
            @images.push images[color + piece]
        @XOFFSET = -20 * @images.length
    draw : ->
        for i in range @images.length
            image @images[i],@XOFFSET+@x+40*i,YOFFSET+360+@y,SIZE,SIZE
            
    inside: (x,y) -> @x < x-@XOFFSET < @x+@w and @y < y-YOFFSET-360 < @y+@h
    click : -> window.location.href = "?base=" + @piece

class Square
    constructor : (@index,@click) ->
        @piece = ""
        @i = @index % 8
        @j = @index // 8
        @x = @i * SIZE
        @y = (7-@j) * SIZE
        @name = "abcdefgh"[@i] + "12345678"[@j]
        # @moving = false
    draw : ->
        fill if (@i+@j) % 2 == 0 then 'gray' else 'yellow'
        rect @x,YOFFSET+@y,SIZE,SIZE

        if clickedFrom != @index #and clickedTo == -1
            if @piece != ''  then image images[@piece],@x,YOFFSET+@y,SIZE,SIZE

    inside: (x,y) -> @x < x < @x+SIZE and @y < y-YOFFSET < @y+SIZE

class Board
    constructor : ->
        @squares = []
        for i in range 64
            @squares.push new Square(i)
    draw : ->
        for square in @squares
            square.draw()
    mousePressed : ->
        for square in board.squares
            if square.inside mouseX,mouseY
                clickedFrom = square.index
                echo 'moving',clickedFrom
    mouseReleased : ->
        # if clickedFrom == -1 then return
        moves = (move.from + move.to for move in chess.moves { verbose: true })
        if moves.length == 0
            getProblem 0
            return
        for square in @squares
            if square.inside mouseX,mouseY
                clickedTo = square.index
                a = @squares[clickedFrom].name
                b = square.name
        if a + b in moves
            chess.move { from: a, to: b }
            moveNumber += 1
            fetchAI()
        clickedFrom = -1

draw = -> 
    background 'green'
    for button in buttons
        button.draw()
    board.draw()
    setStatus()

    if clickedFrom != -1
        square = board.squares[clickedFrom]
        #for square in board.squares
        # echo board.squares[clickedFrom]
        echo square.piece
        image images[square.piece], mouseX-SIZE/2, mouseY-SIZE/2, SIZE,SIZE
#else
#    if @piece != ''  then image images[@piece],@x,YOFFSET+@y,SIZE,SIZE


mousePressed = -> 
    for button in buttons
        if button.inside mouseX, mouseY
            button.click()
            return
    board.mousePressed()
mouseReleased = -> board.mouseReleased()

extractLastMove = (s) ->
    s = s.split("\n").slice(-2).join(' ')
    s.split(' ').slice(-3).join ' '
    
fetchAI = -> 
    fetch 'http://tablebase.lichess.ovh/standard?fen=' + chess.fen()
        .then (response) => 
            if !response.ok then throw new Error 'Network response was not ok'
            return response.json()
        .then (data) =>
            echo data
            if data.category == "draw" then return getProblem -1
            if data.moves.length == 0
                if level < moveNumber
                    return getProblem -1
                else
                    return getProblem +1
            chess.move data.moves[0].san
            chess2board()
            setStatus()
        .catch (error) => echo 'Fetch error:', error
