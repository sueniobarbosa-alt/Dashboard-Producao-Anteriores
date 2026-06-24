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

h1, h2 {
    color: white;
}

.card {
    border: 1px solid white;
    margin-bottom: 20px;
    background-color: black;
}

table {
    width: 100%;
    border-collapse: collapse;
    color: white;
    text-align: center;
}

td {
    border: 1px solid white;
    padding: 8px;
}

.verde {
    color: #00ff00;
    font-size: 22px;
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

.producao {
    font-size: 55px;
    font-weight: bold;
}

.titulo {
    color: #00ff00;
    font-size: 22px;
    font-weight: bold;
}

.rodape {
    font-size: 18px;
    padding: 10px;
}

.data {
    font-size: 18px;
    font-weight: bold;
}

.logo {
    font-size: 24px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")


def card(impostada, teorica, producao, parcial,
         delta, girolf, retrabalho):

    return f"""
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
            <div class="producao">{producao}</div>
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
            Giro linha Final<br>
            <div class="amarelo">{girolf}</div>
        </td>

        <td>
            <div class="logo">
            STELLANTIS
            </div>
        </td>

        <td colspan="2">
            Giro Retrabalho<br>
            <div class="amarelo">{retrabalho}</div>
        </td>

    </tr>

    <tr>

        <td colspan="2">
            <div class="data">
            16:21:04
            </div>
        </td>

        <td>
            STELLANTIS
        </td>

        <td colspan="2">
            <div class="data">
            24/06/2026
            </div>
        </td>

    </tr>

    <tr>
        <td colspan="5" class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL
            <span class="vermelho">
            {delta}
            </span>
        </td>
    </tr>

    <tr>
        <td colspan="5" class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
            <span class="vermelho">
            {delta}
            </span>
        </td>
    </tr>

    </table>

    </div>
    """


col1, col2 = st.columns(2)

with col1:
    st.markdown(
        card(120,120,551,82,-38,0,0),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        card(204,204,226,140,-64,0,0),
        unsafe_allow_html=True
    )

col3, col4 = st.columns(2)

with col3:
    st.markdown(
        card(168,168,521,126,-42,0,0),
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        card(260,260,"363 / 376",161,-99,0,0),
        unsafe_allow_html=True
    )
