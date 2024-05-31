text = input()

def check_text(text):
    count = 0
    max_count = 0
    for i in range(len(text)):
        if text[i] == '.':
            break
        if text[i].isdigit():
            count = 0
        elif text[i].isalpha():
            count = 0
        elif text[i] == ' ':
            count = 0
        else:
            count += 1
            if count > max_count:
                max_count = count
    return max_count


print(check_text(text))
