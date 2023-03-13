import streamlit as st


st.markdown("""#ASHA FM""" )

video_file = open('video-1626791370.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
