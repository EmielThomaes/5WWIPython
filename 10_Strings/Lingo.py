def hint(gegokte_woord, juiste_woord):
    hint = ''
    for i in range(0, len(juiste_woord)):
        if gegokte_woord[i] in juiste_woord:
            if gegokte_woord[i] == juiste_woord[i]:
                hint += gegokte_woord[i].upper()
            else:
                hint += gegokte_woord[i]
        else:
            hint += '.'
    return hint
