# pyton -m streamlit run demo.py
import streamlit as st
st.sidebar.title("Student Info")
batch = st.sidebar.selectbox("Select Batch",["B1","B2","B3","B4"])
gender = st.sidebar.radio("Select Gender",['Male','Female'])

subject = st.sidebar.selectbox('Select Subject',['Python','Fsd'])

if(subject=='Python'):
    st.title("Welcome to Python world")
    name = st.text_input("Enter Name")
    enroll = st.number_input("Enter Enroll")
else:
    st.title("Welcome to Fsd World")
    name = st.text_input("Enter Name")
    enroll = st.number_input("Enter Enroll")

submit = st.button("Submit")
if submit:
    st.write(name)
    st.write(gender)
    st.write(batch)
    st.write(enroll)
    st.write(subject)
