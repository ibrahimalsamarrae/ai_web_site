import streamlit as st

st.title("Hakkında")






footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 60%;
background-color: black;
color: white;
text-align: center;
}
 #MainMenu {visibility: hidden;}
</style>

<div class="footer">
</center><p> by ALSAMARRAE</p><center> 
</div>

"""

st.markdown(footer, unsafe_allow_html=True)

 