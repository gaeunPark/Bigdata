my_data = ['body', 'foo', 'bar']

for i, name in enumerate(my_data):
    print(i, name)
for name in enumerate(my_data):
    print(name)

def positive(x):
    return x>0

print(list(filter(positive, [1, -3, 2, 0, 0, -5, 6] )))



