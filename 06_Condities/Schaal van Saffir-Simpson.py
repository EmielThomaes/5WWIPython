# invoer

windsnelheid = int(input('windsnelheid = '))

# berekening

if windsnelheid < 119:
    uitvoer = 'geen orkaan'
elif windsnelheid >= 119 and windsnelheid <= 153:
    uitvoer = 'categorie 1'
elif windsnelheid >= 154 and windsnelheid <= 177:
    uitvoer = 'categorie 2'
elif windsnelheid >= 178 and windsnelheid <= 209:
    uitvoer = 'categorie 3'
elif windsnelheid >= 210 and windsnelheid <= 249:
    uitvoer = 'categorie 4'
elif windsnelheid >= 250:
    uitvoer = 'categorie 5'

# uitvoer

print(uitvoer)

# omgekeerd vanaf 250 werken -> kortere code
# if windsnelheid >= 250:
# elif windsnelheid >= 210:
# ...
