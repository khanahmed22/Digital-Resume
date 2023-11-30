from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Muhammad Ahmed Khan",page_icon=":sunrise",layout = "wide")

def local_css(file_name):
     with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
def load_lottieurl(url):
     r= requests.get(url)
     if r.status_code != 200:
          return None
     return r.json()
def load_lottieurl1(url):
     r= requests.get(url)
     if r.status_code != 200:
          return None
     return r.json()
lottie_assets = "https://lottie.host/605db1a1-3543-4765-8426-bbf0be43bbfa/9FRlGfcw7Q.json"
lottie_assets2 = "https://lottie.host/1e7b106f-db7e-4315-a8fe-d8e923a44b7c/F7HaKg5aCV.json"
image_WW = Image.open("WeatherWonderPromo.png")
image_DD = Image.open("DUNDUNDUNPROMO.png")
image_AA = Image.open("AhmedGPT PROMO.png")
image_MM = Image.open("ahmed23.png")

selected = option_menu(
    menu_title=None,
    options=["Home","Projects","Contact"],
    icons=["house","book","envelope"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#293d75"},
        "icon": {"color": "white", "font-size": "21px"},
        "nav-link": {
            "font-size": "21px",
            "text-align": "left",
            "margin": "7px",
            "--hover-color": "#1f83ed",
        },
        "nav-link-selected": {"background-color": "#030557"},
    },

)        



#Header
if selected == "Home":
    with st.container():
        text_column, image_column = st.columns((2, 1))
        with image_column:
            st.image(image_MM,width=200)
        with text_column:
            
            st.subheader("Hi, I am Ahmed 👋")
            st.subheader("Flutter Developer | Python Enthusiast | Microsoft Azure Consultant | Electrical Engineer | NED'23")
            st.write("Dedicated and skilled Python and Flutter developer with a profound understanding of cloud technologies. With a solid foundation in software development, I bring forth a wealth of expertise in crafting efficient and scalable solutions. My proficiency in Python allows me to create robust systems, while my adeptness in Flutter ensures the development of seamless cross-platform applications.")
            

    with st.container():
        st.write("---")
        left_column,right_column = st.columns(2)
        with left_column:
            st.header("Skills")
            st.write("##")
            st.write(
                """
                #️⃣**Programming Languages**: Proficient in Python, Dart (Flutter).

                📱**Mobile App Development**: Experienced in Flutter for cross-platform mobile applications.

                ☁️ **Cloud Technologies**: Microsoft Azure.

                💡**Problem-Solving**: Adept at identifying and resolving complex technical challenges.

                🖥**Proficient in Backend Solution**: Firebase


                """
            

            )
            st.write("###")
        with right_column:
            st_lottie(lottie_assets,height = 300,key = "coding")      

if selected == "Projects":
    with st.container():
        
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(image_DD)
        with text_column:
            st.subheader("Dun Dun Dun: The app that makes notetaking a breeze")
            st.write(
                """
                This is an intuitive notetaking app made using Flutter. It uses Firebase Authentication to authenticate users and allows them to create notes in their respective accounts. It uses Firestore Database to store the users Note Data.

                """
            )
            st.markdown("[Check out on Github >](https://github.com/khanahmed22/DunDunDun)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(image_WW)
        with text_column:
            st.subheader("Weather Wonder: Your Weather Asistant")
            st.write(
                """
                A beautiful weather app made using KivyMD that uses OpenWeather API to fetch weather.
                """
            )
            st.markdown("[Check out on Github >](https://github.com/khanahmed22/WeatherWonder)")
            
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(image_AA)
        with text_column:
            st.subheader("AhmedGPT: Personal AI Assistant")
            st.write(
                """
                Meet AhmedGPT, your AI assistant that will answer all your queries. Why bother googling it when you can "AhmedGPT" it.
                """
            )
            st.markdown("[Check out on Github >](https://github.com/khanahmed22/AhmedGPT)")
            st.write("###")

if selected == "Contact":            
    with st.container():
        
        st.header("Get In Touch With Me!")
        st.write("##")
        contact_form = """

            <form action="https://formsubmit.co/ahmed.mak26@outlook.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>




                    """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_assets2,height = 300,key = "message")
        st.write("###") 
st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://twitter.com/khanahmed265" target="_blank">
                <img src="https://img.icons8.com/color/48/000000/twitter.png" alt="Twitter" />
            </a>
            &nbsp;&nbsp;
            <a href="https://www.linkedin.com/in/muhammad-ahmed-khan-109079275/" target="_blank">
                <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" />
            </a>
            &nbsp;&nbsp;
            <a href="https://github.com/khanahmed22" target="_blank">
                <img src="https://img.icons8.com/color/48/000000/github--v1.png" alt="GitHub" />
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

