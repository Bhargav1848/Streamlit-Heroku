import streamlit as st;

st.title("Multiplication of 2 Numbers")

user_input1 = st.number_input("Enter First Number:",)
user_input2= st.number_input("Enter Second Number:",)

st.title(user_input1*user_input2);