def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')


def roteer_letter(letter, aantal_plaatsen):
    if ord(letter) + aantal_plaatsen > 122:
        aantal_plaatsen = (ord(letter) + aantal_plaatsen) - 122
        nieuwe_letter = chr(ord('a') + aantal_plaatsen - 1)
    return nieuwe_letter

print(roteer_letter('z', 22))
