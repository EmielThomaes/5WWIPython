# invoer

i_l = float(input('i_l = '))
f_i = float(input('f_i = '))
L = int(input('L = '))

# berekening

R = 2
f_c = 0.2

N = int(R * i_l * f_i * f_c * L)

# uitvoer

print('samenlevingen in de melkweg waarmee we zouden kunnen communiceren: ' + str(N))
