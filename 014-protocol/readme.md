# Översikt

Hur man översätter ett handskrivet schackprotokoll till en PGN-fil.
Denna version kräver att dragen skrivs på formen e2e4 och med varje tecken i en egen ruta.
Om detta lyckas kommer jag att gå vidare med [Algebraisk Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))

![](data/e2e4/30x30.jpg)

```
1. Nf3 Nf6 
2. c4 g6 
3. Nc3 Bg7 
4. d4 O-O 
5. Bf4 d5 6. Qb3 dxc4 7. Qxc4 c6 8. e4 Nbd7 9. Rd1 Nb6 
10. Qc5 Bg4 11. Bg5 Na4 12. Qa3 Nxc3 13. bxc3 Nxe4 14. Bxe7 Qb6 
15. Bc4 Nxc3 16. Bc5 Rfe8+ 17. Kf1 Be6 18. Bxb6 Bxc4+ 19. Kg1 Ne2+ 
20. Kf1 Nxd4+ 21. Kg1 Ne2+ 22. Kf1 Nc3+ 23. Kg1 axb6 24. Qb4 Ra4 
25. Qxb6 Nxd1 26. h3 Rxa2 27. Kh2 Nxf2 28. Re1 Rxe1 29. Qd8+ Bf8 
30. Nxe1 Bd5 31. Nf3 Ne4 32. Qb8 b5 33. h4 h5 34. Ne5 Kg7 
35. Kg1 Bc5+ 36. Kf1 Ng3+ 37. Ke1 Bb4+ 38. Kd1 Bb3+ 39. Kc1 Ne2+ 
40. Kb1 Nc3+ 41. Kc1 Rc2# 0-1
```

```
program protokoll raw.jpg corners.txt facit.txt 30x30.jpg digits.h5 letters.h5 digits.csv letters.csv PGN
scanner IN        UT
buildLetters                                                        UT
human   IN                            UT  
zero              IN      UT
adam              IN      IN                    UT       
bertil                                IN        IN                             UT         UT  
cesar                                                     IN        IN         IN         IN          UT
```

## digits.h5

Denna modell skapas mha en MNIST-databas. Accuracy 99.2%. Siffrorna är 0123456789.

## letter.h5

Denna modell skapas mha en EMNIST-databas, byClass, där man väljer ut följande bokstäver: abcdefgh.

## zero.js

Först måste man kalibrera in hörnen mha measure.

## adam.py

Detta program plockar ut den intressanta rektangeln som anges av hörnen från föregående steg.

## bertil.py

Detta program läser in facit.txt som innehåller de korrekta dragen på formatet e2e4.
M h a 30x30.jpg skapas därefter två csv-filer, digits.csv och letters.csv.
En rad innehåller facit i första positionen följt av 28 x 28 = 784 tal mellan 0 och 255.

## cesar.py

Detta program använder två modeller, letters.h5 samt digits.h5.
Det predikterar med hjälp av 784 pixlar och jämför med facit.

