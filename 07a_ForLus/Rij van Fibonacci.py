# invoer

nde_getal = int(input('n = '))

# berekening

f_1 = 1
f_2 = 1

uitkomst = 1

for n in range(nde_getal):
    uitkomst = uitkomst + (n - 1) + (n - 2)

print(uitkomst)
