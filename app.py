from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="🇩🇪", layout="wide")

# To launch the lottie animation build a website python and streamlit
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("/home/nemesis/repos/streamlit-website/style/app.css")

# ------ LOAD ASSETS ----------
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("/home/nemesis/repos/streamlit-website/images/pngwing.com.png")
img_lottie_animation = Image.open("/home/nemesis/repos/streamlit-website/images/tumeric.png")

# ------HEADER SECTION --------
with st.container():
    st.subheader("Hi, I am Abdul 🇩🇪 :wave:")
    st.title("A Veteran from Nigeria")
    st.write("I am passionate about truth and the world becoming a better place")
    st.write("[Learn More >](https://www.google.com)")

# ----- WHAT I DO ------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Website I teach how one can grow his/her spirituality to higher levels by:
            - moving away from religion and focusing on what really matters.
            - healing body through feeding which in turn heals the mind.
            - making people understand the truth of what is going on in the world and this will set them free, as it is know "The truth shall set you free".
            - linking people with similar informations and other great teachers, making them aware we are not alone.
            
            If this sounds interesting to you, consider subscribing and organizing a personal session.
            """
        )
        st.write("[Click to Register >](https://www.archlinux.org)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.write("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation, width=500)
    with text_column:
        st.subheader("Being your greatest Version")
        st.write(
            """
            Learn how to stop going to church!
            Lower your prioritization of Money.
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video.....](https://www.youtube.com/watch?v=3f3gLiruWGo)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Starting a new path")
        st.write(
            """
            Increase your luck chances.
            In this tutorial, Build your spiritual senses by feeding right
            """
        )
        st.markdown("[Watch Video.....](https://www.youtube.com/watch?v=g5PPN51-0no)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/pappysouls@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Yourmessage here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()