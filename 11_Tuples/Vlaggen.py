def vlag(richting, kleuren):
    uitvoer = ''
    for i in range(len(kleuren)):
        if richting == 'verticaal':
            uitvoer += (kleuren[i] + ' | ')
        else:
            uitvoer += (kleuren[i] + '\n' + '-' + '\n')
    return uitvoer[:-3]

print(vlag('horizontaal', ('rood', 'geel', 'groen')))
