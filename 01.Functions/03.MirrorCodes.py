numbers = input().split()
num_list = []
num = ''
for i in numbers:
    for i1 in range(len(i) - 1, -1, -1):

        num += i[i1]
    num_list.append(int(num))
    num = ''
print(max(num_list))
