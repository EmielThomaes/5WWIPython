#print('\N{LESS-THAN OR EQUAL TO}')

# invoer

x = float(input('x = '))
y = float(input('y = '))

# berekening

berekening_1 = abs(abs(x) - abs(y))
berekening_2 = abs(x - y)

# uitvoer

print(str(round(berekening_1, 4)) + ' \N{LESS-THAN OR EQUAL TO} ' + str(round(berekening_2, 4)))

#{:.4F}
