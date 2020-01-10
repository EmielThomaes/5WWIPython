# invoer

getal = float(input('geef een willekeurig getal: '))

# berekening

term = (1 / 2)
som_termen = 0
aantal_termen = 0

while som_termen < getal:
    som_termen += term
    term /= 2
    aantal_termen += 1

# uitvoer

print(aantal_termen, som_termen)
