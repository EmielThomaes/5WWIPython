# invoer

speler_1 = input('Speler 1: blad, steen of schaar? ')
speler_2 = input('Speler 2: blad, steen of schaar? ')

# berekening

if speler_1 == speler_2:
    uitvoer = 'onbeslist'
elif speler_1 < speler_2:
    if speler_1 == 'schaar':
        uitvoer = 'speler 2 wint'
    elif speler_1 == 'blad' and speler_2 == 'schaar':
        uitvoer = 'speler 2 wint'
    else:
        uitvoer = 'speler 1 wint'
elif speler_1 > speler_2:
    if speler_2 == 'schaar':
        uitvoer = 'speler 1 wint'
    elif speler_2 == 'blad' and speler_1 == 'schaar':
        uitvoer = 'speler 1 wint'
    else:
        uitvoer = 'speler 2 wint'

# uitvoer

print(uitvoer)
