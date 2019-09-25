# invoer

t = int(input('Geef de tijd (in nanoseconden) die de laser nodig heeft om heen en terug te reizen: '))

# berekening

c = 299792458
n = 1.000277

d = str((c * (t * 10**-9)) / (2 * n)) + ' meter'

# uitvoer

print(d)
