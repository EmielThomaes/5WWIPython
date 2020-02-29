from operator import itemgetter

def bereken_prijs(lijst_winkelartikelen):
    totaalprijs = 0
    for i in range(len(lijst_winkelartikelen)):
        totaalprijs += lijst_winkelartikelen[i][1]
    return totaalprijs

def winkelbriefje(lijst_winkelartikelen):
    lijst = []
    for i in range(len(lijst_winkelartikelen)):
        lijst += [lijst_winkelartikelen[i][0]]
    return lijst

def sorteer(lijst_winkelartikelen):
    lijst_winkelartikelen.sort(key=itemgetter(1))
    return lijst_winkelartikelen


print(sorteer([('Lays Paprika', 3.94), ('Napoleon', 1.48), ('Milky Way', 3.64), ('M&M', 3.06), ('Crocky Zout', 3.62), ('Bounty', 1.86)]))
