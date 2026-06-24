import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}

.card {
    border: 1px solid white;
    padding: 30px;
    text-align: center;
    margin-bottom: 20px;
}

.numero {
    color: white;
    font-size: 60px;
    font-weight: bold;
}

.verde {
    color: lime;
    font-size: 30px;
}

.vermelho {
    color: red;
    font-size: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="verde">IMPOSTADA 120</div>
        <div class="numero">551</div>
        <div class="vermelho">DELTA -38</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="verde">IMPOSTADA 204</div>
        <div class="numero">226</div>
        <div class="vermelho">DELTA -64</div>
    </div>
    """, unsafe_allow_html=True)
