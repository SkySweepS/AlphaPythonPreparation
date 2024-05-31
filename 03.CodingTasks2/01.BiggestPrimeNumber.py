def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())

for i in range(n, 0, -1):
    if is_prime(i):
        print(i)
        break



