n = int(input())

new = 1
new_list = []
count = n - 1
for i in range(1, n + 1):
    new *= 2
    row = new
    count = n - i
    for i1 in range(1, n):
        if count >= n - i1:
            new_list.append(row)
            count -= 1
        row *= 2

print(sum(new_list))
