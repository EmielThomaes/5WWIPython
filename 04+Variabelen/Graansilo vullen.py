# invoer

b = float(input('breedte veld: '))
l = float(input('lengte veld: '))
c = float(input('kubieke meter graan per hectare: '))
r = float(input('straal graansilo: '))
h = float(input('hoogte graansilo: '))

# berekening

pi = 3.14159265359

volume_graansilo = (r**2) * pi * h
hoeveelheid_graan = (c / 10000) * (l * b)
aantal_graansilo = int((hoeveelheid_graan // volume_graansilo) + 1)

rest_hoeveelheid_graan = hoeveelheid_graan % volume_graansilo
hoogte_laatste_graansilo = (rest_hoeveelheid_graan) / ((r**2) * pi)

# uitvoer

print(aantal_graansilo)
print(hoogte_laatste_graansilo)
