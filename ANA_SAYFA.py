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

page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.redbull.com%2Fimages%2Fc_fill%2Cw_1200%2Ch_630%2Cg_auto%2Cf_auto%2Cq_auto%2Fredbullcom%2F2021%2F1%2F26%2Fxisgmjrbpkn04vxnqjfa%2Fyapay-zeka&imgrefurl=https%3A%2F%2Fwww.redbull.com%2Ftr-tr%2Fyapay-zeka-teknolojileri-hakkinda-bir-deney&tbnid=qlPm8bT20UgoHM&vet=12ahUKEwjxx4m188D9AhVl9bsIHb2UBwgQMygIegUIARDIAQ..i&docid=P15QJK10abmqtM&w=1200&h=630&q=yapay%20zeka&ved=2ahUKEwjxx4m188D9AhVl9bsIHb2UBwgQMygIegUIARDIAQ");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
 