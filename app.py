import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))

col1,col2,col3,col4,col5,col6 = st.columns(6)

with col1:
    Age= st.number_input("Age")
with col2:
    SystolicBP	= st.number_input("SystolicBP")
with col3:
    DiastolicBP = st.number_input("DiastolicBP")
with col4:
    BS = st.number_input("BS")
with col5:
    BodyTemp = st.number_input("BodyTemp")
with col6:
    HeartRate = st.number_input("HeartRate")




if st.button('Predict Probability'):
    input_df = pd.DataFrame({ 'Age' : [Age], 'SystolicBP': [SystolicBP], 'DiastolicBP': [DiastolicBP], 'BS': [BS],'BodyTemp':[BodyTemp],'HeartRate':[HeartRate]})

    st.table(input_df)

    result= pipe.predict(input_df)
    result2= pipe.predict_proba(input_df)

    
    st.header("Risk Prediction" + "- " + str(result[0]))

    st.header("Classes:" + " ['high risk' 'low risk' 'mid risk']")
    st.header("Risk Probability" + "- " + str(result2))