woord = input('geef het woord: ')
gedraaide_geldbedrag = int(input('geef het gedraaide geldbedrag: '))
gegokte_letters = ''
gewonnen_geldbedrag = 0

letter = input('geef een letter: ')
while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    gewonnen_geldbedrag += gedraaide_geldbedrag
    letter = input('geef een letter: ')

print(gewonnen_geldbedrag)
