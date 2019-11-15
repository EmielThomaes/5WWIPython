# invoer

dag = int(input('Dag = '))
maand = int(input('Maand = '))
jaar = int(input('Jaar = '))

# berekening

if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10:
    if dag != 31:
        volgende_dag = dag + 1
        uitvoer = str(volgende_dag) + '/' + str(maand) + '/' + str(jaar)
    else:
        volgende_dag = 1
        volgende_maand = maand + 1
        uitvoer = str(volgende_dag) + '/' + str(volgende_maand) + '/' + str(jaar)
if maand == 4 or maand == 6 or maand == 9 or maand == 11:
    if dag == 31:
        volgende_dag = 1
        volgende

# uitvoer

print(uitvoer)
