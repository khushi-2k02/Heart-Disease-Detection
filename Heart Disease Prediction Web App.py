# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:41:16 2023

@author: Khushi
"""

import numpy as np
#pickle is used to load the trained model 
import pickle
#streamlit is used for deploying the model
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Khushi/OneDrive/Desktop/All Semester Courses/5th Semester/Introduction to AIML/heart_trained_model.sav', 'rb'))

#creating a function for prediction

def heart_prediction(input_data):
     

    # change the input data to a numpy array
    input_data_as_array = np.asarray(input_data)

    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'The person does not have a Heart Disease'
    else:
        return 'The person has a Heart Disease'
    
def main():
    #giving a title to the web page
    st.title('Heart Disease Prediction Web App')
    
    #getting the input data from the user
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    
    age = st.text_input("Age")
    sex = st.text_input("Gender")
    cp = st.text_input("Chest pain type")
    trestbps = st.text_input("Resting blood pressure")
    chol = st.text_input("Serum cholestrol")
    fbs = st.text_input("Fasting blood sugar")
    restecg = st.text_input("Resting electrocardiographic results")
    thalach = st.text_input("Maximum heart rate achieved")
    exang = st.text_input("Exercise induced angina")
    oldpeak = st.text_input("Oldpeak-ST depression induced by exercise relative to rest")
    slope = st.text_input("Slope of the peak exercise ST segment")
    ca = st.text_input("Number of major vessels colored by flourosopy")
    thal = st.text_input("Thallium stress testing value")
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction([age, sex, cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
    


if __name__ == '__main__':
    main()
    
    
