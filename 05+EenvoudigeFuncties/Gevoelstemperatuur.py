# invoer

temperatuur = float(input('Geef de luchttemperatuur: '))
windsnelheid = float(input('Geef de windsnelheid: '))

# berekening

gevoelstemperatuur = 13.12 + (0.6215 * temperatuur) + ((0.3965 * temperatuur) - 11.37) * pow((3.6 * windsnelheid), 0.16)

# uitvoer

print(gevoelstemperatuur)
