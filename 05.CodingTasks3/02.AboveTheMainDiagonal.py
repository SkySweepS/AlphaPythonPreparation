import math

n = int(input())
for col in range(1, n + 1):
    start = 1
    for row in range(1, col + 1):
        print(int(math.pow(start, 2)), end=" ")
        start = int(math.pow(start, 2))
    print()