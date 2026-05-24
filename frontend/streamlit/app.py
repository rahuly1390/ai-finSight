import streamlit as st

from components.upload_component import (
    render_upload
)

from components.chat_component import (
    render_chat
)

st.set_page_config(
    page_title="FinSight AI",
    layout="wide"
)

st.title(
    "💰 FinSight AI"
)

st.caption(
    "Enterprise Financial Intelligence Platform"
)

tab1, tab2 = st.tabs(
    [
        "Upload Documents",
        "Financial Assistant"
    ]
)

with tab1:

    render_upload()

with tab2:

    render_chat()