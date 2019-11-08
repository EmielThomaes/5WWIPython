naam = input('Geef naam: ')

aantal_klinkers, aantal_medeklinkers = 0, 0

for letter in naam:
    if letter in 'aeuoi':
        aantal_klinkers += 1
    else:
        aantal_medeklinkers += 1

print(aantal_klinkers, aantal_medeklinkers)



naam = input('Geef naam: ')

aantal_klinkers = 0

for letter in naam:
    if letter in 'aeuoi':
        aantal_klinkers += 1

print(aantal_klinkers, len(naam) - aantal_klinkers)



naam = input('Geef naam: ')

i = 1

for letter in naam:
    print(i * letter)
    i += 1
