SIZE = 40
YOFFSET = 40

BASE = 'KQk' # Hämtas från URL.

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
    textSize 20
    fill 'black'
    text "Mate in " + level, width/2,25
    s = if moveNumber == 0 then "Endbase Exerciser by Christer" else extractLastMove chess.pgn()
    text s,width/2,380

getProblem = (delta) ->
    level += delta
    moveNumber = 0
    if level < 1 then level = 1
    if not level in problemBase then level -= 1
    problems = problemBase[level].split ' '
    problem = _.sample problems
    indexes = (problem.slice 2*i,2*i+2 for i in range BASE.length)
    chess.clear()
    for i in range BASE.length
        letter = BASE[i]
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

    buttons.push new Button 'KQk',width/2,0,100,40
    buttons.push new Button 'KRk',width/2,50,100,40
    buttons.push new Button 'KQkr',width/2,100,100,40
    buttons.push new Button 'KBBk',width/2,150,100,40
    buttons.push new Button 'KBNk',width/2,200,100,40
    buttons.push new Button 'KNNNk',width/2,250,100,40

class Button
    constructor : (@piece,@x,@y,@w,@h) ->
        @images = []
        for letter in @piece
            color = if letter in "KQRBNP" then 'w' else 'b'
            piece = letter.toUpperCase()
            if piece != "K" then @images.push images[color + piece]
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
    draw : ->
        fill if (@i+@j) % 2 == 0 then 'gray' else 'yellow'
        rect @x,YOFFSET+@y,SIZE,SIZE
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
            if square.inside mouseX,mouseY then clickedFrom = square.index
    mouseReleased : ->
        if clickedFrom == -1 then return
        for square in board.squares
            if square.inside mouseX,mouseY then clickedTo = square.index
        moves = (move.from + move.to for move in chess.moves { verbose: true })
        if moves.length == 0
            getProblem 0
            return
        a = board.squares[clickedFrom].name
        b = board.squares[clickedTo].name
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
