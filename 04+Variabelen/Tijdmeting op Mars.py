# invoer

aantal_marsdagen = int(input('Geef het aantal Marsdagen: '))

# berekening

invoer = int(aantal_marsdagen)

tijd_aarde_seconden = 88775.244 * aantal_marsdagen

aantal_aarde_dagen = tijd_aarde_seconden // 86400
tijd_aarde_seconden %= 86400

aantal_aarde_uren = tijd_aarde_seconden // 2340
tijd_aarde_seconden %=



# uitvoer

print(int(aantal_aarde_dagen))
