import streamlit as st
from PIL import Image

st.title("sonuçu yazdır")
file =st.session_state("my_input")
age =st.session_state("age")
if file is not None:
    st.image(file, width=300)
    image = Image.open(file)
    st.markdown("## yaşınız %i gibi görünüyor" %age[0][0])
    
       
#st.write("You have entered", st.session_state["my_input"])
