import streamlit as st
import pandas as pd
import numpy as np 
import pickle

#load the model 
with open('first_hypertension_model.pkl','rb') as file:
    model = pickle.load(file)
 # streamlit UI
st.title('Presences of Hypertention')
st.write('This app predicts the **Presence** type!')
st.write('Please input the following parameters')

#input form

age = st.number_input('Age',value=0)
sex = st.selectbox("Select Gender 0 for femal and 1 for male:", [0, 1])
cp = st.number_input('CP',value=0)
trestbps = st.number_input('Trestbps',value=0)
chol = st.number_input('Chol',value=0)
fbs = st.number_input('FBS',value=0)
restecg = st.number_input('Restecg',value=0)
thalach = st.number_input('Thalach',value=0)
exang = st.number_input('Exang',value=0)
oldpeak = st.number_input('Oldpeak',value=0)
slope = st.number_input('Slope', value=0)
ca = st.number_input('Ca', value=0)
thal = st.number_input('Thal', value=0)

#prediction 
if st.button('Predict'):
      user_input = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
      prediction = model.predict(user_input)
      BP_mapping = {0: 'Non Hypertensive', 1: 'Hypertensive',}
      st.write(prediction)
      predicted = BP_mapping.get(int(prediction[0]), 'unknown')
      st.write(f'The predicted species is: {predicted}')

      # footer 
      st.write('Made with Streamlit')
