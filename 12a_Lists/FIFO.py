wachtrij = []
element = input()

while element != 'STOP':
    if element != '?':
#       wachtrij += [element]
        wachtrij.append(element)
    elif len(wachtrij) > 0:
        print(wachtrij.pop(0))
    element = input()
