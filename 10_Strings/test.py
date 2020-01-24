woord = 'python'

for letter in woord:
    print(letter)

print('')

for i in range(0, len(woord)):
    print(woord[i])

print('')

for i in range(0, len(woord), 2):
    print(woord[i])

print('')

for i in range(-1, -len(woord)-1, -1):
    print(woord[i])

print('')

for i in range(-len(woord), 0):
    print(woord[i])

print('')

a = 1
b = 4

print(woord[a - 1: b])

print('')

# veelgemaakte fout
woord = input('woord: ')

for i in range(0, len(woord)):
    if woord[i] in 'aeoui':
        woord[i] = '*'

print(woord)

print('')

# juiste code
woord = input('woord: ')

for i in range(0, len(woord)):
    if woord[i] in 'aeoui':
        woord = woord[:i] + '*' + woord[i + 1:]

print(woord)
