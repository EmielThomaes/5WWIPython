# invoer

nde_getal = int(input('n = '))

# berekening

f_1 = 1
f_2 = 0

for n in range(nde_getal):
    uitkomst = f_1 + f_2
    f_1 = uitkomst - f_1
    f_2 = uitkomst

print(uitkomst)
