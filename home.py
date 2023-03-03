import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<style>
    .headstyle {
        color: rgb(255, 255, 255);
        font-variant: petite-caps;
        background-color: rgb(0, 0, 0, 0.8);
        margin-bottom: 0px
    }

    .divstyle {
        border-radius: 10px 10px 10px 10px;
        margin-left: 1px;
        margin-right: 1px
    }
</style>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">

    <title>AI' ILE YAŞINIZI BiLİN</title>
</head>

<body>


    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">AI' ILE YAŞINIZI BİLİN</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">


                    <li class="nav-item">
                        <a class="nav-link " aria-current="page" href="templates/Hakkında.html">Hakkında</a>
                    </li>
                      <li class="nav-item">
                          <a class="nav-link " aria-current="page" href="templates/uygulama.html">programa giriş</a>
                      </li>


                   
                </ul>
            </div>
        </div>
    </nav>

    <h1 class='text-center py-3'
            style="font-variant: petite-caps;margin-bottom:0px">
            <b><i>Yapay Zeka ile Yaşınızı Bilin</i></b>
    </h1>

    <div class="row" style="font-size: 20px;padding: 0px 50px 50px 50px;">
        <p><b> Yapay zeka ile görünüşünüze göre kaç yaşında göründüğünüzü öğrenebilirsiniz.</p>


        <div class='divstyle' style='margin:40px 20px 60px 20px'>
            <div class="row py-3">
                <div class="col md-3">
                    <h3 class='text-center py-3 headstyle' style="font-size: 18px;"><b>programa giriş</b></h3>
                    <a href="/templates/uygulama.html"><img src="static/icons/ana_sayfa.jpeg" class="img-fluid mx-auto d-block"></a>
                </div>
      
      
            </div>
        </div>



        <h3 class='text-center py-3'
            style="color: rgb(255, 255, 255);font-variant: petite-caps;background-color: rgb(0, 0, 0);margin-bottom:0px">
            <b><i>AI nedir</i></b>
        </h3>
        <div class="row py-3"
            style='margin-bottom: 30px;'>
            <div class="col">
                <p class="text-left" style='font-size:18px'>
          
          AI, en basit ifadeyle, görevleri yerine getirmek için insan zekasını taklit eden ve topladığı bilgilere göre kendini geliştirebilen sistem veya cihazları ifade eder.
                </p>
            </div>
            <div class="col">
            
                <img src="static/yapay_zeka.jpg" class="img-fluid rounded mx-auto d-block" alt="...">
            </div>
        </div>

        <h3 class='text-center py-3'
            style="color: rgb(255, 255, 255);font-variant: petite-caps;background-color: rgb(0, 0, 0);margin-bottom:0px">
            <b><i>Machine Learning nedir</i></b>
        </h3>
        <div class="row py-3" style='margin-bottom: 30px'>
            <div class="col">
                <p class="text-left" style='font-size:18px'>
                    Makine öğrenimi (ML), yazılım uygulamalarının, bunu yapmak için açıkça programlanmasına gerek kalmadan sonuçları tahmin etmede daha doğru hale gelmesine izin veren bir yapay zeka (AI) türüdür.
                </p>
            </div>
            <div class="col">
                <img src="/static/makine.jpg" class="img-fluid rounded mx-auto d-block" alt="...">
            </div>
        </div>



    <footer class='text-light bg-dark position-relative '>
        <p class='text-center py-1 my-0'>
            copyright&copy;ALSAMARRAE 
        </p>
    </footer>

  <!-- Option 1: Bootstrap Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
      crossorigin="anonymous"></script>
</body>
    """,
    width=800, height=1000, scrolling=True
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 