def string_num(num):
    count = 0
    for i in str(num):
        if int(i) == 0:
            count += 1
        if int(i) != 0 and num % int(i) == 0:
            count += 1
    if count == len(str(num)):
        return True
    else:
        return False

count = 0
n = input().split()
for i in range(int(n[0]), int(n[1]) + 1):
    if string_num(i):
        count += 1

print(count)