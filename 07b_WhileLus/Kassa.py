totaalbedrag = 0

prijs_product = float(input('prijs product = '))

while prijs_product > 0:
    totaalbedrag += prijs_product
    prijs_product = float(input('prijs product = '))

uitvoer = 'De totale prijs is € {:.2f}'

print(uitvoer.format(totaalbedrag))
