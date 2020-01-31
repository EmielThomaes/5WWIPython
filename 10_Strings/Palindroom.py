def is_palindroom(woord):
    nieuw_woord = ''
    for letter in woord:
        nieuw_woord = letter + nieuw_woord
    if woord == nieuw_woord:
        return True
    else:
        return False
