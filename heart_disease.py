pip install scikit-learn
import numpy as np
import pickle
import streamlit as st
import sklearn

loaded_model = pickle.load(open('model.sav','rb'))

def heart_predict(input_data):
    input_array = np.asarray(input_data)
    re=input_array.reshape(1,-1)
    prediction=loaded_model.predict(re)
    print(prediction)
    
    if prediction[0] == 1:
        return 'Heart Disease Infected'
    else:
        return 'No Heart Disease Infected'

def main():
    st.title('Know Your Risk for Heart Disease !')

    age = st.text_input('Age')
    sex = st.text_input('Sex (0=Female 1=Male)')
    cp = st.text_input('Chest Pain Type (0,1,2,3)')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholestrol mg/d;')
    fbs = st.text_input('Fasting Blood Sugar > 120 (0=False 1=True)')
    restecg = st.text_input('Resting Electrocardiographic (0,1,2)')
    thalach = st.text_input('Maximum Heart Rate')
    exang = st.text_input('Exercise Induced Angina (0=No 1=Yes)')
    oldpeak = st.text_input('ST Depression Induced')
    slope = st.text_input('The Slope Of The Peak Exercise ST Segment')
    ca = st.text_input('Number Of Major Vessels')
    thal = st.text_input('Thal (0=Normal 1=Fixed Defect 2=Reversable Defect)')

    diagnose = ''

    if st.button('Heart Disease Result'):
        diagnose = heart_predict([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnose)

if __name__ == '__main__':
    main()
