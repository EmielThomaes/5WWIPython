# invoer

b = float(input('breedte veld: '))
l = float(input('lengte veld: '))
c = float(input('kubieke meter graan per hectare: '))
r = float(input('straal graansilo: '))
h = float(input('hoogte graansilo: '))

# berekening

pi = 3.14159

volume_graansilo = (r**2) * pi * h
hoeveelheid_graan = (c / 10000) * (l * b)
aantal_graansilo = int((hoeveelheid_graan // volume_graansilo) + 1)

hoogte_laatste_graansilo = hoeveelheid_graan % volume_graansilo

# uitvoer

print(aantal_graansilo)
print(hoogte_laatste_graansilo)
