# invoer

dobbelsteen_1_aanvaller = int(input('dobbelsteen 1 aanvaller = '))
dobbelsteen_2_aanvaller = int(input('dobbelsteen 2 aanvaller = '))
dobbelsteen_3_aanvaller = int(input('dobbelsteen 3 aanvaller = '))

dobbelsteen_1_verdediger = int(input('dobbelsteen 1 verdediger = '))
dobbelsteen_2_verdediger = int(input('dobbelsteen 2 verdediger = '))

# berekening

grootste_ds_aanvaller = max(dobbelsteen_1_aanvaller,dobbelsteen_2_aanvaller,dobbelsteen_3_aanvaller)
kleinste_ds_aanvaller = min(dobbelsteen_1_aanvaller,dobbelsteen_2_aanvaller,dobbelsteen_3_aanvaller)
middelste_ds_aanvaller = (dobbelsteen_1_aanvaller + dobbelsteen_2_aanvaller + dobbelsteen_3_aanvaller) - (grootste_ds_aanvaller + kleinste_ds_aanvaller)

grootste_ds_verdediger = max (dobbelsteen_1_verdediger,dobbelsteen_2_verdediger)
kleinste_ds_verdediger = min(dobbelsteen_1_verdediger,dobbelsteen_2_verdediger)

if grootste_ds_aanvaller > grootste_ds_verdediger:
    /

# uitvoer



# maximum = max(x1, x2, x3, x4)
# minimum = min(x1, x2, x3, x4)
# mid_1 = max(min(x1, x2), min(x2, x3), min(x1, x3))
# mid_2 = x1 + x2 + x3 + x4 - minimum - maximum - mid_1
# print(maximum, max(mid_1, mid_2), min(mid_1, mid_2), minimum
