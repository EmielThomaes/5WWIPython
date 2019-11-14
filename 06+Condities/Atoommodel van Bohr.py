# invoer

aantal_elektronen = int(input('aantal elektronen = '))

# berekening

if aantal_elektronen >= 156:
    schil = 'Q-schil'
elif aantal_elektronen >= 124:
    schil = 'P-schil'
elif aantal_elektronen >= 92:
    schil = 'O-schil'
elif aantal_elektronen >= 60:
    schil = 'N-schil'
elif aantal_elektronen >= 28:
    schil = 'M-schil'
elif aantal_elektronen >= 10:
    schil = 'L-schil'
else:
    schil = 'K-schil'

# uitvoer

print('De ' + schil + ' is de buitenste schil van een stabiel atoom met ' + str(aantal_elektronen) + ' elektronen.')
