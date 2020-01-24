# overloop alle letters van de strin
# indien de letter een spatie is
# volgende letter wordt hoofdletter
# werk met: nieuwe_zin +=

def germaniseer(zin):
    nieuwe_zin = ''
    for i in range (0, len(zin)):
        if zin[i] == ' ':
            nieuwe_zin += ' ' + zin[i+1].upper()
        else:
            nieuwe_zin += zin[i]
    return nieuwe_zin

print(germaniseer('Dit is een test'))
