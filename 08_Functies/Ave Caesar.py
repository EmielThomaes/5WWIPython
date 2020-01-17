def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')


def roteer_letter(l, aantal_plaatsen):
    return chr(ord(l) + aantal_plaatsen)
