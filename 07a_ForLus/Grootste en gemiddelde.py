# invoer

aantal_getallen = int(input('aantal getallen = '))

# berekening

# lees het eerste getal voor de lus in
getal_0 = int(input('geef getal = '))

# het eerste getal is onmiddellijk de som en het grootste getal
som, grootste = getal_0, getal_0

for i in range(aantal_getallen - 1):
    getal = int(input('geef getal = '))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal_getallen

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'

# uitvoer

print(uitvoer.format(grootste, gemiddelde))
