def ontdubbelen(woord):
    nieuw_woord = ''
    vorige_letter = ''
    for i in range(len(woord)):
        if woord[i] != vorige_letter:
            nieuw_woord += woord[i]
        vorige_letter = woord[i]
    return nieuw_woord
