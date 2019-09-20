# invoer
r = float(input('Geef straal: '))
r = r * 10**(-2)
q_1 = 2.0 * 10**-6
q_2 = 1.0 * 10**-6
k_0= 8.99 * 10**9

# berekening
f = k_0 * q_1 * q_2 / r**2

# uitvoer
print(f)
