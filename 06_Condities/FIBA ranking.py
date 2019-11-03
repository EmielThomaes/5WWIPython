# invoer

gescoorde_punten_thuisploeg = int(input('aantal gescoorde punten thuisploeg: '))
gescoorde_punten_uitploeg = int(input('aantal gescoorde punten uitploeg: '))

# berekening

if gescoorde_punten_thuisploeg > gescoorde_punten_uitploeg:
    puntenverschil = gescoorde_punten_thuisploeg - gescoorde_punten_uitploeg
else:
    puntenverschil = gescoorde_punten_uitploeg - gescoorde_punten_thuisploeg

if puntenverschil >= 20:
    punten_winnaar = 800
    punten_verliezer = 200
elif puntenverschil >= 10:
    punten_winnaar = 700
    punten_verliezer = 300
else:
    punten_winnaar = 600
    punten_verliezer = 400

if gescoorde_punten_thuisploeg > gescoorde_punten_uitploeg:
    punten_thuisploeg = int(punten_winnaar - 70)
    punten_uitploeg = int(punten_verliezer + 70)
else:
    punten_thuisploeg = int(punten_verliezer - 70)
    punten_uitploeg = int(punten_winnaar + 70)

uitvoer_1 = 'thuisploeg: ' + '{:.2f}'
uitvoer_2 = '  uitploeg: ' + '{:.2f}'

# uitvoer

print(uitvoer_1.format(punten_thuisploeg))
print(uitvoer_2.format(punten_uitploeg))
