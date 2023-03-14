import streamlit as st
from PIL import Image
import base64


st.set_page_config(layout="wide")


##HEADING
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write(' ')

with col2:
    image = Image.open('data/ASHAFMLOGO.PNG')
    st.image(image, caption=None, width=650)

with col3:
    st.write(' ')

with col4:
    st.write(' ')

with col5:
    st.write(' ')



##ASHA FM DEMO DAY VIDEO
video_file = open('data/video-1626791370.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


st.write("  ")
st.write("  ")

##DESCRIPTION/BACKGROUND FORMAT
st.markdown("""
<style>
.mid-font {
    font-size:30px;
    font-weight: thin;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

##DESCRIPTION/BACKGROUND TEXT
with st.container():
   st.markdown('<p class="mid-font">SOLIDARITY & SELECTAS brought by @ashasoundsystem - coming soon.</p>', unsafe_allow_html=True)

st.write("  ")
st.write("  ")

##TEAM
col1, col2, col3, col4 = st.columns(4)

st.markdown("""
<style>
.header-font {
    font-size:90px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

with col1:
   st.markdown('<p class="mid-font">MAADHAV</p>', unsafe_allow_html=True)
   file_ = open("data/maadhavsmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

with col2:
   st.markdown('<p class="mid-font">SOPHIA</p>', unsafe_allow_html=True)
   file_ = open("data/sophiasmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

with col3:
   st.markdown('<p class="mid-font">JACK</p>', unsafe_allow_html=True)
   file_ = open("data/jacksmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)


with col4:
   st.markdown('<p class="mid-font">MATEA</p>', unsafe_allow_html=True)

   file_ = open("data/mateasmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)




st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")

##UPLOAD AUDIO BUTTON
audio = st.file_uploader("UPLOAD YOUR MUSIC", type=["mp3, WAV, AIFF"])
st.write("  ")
st.write("  ")

##PLACEHOLDER FOR IMAGE UPLOAD - STRETCH GOAL
##images = st.file_uploader("UPLOAD YOUR IMAGES", type="jpg, png")
##st.write("  ")
##st.write("  ")
with open("data/video-1626791370.mp4", "rb") as file:
    btn = st.download_button(
            label="DOWNLOAD YOUR VIDEO",
            data=file,
            file_name="YOUR MUSIC VIDEO",
            mime="mp4"
          )

st.write("  ")
st.write("  ")
st.write("  ")


##SOCIAL MEDIA HANDLE AND WEBSITE LINK
col1, col2,  col3, col4, col5, col6, col7, col8 = st.columns(8)

with col4:
   st.image(image='https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png', caption=None, width=45, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
   st.write("[@ASHA_FM](https://www.instagram.com/_asha_fm_/)")

with col5:
   image = Image.open('data/circlelogosmall.jpeg')
   st.image(image, caption=None, width=45, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
   st.write("[ASHA.FM](https://www.asha.fm)")
