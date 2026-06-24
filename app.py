import streamlit as st

st.set_page_config(
    page_title="Produção Jaboatão",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

col1, col2 = st.columns(2)

with col1:
    st.metric("JEEP 551", "551", "-9")
    st.metric("GIRO LF", "6")
    st.metric("RETRABALHO", "1")

with col2:
    st.metric("JEEP 226", "226", "-26")
    st.metric("GIRO LF", "23")
    st.metric("RETRABALHO", "7")

col3, col4 = st.columns(2)

with col3:
    st.metric("FIAT 521", "521", "-11")
    st.metric("GIRO LF", "10")
    st.metric("RETRABALHO", "3")

with col4:
    st.metric("FIAT 363", "363", "-10")
    st.metric("GIRO LF", "13")
    st.metric("RETRABALHO", "5")
