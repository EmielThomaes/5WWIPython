def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')


def roteer_letter(letter, aantal_plaatsen):
    # volgnummer in het alfabet bepaald van de gegeven leeter
    volgnummer_letter = min(ord(letter)) % ord('a'), ord(letter) % ord('A')
    # volgnummer in alfabet van nieuwe letter
    nieuw_volgnummer = (volgnummer_letter + aantal_plaatsen) % 26
    # offset
    offset = nieuw_volgnummer - volgnummer_letter
    return chr(ord(letter) + offset)
    # if en else is ook mogelijk

def versleutel(woord, n):
    rotatie = ''
