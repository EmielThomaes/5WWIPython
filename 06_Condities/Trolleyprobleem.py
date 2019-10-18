# invoer

antwoord_1 = input('Aan de handel trekken van de wissel? ')
antwoord_2 = input('Man van de brug duwen? ')

# berekening

if antwoord_1 != antwoord_2:
    doden = 1
elif antwoord_1 == 'ja':
    doden = 2
else:
    doden = 5

# uitvoer

print(doden)

# if antwoord_1 == 'ja' and antwoord_2 != 'ja':
#   doden = 2
# if antwoord_1 != 'ja' and ... (alle combinaties geven)
