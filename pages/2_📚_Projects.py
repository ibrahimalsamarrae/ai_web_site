import streamlit as st
from PIL import Image

st.title("sonuçu yazdır")

image = Image.open(st.session_state("my_input")) 
    
       
#st.write("You have entered", st.session_state["my_input"])
