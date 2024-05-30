number = input()
digits = [int(i) for i in number]

def biggest_num(a, b, c, d):
    return max(a, b, c, d)


plus = digits[0] + digits[1] + digits[2]
multiplier = digits[0] * digits[1] * digits[2]
plus_multiplier = digits[0] + digits[1] * digits[2]
multiplier_plus = digits[0] * digits[1] + digits[2]

print(biggest_num(plus, multiplier, plus_multiplier, multiplier_plus))

