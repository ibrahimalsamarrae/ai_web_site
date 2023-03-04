import streamlit as st
from PIL import Image
import tensorflow as tf
from streamlit_option_menu import option_menu

img= Image.open("1.jpg")
st.set_page_config(
        page_title="ANA SAYFA",
        page_icon=img
    )

st.title("AI PROGRAMIZA HOŞ GELDİNİZ💫")
st.sidebar.success("Yukarıdan bir sayfa seçin.")




selected = option_menu("Menu", ['ANA SAYFA',"kamera'ile çek"], 
icons=['house', 'bi bi-camera-fill'], default_index=0)

if selected == "ANA SAYFA":
    st.write("lütfen yüzünüz resmi yükleyin")
    
  
   ################################################################
elif selected == "kamera'ile çek":
    st.title("kamera' ile resim çek ve sonoç al")

    file = st.camera_input("")

    submit = st.button("sonuç")
           
          
    if submit:
        if file is not None:
            st.image(file, width=300)
            image = Image.open(file)
            
            image = tf.keras.preprocessing.image.img_to_array(image)
            image = tf.image.resize(image, [224,224]) 
            image = image / 255.0      
            image = tf.expand_dims(image, axis=0)
            
            model = tf.keras.models.load_model("yasmodel.h5")
            age = model.predict(image)
            age=st.markdown("## yaşınız %i gibi görünüyor" %age[0][0])

def main():

        
       st.write("note: resminizi yüzünüz billi olsun")
       file = st.file_uploader("",help=None)
       submit1 = st.button("sonuç al")
       
      
       if submit1:
           if file is not None:
                st.image(file)
                image = Image.open(file)
                
                image = tf.keras.preprocessing.image.img_to_array(image)
                image = tf.image.resize(image, [224,224]) 
                image = image / 255.0      
                image = tf.expand_dims(image, axis=0)
                
                model = tf.keras.models.load_model("yasmodel.h5")
                age = model.predict(image)
                age=st.markdown("## yaşınız %i gibi görünüyor" %age[0][0])

            
            

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
import time

with st.spinner('Yükleniyor...'):
    time.sleep(3)
st.success('Done!')

if __name__ == "__main__":
    main()
 