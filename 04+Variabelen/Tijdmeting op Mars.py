# invoer

aantal_sol = int(input('Geef het aantal sol (marsdagen): '))

# berekening

aantal_sol_seconden = aantal_sol * 88775.244

aantal_dagen_aarde = int(aantal_sol_seconden // (24 * 60 * 60))
rest_seconden_sol = aantal_sol_seconden % (24 * 60 * 60)

aantal_uren_aarde = int(rest_seconden_sol // (60 * 60))
rest_seconden_sol %= (60 * 60)

aantal_minuten_aarde = int(rest_seconden_sol // 60)
rest_seconden_sol %= 60

aantal_seconden_aarde = int(rest_seconden_sol)

# uitvoer

print(str(aantal_sol) + ' sol = ' + str(aantal_dagen_aarde) + ' dagen, ' + str(aantal_uren_aarde) + ' uren, ' + str(aantal_minuten_aarde) + ' minuten en ' + str(aantal_seconden_aarde) + ' seconden')
