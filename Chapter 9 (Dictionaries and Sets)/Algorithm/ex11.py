import pickle
dct = {'Игорь': 12}
data = open('mydata.dat', 'wb')
pickle.dump(dct, data)
data.close()

