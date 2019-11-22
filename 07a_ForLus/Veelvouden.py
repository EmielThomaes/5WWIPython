# invoer

getal = int(input('geef een getal: '))

# berekening

uitkomst = 0

for veelvoud in range(getal, 101, getal):
    uitkomst += veelvoud

# uitvoer

print(uitkomst)
