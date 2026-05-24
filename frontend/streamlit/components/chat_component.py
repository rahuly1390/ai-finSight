import streamlit as st

from api_client import (
    ask_agent
)

from components.risk_dashboard import (
    render_dashboard
)


def render_chat():

    st.subheader(
        "💬 Financial AI Assistant"
    )

    query = st.text_input(
        "Ask financial question"
    )

    if st.button(
        "Analyze"
    ):

        if query:

            with st.spinner(
                "Analyzing..."
            ):

                result = (
                    ask_agent(
                        query
                    )
                )

            st.success(
                "Analysis Complete"
            )

            render_dashboard(
                result[
                    "analysis"
                ]
            )

            st.subheader(
                "📌 Retrieved Evidence"
            )

            for doc in result[
                "retrieved_docs"
            ]:

                st.write(
                    f"• {doc[:200]}"
                )