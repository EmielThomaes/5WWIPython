uitvoer = '{} + {} = {}'
print(uitvoer.format(3, 4, 7))
print(uitvoer.format(-1, 3, 10))

uitvoer = '{0} + {0} = {1}'
print(uitvoer.format(3, 6))

uitvoer = '{:d} + {:f} = {:d}'
print(uitvoer.format(1, 1, 2))

uitvoer = '{0:d} + {0:f} = {1:d}'
print(uitvoer.format(1, 2))

uitvoer = '{0:d} + {0:.2f} = {1:d}'
print(uitvoer.format(1, 2))

uitvoer = '{:d} + {:9.9f} = {:d}'
print(uitvoer.format(1, pow(2, 0.5), 2))

uitvoer = '{:d} + {:9.2f} = {:d}'
print(uitvoer.format(1, pow(2, 0.5), 2))

uitvoer = '{:d} + {:^9.2f} = {:d}'
print(uitvoer.format(1, pow(2, 0.5), 2))



from math import sqrt
print(sqrt(2))

from math import pi
print(pi)



import random
print(random.random())

from random import uniform, random, randint, seed
seed(1233)
print(random())
print(uniform(1, 5))
print(randint(3, 100))
