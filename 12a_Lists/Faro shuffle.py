def nieuw_kaartspel(kleuren, waarden):
    uitvoer = []
    for i in range(len(kleuren)):
        for j in range(len(waarden)):
            uitvoer += [kleuren[i] + waarden[j]]
    return uitvoer

def splits_kaartspel(kaartspel):
    uitvoer = (kaartspel[: len(kaartspel) // 2], kaartspel[len(kaartspel) // 2 :])
    return uitvoer

def faro_shuffle(deel_1, deel_2):
    uitvoer = []
    for i in range(len(deel_1)):
        uitvoer.append(deel_1[i])
        uitvoer.append(deel_2[i])
    if len(deel_1) != len(deel_2):
        uitvoer.append(deel_2[-1])
    return uitvoer

print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))
