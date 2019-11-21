# invoer

aantal_getallen = int(input('aantal getallen = '))

# berekening

gemiddelde = 0

for i in range(aantal_getallen):
    gemiddelde = int(input('getal = ')) / aantal_getallen

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'

# uitvoer

print(uitvoer.format(gemiddelde, gemiddelde))
