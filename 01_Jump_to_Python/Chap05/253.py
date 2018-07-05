import pickle

f=open("test.txt", 'wb', encoding='utf-8')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()