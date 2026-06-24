import streamlit as st
from datetime import datetime
st.set_page_config(
    page_title="Produção Jaboatão",
    layout="wide"
)
st.image("file.png", width=250)

st.markdown(
    f"<h3 style='color:white'>Atualização: {datetime.now().strftime('%H:%M:%S')}</h3>",
    unsafe_allow_html=True
)
st.markdown("""
<style>
.stApp{
    background-color:black;
}

.card{
    border:1px solid white;
    padding:10px;
    height: 280px;
    margin:10px;
    background-color:black;
    color:white;
    text-align:center;
}

.valor{
    font-size:55px;
    font-weight:bold;
    color:white;
}

.verde{
    color:#00ff00;
    font-size:30px;
}

.vermelho{
    color:red;
    font-size:30px;
}

.amarelo{
    color:yellow;
    font-size:25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='color:white'>STELLANTIS - JABOATÃO</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='color:white'>REPORT PRODUÇÃO ANTERIORES</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    <h2>JEEP</h2>
    <div class='valor'>551</div>
    <div class='vermelho'delta = -9

cor = "red" if delta < 0 else "#00ff00"

st.markdown(
    f"<div style='font-size:40px;color:{cor};'>Δ {delta}</div>",
    unsafe_allow_html=True

with col2:
    st.markdown("""
    <div class='card'>
    <h2>JEEP</h2>
    <div class='valor'>226</div>
    <div class='vermelho'>Δ -26</div>
    <br>
    <div class='amarelo'>GIRO LF: 23</div>
    <div class='amarelo'>RETRABALHO: 7</div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class='card'>
    <h2>JEEP</h2>
    <div class='valor'>521</div>
    <div class='vermelho'>Δ -11</div>
    <br>
    <div class='amarelo'>GIRO LF: 10</div>
    <div class='amarelo'>RETRABALHO: 3</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
    <h2>FIAT</h2>
    <div class='valor'>363</div>
    <div class='vermelho'>Δ -10</div>
    <br>
    <div class='amarelo'>GIRO LF: 13</div>
    <div class='amarelo'>RETRABALHO: 5</div>
    </div>
    """, unsafe_allow_html=True)
