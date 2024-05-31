n = int(input())
my_dict = {}
for i in range(n):
    num = int(input())
    if not num in my_dict:
        my_dict[num] = 1
    else:
        my_dict[num] += 1
max_key = 0
min_num = 0
for i in my_dict:
    if my_dict[i] > min_num:
        min_num = my_dict[i]
        max_key = i

print(f"{max_key} ({min_num} times)")