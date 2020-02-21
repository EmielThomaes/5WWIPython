def hoogtemeters(lijst_hoogtes):
    lijst_hoogteverschillen = []
    for i in range(0, len(lijst_hoogtes) - 1):
        lijst_hoogteverschillen.append(lijst_hoogtes[i + 1] - lijst_hoogtes[i])
    return lijst_hoogteverschillen

def dalen_en_stijgen(lijst):
    dalen, stijgen = 0, 0
    for hoogtemeter in lijst:
        if hoogtemeter < 0:
            dalen += hoogtemeter
        else:
            stijgen += hoogtemeter
    return abs(dalen), stijgen
