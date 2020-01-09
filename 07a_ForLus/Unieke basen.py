# invoer

aantal_basen = int(input('aantal basen = '))

# berekening

dna_a = ''
dna_t = ''
dna_g = ''
dna_c = ''

for i in range(aantal_basen):
    soort = input('geef de soort DNA: ')
    if soort == 'A':
        dna_a = ' A'
    if soort == 'T':
        dna_t = ' T'
    if soort == 'G':
        dna_g = ' G'
    if soort == 'C':
        dna_c = ' C'

aantal_verschillende_soorten = int((len(str(dna_a + dna_t + dna_g + dna_c))) / 2)

# uitvoer
