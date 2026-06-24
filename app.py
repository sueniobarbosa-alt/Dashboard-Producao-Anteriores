import streamlit as st

st.set_page_config(
    page_title="Produção Anteriores",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}

.card {
    border: 1px solid white;
    padding: 20px;
    text-align: center;
    background: black;
}

.verde {
    color: #00ff00;
    font-size: 30px;
    font-weight: bold;
}

.amarelo {
    color: yellow;
    font-size: 28px;
    font-weight: bold;
}

.vermelho {
    color: red;
    font-size: 28px;
    font-weight: bold;
}

.producao {
    font-size: 70px;
    font-weight: bold;
}

.titulo {
    color: #00ff00;
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="verde">IMPOSTADA 120</div>
        <br>
        <div class="producao">551</div>
        <br>
        <div class="vermelho">DELTA -38</div>
        <br>
        <div class="amarelo">GIRO LF: 0</div>
        <div class="amarelo">RETRABALHO: 0</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="verde">IMPOSTADA 204</div>
        <br>
        <div class="producao">226</div>
        <br>
        <div class="vermelho">DELTA -64</div>
        <br>
        <div class="amarelo">GIRO LF: 0</div>
        <div class="amarelo">RETRABALHO: 0</div>
    </div>
    """, unsafe_allow_html=True)
