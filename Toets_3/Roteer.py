def roteer(woord, cijfer_rotatie):
    geroteerd_woord = ''
    while cijfer_rotatie >= len(woord):
        cijfer_rotatie -= len(woord)
    geroteerd_woord += (woord[cijfer_rotatie: len(woord)] + woord[0: cijfer_rotatie])
    return geroteerd_woord
