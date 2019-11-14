from math import pi, sqrt

# invoer

afstand = float(input('afstand van de satelliet tot het middelpunt van de aarde = '))
snelheid = float(input('snelheid van de satelliet ten opzichte van de aarde = '))

# berekening

geocentrische_constante = 398600.4418 * pow(10, 9)

lengte_grote_as = (geocentrische_constante * afstand) / ((2 * geocentrische_constante) - (afstand * (pow(snelheid, 2))))

lengte_periode = 2 * pi * sqrt(pow(lengte_grote_as, 3) / geocentrische_constante)

aantal_dagen = int(lengte_periode // (24 * 60 * 60))
rest_lengte_periode = lengte_periode % (24 * 60 * 60)

aantal_uren = int(rest_lengte_periode // (60 * 60))
rest_lengte_periode %= (60 * 60)

aantal_minuten = int(rest_lengte_periode // 60)

uitvoer_1 = 'grote as: {} meter'
uitvoer_2 = 'periode: {} seconden'
uitvoer_3 = 'periode: {} dagen, {} uren en {} minuten'

# uitvoer

print(uitvoer_1.format(lengte_grote_as))
print(uitvoer_2.format(lengte_periode))
print(uitvoer_3.format(aantal_dagen, aantal_uren, aantal_minuten))
