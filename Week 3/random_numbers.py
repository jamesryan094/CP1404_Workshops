import random

#randint open range, takes only integers
print(random.randint(5, 20))

#randrange, half open, ints only, odd numbers between 3 and 9
print(random.randrange(3, 10, 2))

#uniform, rand range with float instead of ints, half open
print(random.uniform(2.5, 5.5))