import streamlit as st
from datetime import date,time
import random as r
with st.expander("Click here for more info"):
    st.write("Kem")
    st.write("Cho")
    st.write("Majama??")

date = st.date_input("Enter date",min_value=date(2024,1,1))

st.sidebar.title("Student Info")

name =st.sidebar.text_input('Enter Name')

if name:
    no = r.randint(0,100)
    if(no>50):
        st.image("download.jfif")
    else:
        st.image('images.jfif')
