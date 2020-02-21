def dubbels(lijst):
    nieuwe_lijst = []

    for element in lijst:
    # als element 2 x voorkomt in lijst en nog niet voorkomt in nieuwe_lijst
        if lijst.count(element) > 1 and element not in nieuwe_lijst:
            nieuwe_lijst.append(element)
    return nieuwe_lijst
