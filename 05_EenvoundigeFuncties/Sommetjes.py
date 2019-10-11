# invoer

a = int(input('a = '))
b = int(input('b = '))

# berekening

uitkomst = int(a + b)
uitvoer = '{:>6.0f} + {:<6.0f} = {:<6.0f}'

# uitvoer

print(uitvoer.format(a, b, uitkomst))
print(uitvoer.format(a * 10, b * 10, uitkomst * 10))
print(uitvoer.format(a * (10**2), b * (10**2), uitkomst * (10**2)))
print(uitvoer.format(a * (10**3), b * (10**3), uitkomst * (10**3)))
print(uitvoer.format(a * (10**4), b * (10**4), uitkomst * (10**4)))

