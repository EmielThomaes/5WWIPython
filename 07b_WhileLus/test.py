getal = 10
while getal > 0 and getal < 10000000:
    getal = getal * getal
    print(getal)

print('')

getal = 0

while getal < 5:
    print(getal)
    getal += 1

print('')

for i in range(5):
    print(i)

print('')

woord = 'start'

while woord != 'stop':
    print(woord)
    woord = input('geef woord:')

print('')

vorst_periode = 0
temperatuur = int(input('Dagtemperatuur: '))

while temperatuur <= 0:
    vorst_periode += 1
    # op einde van while-lus NIEUWE INVOER vragen
    temperatuur = int(input('Dagtemperatuur: '))

print(vorst_periode)

print('')

from random import randint

max_periode = 0

for i in range(1000000):
    temp = randint(-10, 30)
    vorst_periode = 0

    while temp < 0:
        vorst_periode += 1
        temp = randint(-10, 30)
    max_periode = max(max_periode, vorst_periode)

print(max_periode)

print('')

from random import randint

munt = 0
aantal_experimenten = 100000

for i in range(aantal_experimenten):
    munt += randint(0, 1)

print('munt:', munt / aantal_experimenten, 'kop:', (aantal_experimenten - munt) / aantal_experimenten)
