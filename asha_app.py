import streamlit as st
from PIL import Image
import base64


st.set_page_config(layout="wide")


##HEADING
file_ = open("data/movinglogo.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
unsafe_allow_html=True)



##ASHA FM DEMO DAY VIDEO
video_file = open('data/vidasha.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



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

st.markdown("""
<style>
.big-font {
    font-size:40px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

##DESCRIPTION/BACKGROUND TEXT
col1, col2, col3 = st.columns(3)
with col1:
    st.write("  ")

with col2:
    image = Image.open('data/solidarity.png')
    st.image(image)

with col3:
    st.write("  ")


st.write("  ")
st.write("  ")

st.markdown("""
<style>
.desc-font {
    font-size:20px;
    font-weight: thin;
}
</style>
""", unsafe_allow_html=True)

with st.expander("READ MORE ABOUT OUR AUDIOVISUAL INTERACTIVE PROJECT:", expanded=True):
    file_ = open("data/description.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="description">',
    unsafe_allow_html=True,)

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
    f'<img src="data:image/gif;base64,{data_url}" alt="maadhav">',
    unsafe_allow_html=True,
)

with col2:
   st.markdown('<p class="mid-font">SOPHIA</p>', unsafe_allow_html=True)
   file_ = open("data/sophiasmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="sophia">',
    unsafe_allow_html=True,
)

with col3:
   st.markdown('<p class="mid-font">JACK</p>', unsafe_allow_html=True)
   file_ = open("data/jacksmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="jack">',
    unsafe_allow_html=True,
)


with col4:
   st.markdown('<p class="mid-font">MATEA</p>', unsafe_allow_html=True)

   file_ = open("data/mateasmall.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="matea">',
    unsafe_allow_html=True,
)

st.write("  ")
st.write("  ")


##DEMO INSTRUCTIONS
st.markdown("""
<style>
.instr-font {
    font-size:25px;
    font-weight: thin;
    color: #000000;
    text-align: center;
    background-color: #FFFFFF;
    border-radius:2%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="instr-font">TO START, UPLOAD YOUR MUSIC FILE IN MP3/WAV FORMAT.</p>', unsafe_allow_html=True)
st.write("  ")


##UPLOAD AUDIO BUTTON
audio = st.file_uploader("UPLOAD YOUR MUSIC", type=["mp3, WAV, AIFF"])
st.write("  ")
st.write("  ")

##DEMO INSTRUCTIONS- DOWNLOAD
st.markdown('<p class="instr-font">NOW PRESS DOWNLOAD AND WATCH THE MAGIC UNFOLD.</p>', unsafe_allow_html=True)
st.write("  ")

##PLACEHOLDER FOR IMAGE UPLOAD - STRETCH GOAL
##images = st.file_uploader("UPLOAD YOUR IMAGES", type="jpg, png")
##st.write("  ")
##st.write("  ")

##DOWNLOAD BUTTON
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




##OUR WONDERFUL TAS
st.markdown('<p class="mid-font">BIG THANK YOU FROM THE ASHA FM TEAM TO OUR WONDERFUL LE WAGON TAS</p>', unsafe_allow_html=True)
st.write("  ")
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
    st.write("  ")

with col2:
   st.markdown('<p class="mid-font">CHARLOTTE</p>', unsafe_allow_html=True)
   file_ = open("data/charlottegif.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

with col3:
   st.markdown('<p class="mid-font">LORCAN</p>', unsafe_allow_html=True)
   file_ = open("data/lorcangif.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()
   st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)


with col4:
    st.write("  ")


st.write("  ")
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
