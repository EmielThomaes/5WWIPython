# invoer

dag = int(input('Dag = '))
maand = int(input('Maand = '))
jaar = int(input('Jaar = '))

# berekening

if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10:
    volgende_dag = dag + 1
    uitvoer = str(volgende_dag) + ' / ' + str(maand) + ' / ' + str(jaar)

# uitvoer

print(uitvoer)
