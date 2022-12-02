import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/dhiem/Documents/model/model.sav','rb'))

input_data = (43,0,0,132,341,1,0,136,1,3,1,0,3)
input_array = np.asarray(input_data)
re= input_array.reshape(1,-1)

prediction=loaded_model.predict(re)
print(prediction)

if prediction[0] == 1:
    print('Kamu terindikasi penyakit jantung')
else:
    print('Kamu bebas penyakit jantung')