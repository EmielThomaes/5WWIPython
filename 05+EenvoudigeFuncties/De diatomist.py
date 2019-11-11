# invoer

from math import pi

kleine_straal = float(input('Straal van de kleine cirkel: '))
grote_straal = float(input('Straal van de grote cirkel: '))

# berekening

maximum_aantal_kleine_cirkels = int((0.83 * ((grote_straal ** 2) / (kleine_straal ** 2))) - 1.9)

bedekkingsgraad =

uitvoer = 'test {:d} + {:.2f}'

# uitvoer

print(uitvoer.format(maximum_aantal_kleine_cirkels, bedekkingsgraad))
