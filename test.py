import pickle

a = pickle.load(open('sentences.dat','rb'))
b = pickle.load(open('heads.dat','rb'))

print(len(a[0]))

print(len(b[0]))

print(b[0])
