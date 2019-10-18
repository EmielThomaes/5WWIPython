# bij elif wordt eerste blokje die juist is uitgevoerd en dan naar einde gegaan (max. 1 keer uitgevoerd)
# bij if wordt telkens het blokje dat juist is uitgevoerd (kan meerdere keren)
# eerst overal pass invullen dan pas op het einde voorwaarden aanvullen
# test 3 = test 2 maar simpeler en correcter

getal = int(input('geef getal: '))

if getal < 0 and getal % 2 == 0:
    uitvoer = 'negatief en even getal'
elif getal < 0 and getal % 2 != 0:
    uitvoer = 'negatief en oneven getal'
elif getal > 0 and getal % 2 == 0:
    uitvoer = 'positief en even getal'
elif getal > 0 and getal % 2 != 0:
    uitvoer = 'positief en oneven getal'
else:
    uitvoer = 'gelijk aan nul'

print(uitvoer)
