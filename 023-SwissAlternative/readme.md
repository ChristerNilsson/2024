### Denna swisslottning är inte identisk med FIDE:s.

Orsaken till detta kan diskuteras.
Det verkar som att FIDE:s regler avspeglar hur en icke publicerad algoritm fungerar.
Denna algoritm är troligen JaVaFo.
De flesta lottningsprogram anropar javafo.jar.

```
Metod:
Sortera spelarna fallande på [poäng,rating,namn]
Gruppera på poäng.
För varje grupp:
  Hämta eventuell sinker från föregående grupp.
  Halvera gruppen. Vid udda antal blir den sista en sinker till nästa grupp.
  Para ihop de två halvgrupperna typ blixtlås.
Låt vanlig backtrackande Monrad hantera resten.
```
