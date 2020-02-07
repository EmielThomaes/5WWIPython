def verwijder_medeklinkers(woord):
    nieuw_woord = ''
    for i in range(len(woord)):
        if woord[i] != 'a' and woord[i] != 'e' and woord[i] != 'i' and woord[i] != 'o' and woord[i] != 'u':
            nieuw_woord += (woord[i + 1: len(woord)])
        else:
            nieuw_woord = woord
    return nieuw_woord

def varkenslatijn(woord):
    vertaald_woord = ''
    if woord[0] == 'a' or woord[0] == 'e' or woord[0] == 'i' or woord[0] == 'o' or woord[0] == 'u':
        vertaald_woord += (woord + 'ibus')
    elif woord[len(woord) - 1] == 'a' or woord[len(woord) - 1] == 'i' or woord[len(woord) - 1] == 'u':
        vertaald_woord += (woord + 'nt')
    else:
        vertaald_woord += (verwijder_medeklinkers(woord) + 'itum')
    vertaald_woord.replace('j', 'i')
    vertaald_woord.replace('z', '')
    vertaald_woord.replace('y', '')
    return vertaald_woord

def vertaal(zin):
