import streamlit as st
st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:150px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">ASHA FM</p>', unsafe_allow_html=True)

video_file = open('data/video-1626791370.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


st.write("  ")
st.write("  ")


st.markdown("""
<style>
.mid-font {
    font-size:30px;
    font-weight: thin;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


with st.container():
   st.markdown('<p class="mid-font">SOLIDARITY & SELECTAS brought by @ashasoundsystem - coming soon.</p>', unsafe_allow_html=True)

st.write("  ")
st.write("  ")
st.write("  ")
st.write("  ")

audio = st.file_uploader("UPLOAD YOUR MUSIC", type=["mp3, WAV, AIFF"])
st.write("  ")
st.write("  ")
images = st.file_uploader("UPLOAD YOUR IMAGES", type="jpg, png")
st.write("  ")
st.write("  ")
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

st.image(image='https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png', caption=None, width=75, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write("Follow us on Instagram [@ASHA_FM](https://www.instagram.com/_asha_fm_/)")
