# invoer
eurocent = int(input('Geef aantal eurocent: '))

# berekening

eurocent_invoer = eurocent

aantal_muntstukken = eurocent // 100
eurocent %= 100

aantal_muntstukken += (eurocent // 50)
eurocent %=  50

aantal_muntstukken += (eurocent // 20)
eurocent %= 20

aantal_muntstukken += (eurocent // 10)
eurocent %= 10

aantal_muntstukken += (eurocent // 5)
eurocent %= 5

aantal_muntstukken += (eurocent // 2)
eurocent %= 2

aantal_muntstukken += (eurocent // 1)
eurocent %= 1

uitvoer= str(eurocent_invoer) + ' cent kan je omwisselen in ' + str(aantal_muntstukken) + ' muntstukken'

# uitvoer

print(uitvoer)
