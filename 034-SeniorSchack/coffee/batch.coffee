# import {md,div,echo,menu,table,tr,td,range} from './utils.js'
import {div,echo,md,range,table,tr,td} from './utils.js'
import fs from 'fs'

A = ''

# tds = {style:"border:1px solid black; text-align:left"}
# tdt = {style:"border:1px solid black"}

# rubrik = (a,b,c) =>
# 	tr {},
# 		th tds, a
# 		th tds, b
# 		th tds, c

# rad = (a,b,c) =>
# 	tr {},
# 		td tds, a
# 		td tdt, b
# 		td tdt, c

# export getHTML = ->
# 	div A,
# 		menu A,
# 			"Adam|adam"
# 			"*Bertil*|bertil"
# 			"Ture|Nilsson"
# 			"Gösta|Persson"
# 		menu A,
# 			"Kajsa|adam"
# 			"Greta|bertil"
# 			"Anna|Nilsson"
# 			"Eva|Persson"

getHTML = -> # tabell i tabell. Man får hantera alignment i varje td om kolumnerna ska ha olika alignment
# Eller använda col, colgroup samt nth-child (enligt chatgpt)

	t = table 'style="text-align:right"',
		tr A,
			td A, md "[aaa](aaa)"
			td A,'*bb*'
		tr A,
			td A,'__c__'
			td A,'dddd'

	table A,
		tr A,
			td A, t
			td A, t
			td A, t
		tr A,
			td A, t
			td A, t
			td A, t
		tr A,
			td A, t
			td A, t
			td A, t

	# table A, (tr A,(td A, c+r for c in "abcdefgh").join "" for r in "87654321").join ""

# export getHTML = ->
# 	md """
# 		|||
# 		|-|-:|
# 		|[*bertil*](bertilsson)|1|
# 		|*kalle*|123|
# 		|**ludde**|12|
# 	"""

content = getHTML()
fs.writeFile "batch.html", content, (err) => if (err) then console.error err else console.log "File written successfully."

