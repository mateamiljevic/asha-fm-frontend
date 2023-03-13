import streamlit as st

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', STRETCH-SANS;
			}
			</style>
			"""

st.markdown("""#ASHA FM""")

video_file = open('video-1626791370.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
