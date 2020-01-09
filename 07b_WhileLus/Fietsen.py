# invoer

snelheid_stijn = int(input('geef de snelheid van Stijn (in m/s): '))
snelheid_kaat = int(input('geef de snelheid van Kaat (in m/s): '))
afstand = int(input('geef de afstand tussen de twee huizen (in m): '))

# berekening

afstand_stijn = 0
afstand_kaat = 0
tijd = 0

while (afstand_stijn + afstand_kaat) < afstand:
    afstand_stijn += snelheid_stijn
    afstand_kaat += snelheid_kaat
    tijd += 1

uitvoer = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'

# uitvoer

print(uitvoer.format(tijd))

