list_1 = input().split(",")
list_2 = input().split(",")
final_list = []
for i in range(len(list_1)):
    final_list.append(list_1[i])
    final_list.append(list_2[i])
print(",".join(final_list))