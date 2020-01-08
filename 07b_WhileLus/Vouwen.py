# invoer

dikte_papier = int(input('dikte papier (in mm): '))
afstand_hemellichaam = int(input('afstand tot hemellichaam (in mm): '))

# berekening

aantal_keer_vouwen = 0
hoogte_gevouwen_papier = dikte_papier

while hoogte_gevouwen_papier < afstand_hemellichaam:
    aantal_keer_vouwen += 1
    hoogte_gevouwen_papier *= 2

uitvoer = 'Na {} keer vouwen bedraagt de dikte van het papier {} mm.'

# uitvoer

print(uitvoer.format(aantal_keer_vouwen, hoogte_gevouwen_papier))
