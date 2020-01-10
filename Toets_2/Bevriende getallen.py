# invoer

getal_a = int(input('geef een getal: '))
getal_b = int(input('geef een getal: '))

# berekening

som_delers_a = 0
som_delers_b = 0

deler_a = 1
deler_b = 1

for i in range(1, getal_a):
    if (getal_a % deler_a) == 0:
        som_delers_a += deler_a
        deler_a += 1
    else:
        deler_a += 1

for i in range(1, getal_b):
    if (getal_b % deler_b) == 0:
        som_delers_b += deler_b
        deler_b += 1
    else:
        deler_b += 1

if som_delers_a == getal_b and som_delers_b == getal_a:
    uitvoer = '{} en {} zijn bevriende getallen'
else:
    uitvoer = '{} en {} zijn geen bevriende getallen'

# uitvoer

print(uitvoer.format(getal_a, getal_b))

