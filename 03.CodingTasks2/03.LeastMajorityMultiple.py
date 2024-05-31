import math
from itertools import combinations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

num_list = [a, b, c, d, e]


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def lcm2(a, b, c):
    return lcm(a, lcm(b, c))
min_num = 10000000
for combo in combinations(num_list, 3):
    curr_lcm = lcm2(*combo)
    if curr_lcm < min_num:
        min_num = curr_lcm
print(min_num)
