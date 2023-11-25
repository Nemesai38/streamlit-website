from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="🇩🇪", layout="wide")

# To launch the lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------ LOAD ASSETS ----------
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("~/repos/streamlit-website/images/pngwing.com.png")
img_lottie_animation = Image.open("images/Turmeric-Rice-main.jpg")

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
            - making people understand the truth of what is going on in the world and this will set them free, as it is know "The truth shall set you free
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
        st.image(img_contact_form)
        # insert image
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to stop going to church!
            Lower your prioritization of Money.
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video.....](https://www.youtube.com/watch?v=3f3gLiruWGo)")