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

#if ant_1 == ant_2:
#    uitvoer = 'onbeslist'
#elif ant_1 == 'blad':
#    if ant_2 == 'steen':
#        uitvoer = 'speler 1 wint'
#    else:
#        uitvoer = 'speler 2 wint'
#elif ant_1 == 'steen':
#    if ant_2 == 'schaar':
#        uitvoer = 'speler 1 wint'
#    else:
#        uitvoer = 'speler 2 wint'
#else:
#    if ant_2 == 'blad':
#        uitvoer = 'speler 1 wint'
#    else:
#        uitvoer = 'speler 2 wint'


# else enkel gebruiken voor moeilijkste code (makkelijkste manier om 'speler 2 wint' enkel in else vermelden)
# -> elif speler_1 == 'steen' and speler_2 == 'schaar'
#       'speler 1 wint'
