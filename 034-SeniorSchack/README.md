[Try it!](https://christernilsson.github.io/2024/034-SeniorSchack)

# Vad jag behövde göra för att få detta att fungera med nodejs och import

* npm install lodash

* package.json: { "type": "module" }

* utils.coffee
	* import {marked} from "marked"
	* import _ from "lodash"
	* export md = marked

* batch.coffee
	* import {div,echo,md,range,table,tr,td} from './utils.js'
	* import fs from 'fs'
	* content = getHTML()
	* fs.writeFile "batch.html", content, (err) => if (err) then console.error err else console.log "File written successfully."
		* error-funktionen måste vara med
