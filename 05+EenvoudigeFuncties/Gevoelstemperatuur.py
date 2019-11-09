# invoer

temperatuur = float(input('Geef de luchttemperatuur: '))
windsnelheid = float(input('Geef de windsnelheid: '))

# berekening

windsnelheid_meter = windsnelheid / 3.6
gevoelstemperatuur = 13.12 + (0.6215 * temperatuur) + ((0.3965 * temperatuur) - 11.37) * pow((3.6 * windsnelheid_meter), 0.16)

# uitvoer

print(gevoelstemperatuur)
