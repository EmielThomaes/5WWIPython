getal = int(input('geef een getal: '))

deler = 2

while (getal % deler) != 0 and getal != 1:
    deler += 1

if deler == getal:
    uitvoer = str(getal) + ' is een priemgetal'
else:
    uitvoer = str(getal) + ' is geen priemgetal'

print(uitvoer)
