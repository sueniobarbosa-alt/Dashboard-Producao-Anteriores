import streamlit as st
from datetime import datetime

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
    background-color: black;
    padding: 0px;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    text-align: center;
    color: white;
}

td {
    border: 1px solid white;
    padding: 6px;
}

.verde {
    color: #00ff00;
    font-size: 26px;
    font-weight: bold;
}

.amarelo {
    color: yellow;
    font-size: 22px;
    font-weight: bold;
}

.vermelho {
    color: red;
    font-size: 22px;
    font-weight: bold;
}

.linha {
    font-size: 55px;
    font-weight: bold;
}

.titulo {
    color: #00ff00;
    font-size: 20px;
    font-weight: bold;
}

.hora {
    font-size: 24px;
    font-weight: bold;
}

.data {
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

hora = datetime.now().strftime("%H:%M:%S")
data = datetime.now().strftime("%d/%m/%Y")


def card(impostada, teorica, linha,
         parcial, delta,
         giro_lf, giro_rt):

    st.markdown(f"""
    <div class="card">

    <table>

    <tr>

        <td>
            Impostada<br>
            <div class="verde">{impostada}</div>
        </td>

        <td>
            Teórica<br>
            <div class="verde">{teorica}</div>
        </td>

        <td>
            <div class="linha">{linha}</div>
            <div class="titulo">
                Produção Anteriores
            </div>
        </td>

        <td>
            Parcial<br>
            <div class="verde">{parcial}</div>
        </td>

        <td>
            Delta<br>
            <div class="vermelho">{delta}</div>
        </td>

    </tr>

    <tr>

        <td colspan="2">
            Giro Linha Final<br>
            <div class="amarelo">
                {giro_lf}
            </div>
        </td>

        <td>
            STELLANTIS
        </td>

        <td colspan="2">
            Giro Retrabalho<br>
            <div class="amarelo">
                {giro_rt}
            </div>
        </td>

    </tr>

    <tr>

        <td colspan="2">
            <div class="hora">
                {hora}
            </div>
        </td>

        <td>
            STELLANTIS
        </td>

        <td colspan="2">
            <div class="data">
                {data}
            </div>
        </td>

    </tr>

    <tr>
        <td colspan="5">
            CONTABILIZANDO GIRO LINHA FINAL
            <span class="vermelho">
                {delta}
            </span>
        </td>
    </tr>

    <tr>
        <td colspan="5">
            CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
            <span class="vermelho">
                {delta}
            </span>
        </td>
    </tr>

    </table>

    </div>
    """, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    card(120, 120, "551", 82, -38, 0, 0)

with col2:
    card(204, 204, "226", 140, -64, 0, 0)

col3, col4 = st.columns(2)

with col3:
    card(168, 168, "521", 126, -42, 0, 0)

with col4:
    card(260, 260, "363 / 376", 161, -99, 0, 0)
