# invoer

n_60 = float(input('Geef het aantal waargenomen tjirps per minuut: '))

# berekening

formule_celsius = 'temperatuur (Celsius): ' + str(10 + ((n_60 - 40) / 7))

formule_fahrenheit = 'temperatuur (Fahrenheit): ' + str(50 + ((n_60 - 40) / 4))

# uitvoer

print(formule_fahrenheit)
print(formule_celsius)
