singles = (('roos', 9), ('bieke', 8), ('mieke', 10))
uitvoer = '{}: {}/10'

print('punten toets: ')
for single in singles:
    print(uitvoer.format(single[0], single[1]))

print('')

for i in range(len(singles)):
    print(uitvoer.format(singles[i][0], singles[i][1]))
