# invoer

s = int(input('Geef een aantal seconden: '))

# berekening

aantal_dagen = str(s // (24 * 60 * 60)) + 'd '
rest_seconden = s % (24 * 60 * 60)

aantal_uren = str(rest_seconden // (60 * 60))
rest_seconden %= (60 * 60)

aantal_minuten = str(rest_seconden // 60)
rest_seconden %= 60

aantal_seconden = str(rest_seconden)

# uitvoer

print(aantal_dagen + aantal_uren + ':' + aantal_minuten + ':' + aantal_seconden)
