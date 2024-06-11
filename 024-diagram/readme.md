[Resultat](https://member.schack.se/ShowTournamentServlet?id=13664&listingtype=2)

# Tyresö Open 2024

* Axlarna är de båda spelarna i ett parti
* Siffran i matrisen är rondnummer
* Asterisk markerar att en spelare ej kan möta sig själv
* Matrisen är symmetrisk kring denna diagonal
* 78 spelare
* 8 ronder

### Monrad sorterad på Elo

* Algoritmen försöker skapa personliga grupper med varje spelare i mitten.
* Spelare 14,17,19,24,38,41,43,48,62 och 65 uppvisar perfekta grupper
* Första och sista spelarna kan av naturliga skäl inte ligga i mitten
* Notera att övre vänstra 8x8-hörnet i princip är fullt. Här möts de bästa spelarna.
* Tar man bort rond 8 försvinner en del ojämna partier.
* Priser utdelas till spelarna med bäst Elo-diffar.
* Det innebär att även spelaren med sämst Elo-tal kan vinna.
* Denna matris är oberoende av vilka resultat partierna får.
* Den är även oberoende av avståndet mellan elo-talen eller deras nivå.
* 1-2-3-4-5-6-7-8 ger exakt samma matris som 1000-1100-1200-1300-2100-2200-2300-2400
* Bidirectional innebär att monrad-parningen sker omväxlande neråt och uppåt. Avsikten med detta är att i görligaste mån centrera varje spelare i sin grupp.

### Swiss (Dutch) bygger på poänggrupper som halveras

* Notera den stora mängden ojämna partier pga Swiss, ffa i rond 1
* Notera glesheten i övre vänstra 8x8-hörnet