def volgende_rij(rij):
    nieuwe_rij = []
    for i in range(len(rij) - 1):
        if rij[i] == rij[i + 1]:
            nieuwe_rij.append(rij[i])
        else:
            if (rij[i] == 'Y' and rij[i + 1] == 'G') or (rij[i] == 'G' and rij[i + 1] == 'Y'):
                nieuwe_rij.append('R')
            elif (rij[i] == 'Y' and rij[i + 1] == 'R') or (rij[i] == 'R' and rij[i + 1] == 'Y'):
                nieuwe_rij.append('G')
            else:
                nieuwe_rij.append('Y')
    return nieuwe_rij

def driehoek(onderste_rij):
    lijst = [onderste_rij]
    nieuwe_rij = volgende_rij(onderste_rij)
    while len(nieuwe_rij) != 0:
        lijst.append(nieuwe_rij)
        nieuwe_rij = volgende_rij(lijst[len(lijst) - 1])
    return lijst

def kleuren(lijst):
    green, red, yellow = 0, 0, 0
    for i in range(len(lijst)):
        for j in range(len(lijst[i])):
            if lijst[i][j] == 'Y':
                yellow += 1
            elif lijst[i][j] == 'G':
                green += 1
            else:
                red += 1
    return green, red, yellow
