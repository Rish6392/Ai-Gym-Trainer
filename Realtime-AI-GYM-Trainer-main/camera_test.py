import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="Camera Test")

st.title("📷 Camera Test")

ctx = webrtc_streamer(
    key="camera-test",
    mode=WebRtcMode.SENDRECV,
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
    async_processing=True,
)

st.write("Camera playing:", ctx.state.playing)