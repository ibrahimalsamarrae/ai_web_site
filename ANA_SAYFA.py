import streamlit as st
from PIL import Image
import tensorflow as tf
img= Image.open("1.jpg")
st.set_page_config(
        page_title="ANA SAYFA",
        page_icon=img
    )

st.title("AI PROGRAMIZA HOŞ GELDİNİZ💫")
st.sidebar.success("Select a page above.")


def main():
        
       st.header("Görünüşüne göre yaşını bil")
       st.write("Öğrenmek için aşağıya kendi resminizi yükleyin! ")
       file = st.file_uploader("Upload Photo")
       if file is not None:
            st.image(file, width=300)
            image = Image.open(file)
            
            image = tf.keras.preprocessing.image.img_to_array(image)
            image = tf.image.resize(image, [224,224]) 
            image = image / 255.0      
            image = tf.expand_dims(image, axis=0)
            
            model = tf.keras.models.load_model("yasmodel.h5")
            age = model.predict(image)
            
            st.markdown("## yaşınız %i gibi görünüyor" %age[0][0])
            
            
            
if __name__ == '__main__':
     main()
        


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Heflin Stephen Raj S</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)