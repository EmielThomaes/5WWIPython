# invoer

from math import pi

kleine_straal = float(input('Straal van de kleine cirkel: '))
grote_straal = float(input('Straal van de grote cirkel: '))

# berekening

maximum_aantal_kleine_cirkels = int((0.83 * ((grote_straal ** 2) / (kleine_straal ** 2))) - 1.9)

oppervlakte_grote_cirkel = (pow(grote_straal, 2) * pi)
oppervlakte_kleine_cirkel = (pow(kleine_straal, 2) * pi)

bedekkingsgraad = ((maximum_aantal_kleine_cirkels * oppervlakte_kleine_cirkel) / oppervlakte_grote_cirkel) * 100

uitvoer = '{:d} kleine cirkels bedekken {:.2f}% van de grote cirkel'

# uitvoer

print(uitvoer.format(maximum_aantal_kleine_cirkels, bedekkingsgraad))
