# invoer

getal = int(input('geef een getal: '))

# berekening

som = 0

for cijfer in str(getal):
    som += int(cijfer)

if getal % som == 0:
    uitvoer = '{} is een Harshadgetal'
else:
    uitvoer = '{} is geen Harshadgetal'

# uitvoer

print(uitvoer.format(getal))
