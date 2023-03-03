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
       st.write("note: resminizi yüzünüz billi olsun")
       file = st.file_uploader("lütfen geçerli bir fotograf ekleyen",help=None)
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
            
            

footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
 #MainMenu {visibility: hidden;}
</style>
<div class="footer">
<p>Developed by ALSAMARRAE</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('2.jpg')

if __name__ == "__main__":
    main()
 