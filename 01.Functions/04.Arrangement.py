numbers = input().split()
num_list = []
for i in range(len(numbers)):
    num_list.append(int(numbers[i]))


def sort(num_list):
    if num_list[0] < num_list[1] < num_list[2] < num_list[3]:
        print("Ascending")
    elif num_list[0] > num_list[1] > num_list[2] > num_list[3]:
        print("Descending")
    else:
        print("Mixed")

sort(num_list)

