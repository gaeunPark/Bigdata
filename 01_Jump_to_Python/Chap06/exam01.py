
word = input("문자열 입력: ");

result=""
ch = word[0]
count = 0
idx = 0
while(True):
    if ch == word[idx]:
        count += 1
    else:
        result = result + ch + str(count)
        ch = word[idx]
        count = 1

    idx += 1
    if idx >= len(word):
        result = result + ch + str(count)
        break


print(result)