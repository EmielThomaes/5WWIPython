# invoer

bruto_jaarsalaris = float(input('geef het bruto jaarsalaris: '))

# berekening

rsz_bijdrage = bruto_jaarsalaris * 0.1307
netto_belastbaar_inkomen = bruto_jaarsalaris - rsz_bijdrage

if netto_belastbaar_inkomen <= 8860.00:
    schijf_één = 0
    voorheffing = 0
elif netto_belastbaar_inkomen <= 13250.00:
    schijf_één = netto_belastbaar_inkomen - 8860.00
    voorheffing = schijf_één * 0.25
elif netto_belastbaar_inkomen <= 23390.00:
    schijf_één = 13250.00
    schijf_twee = netto_belastbaar_inkomen - 13250.00
    voorheffing = (schijf_één * 0.25) + (schijf_twee * 0.40)
elif netto_belastbaar_inkomen <= 40480.00:
    schijf_één = 13250.00
    schijf_twee = 10140.00
    schijf_drie = netto_belastbaar_inkomen - 23390.00
    voorheffing = (schijf_één * 0.25) + (schijf_twee * 0.40) + (schijf_drie * 0.45)
else:
    schijf_één = 13250.00
    schijf_twee = 10140.00
    schijf_drie = 17090.00
    schijf_vier = netto_belastbaar_inkomen - 40480.00
    voorheffing = (schijf_één * 0.25) + (schijf_twee * 0.40) + (schijf_drie * 0.45) + (schijf_vier * 0.50)

netto_jaarsalaris = netto_belastbaar_inkomen - voorheffing
netto_maandsalaris = netto_jaarsalaris / 12

uitvoer_1 = '+ bruto jaarsalaris {:>10.2f}'
uitvoer_2 = '- rsz {:>25.2f}'
uitvoer_3 = '- voorheffing {:>17.2f}'
uitvoer_4 =
# uitvoer

print(uitvoer_1.format(bruto_jaarsalaris))
