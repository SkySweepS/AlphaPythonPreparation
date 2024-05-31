n = input().split(",")
n_list = []
for i in range(len(n)):
    count = i + 1

    if str(count) not in n:
        n_list.append(str(count))

print(",".join(n_list))