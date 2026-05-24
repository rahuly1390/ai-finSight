import streamlit as st

from api_client import (
    upload_document
)


def render_upload():

    st.subheader(
        "📄 Upload Financial Documents"
    )

    uploaded_file = (
        st.file_uploader(
            "Upload PDF / CSV / TXT",
            type=[
                "pdf",
                "csv",
                "txt"
            ]
        )
    )

    if uploaded_file:

        with st.spinner(
            "Uploading..."
        ):

            result = (
                upload_document(
                    uploaded_file
                )
            )

        st.success(
            "Document uploaded"
        )

        st.json(result)