import streamlit as st


def render_dashboard(
    analysis
):

    st.subheader(
        "📊 Risk Analysis"
    )

    st.info(analysis)