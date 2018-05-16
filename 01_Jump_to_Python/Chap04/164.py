f = open('새파일txt', 'r', encoding='UTF-8')

lines = f.readlines()

for line in lines:
    print(line, end='')

f.close()