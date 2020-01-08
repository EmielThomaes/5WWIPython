# invoer

tijdstip = int(input('geef het tijdstip: '))

# berekening

stappen_naar_voor = 0
stappen_naar_achter = 0

for i in range(1, tijdstip + 1):
    if i % 2 != 0:
        stappen_naar_voor = stappen_naar_voor + i + 1
    if i % 2 == 0:
        stappen_naar_achter = stappen_naar_achter + (i // 2)

# uitvoer

print(stappen_naar_voor - stappen_naar_achter)
