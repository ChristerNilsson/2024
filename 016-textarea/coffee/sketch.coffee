range = _.range

lines = []

window.setup = ->
	btn = document.getElementById "add"
	btn.addEventListener 'click', ->
		pgn = document.getElementById "pgn"
		lines.push "#{lines.length}. Nbxe4+ Nbxe4+"
		pgn.innerHTML = lines.join "\n"
		pgn.scrollTop = pgn.scrollHeight

	sel = document.getElementById "sel"
	sel.addEventListener 'click', ->
		pgn = document.getElementById "pgn"
		pgn.select()
		document.execCommand 'copy'

	anal = document.getElementById "anal"
	anal.addEventListener 'click', ->
		pgn = document.getElementById "pgn"
		pgn.select()
		document.execCommand 'copy'
		pgn.selectionStart = pgn.selectionEnd
