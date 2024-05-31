n = int(input())
height = 2 * n - 1

def upper_road(n):
    for i in range(n):
        for i1 in range(n):
            if i1 == i:
                print("*", end="")
            else:
                print(".", end="")
        print()


def lower_road(n):
    for i in range(n - 1, 0, -1):
        for i1 in range(n):
            if i1 == i - 1:
                print("*", end="")
            else:
                print(".", end="")
        print()


upper_road(n)
lower_road(n)