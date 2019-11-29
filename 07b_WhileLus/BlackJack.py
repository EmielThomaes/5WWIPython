totaal_kaarten = 0

waarde_kaart = int(input('geef de waarde van de kaart: '))

while waarde_kaart > 0 and totaal_kaarten < 21:
    totaal_kaarten += waarde_kaart
    if totaal_kaarten < 21:
        waarde_kaart = int(input('geef de waarde van de kaart: '))

if totaal_kaarten == 21:
    uitvoer = 'Gewonnen!'
elif totaal_kaarten > 21:
    uitvoer = 'Verbrand (' + str(totaal_kaarten) + ')'
else:
    uitvoer = 'Voorzichtig gespeeld (' + str(totaal_kaarten) + ')'

print(uitvoer)
