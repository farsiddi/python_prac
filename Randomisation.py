# Mersenne twister

import random

# Random integer(both range values are included)
rand_int = random.randint(100, 199)
print(rand_int)

# Random floating point number(0.000000000 - 0.99999999999)
rand_float = random.random()
print(rand_float)
# In range 0 to 5
rand_float = rand_float * 5
print(rand_float)

places = ["Kashmir", "Himachal", "Assam", "Nagpur", "Lucknow", "Mumbai", "Lucknow"]
place = random.choice(places)
print(place)