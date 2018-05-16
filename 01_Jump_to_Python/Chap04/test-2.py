# f = open("sample.txt", 'w', encoding='utf-8')

f = open("sample.txt", 'r', encoding='utf-8')
lines=f.readlines()
f.close()

total=0
for line in lines:
    score=int(line)
    total += score
print(lines)
average=total/len(lines)


f= open("result.txt", 'w', encoding='utf-8')
f.write("총합: %d" %average)
f.close()