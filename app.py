import streamlit as st

st.set_page_config(
    page_title="Produção Anteriores",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background-color:black;
    color:white;
}

table{
    width:100%;
    border-collapse:collapse;
    text-align:center;
    background:black;
    color:white;
}

td{
    border:1px solid white;
    padding:8px;
}

.valor-verde{
    color:#00ff00;
    font-size:40px;
    font-weight:bold;
}

.valor-vermelho{
    color:red;
    font-size:40px;
    font-weight:bold;
}

.producao{
    font-size:70px;
    font-weight:bold;
}

.titulo{
    color:#00ff00;
    font-size:28px;
    font-weight:bold;
}

.amarelo{
    color:yellow;
    font-size:35px;
    font-weight:bold;
}

.hora{
    font-size:30px;
    font-weight:bold;
}

.data{
    font-size:24px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <table>
        <tr>
            <td>
                Impostada<br>
                <div class="valor-verde">120</div>
            </td>

            <td>
                Teórica<br>
                <div class="valor-verde">120</div>
            </td>

            <td>
                <div class="producao">551</div>
                <div class="titulo">Produção Anteriores</div>
            </td>

            <td>
                Parcial<br>
                <div class="valor-verde">82</div>
            </td>

            <td>
                Delta<br>
                <div class="valor-vermelho">-38</div>
            </td>
        </tr>

        <tr>
            <td colspan="2">
                Giro linha Final<br>
                <div class="amarelo">0</div>
            </td>

            <td>
                STELLANTIS
            </td>

            <td colspan="2">
                Giro Retrabalho<br>
                <div class="amarelo">0</div>
            </td>
        </tr>

        <tr>
            <td colspan="2">
                <div class="hora">16:21:04</div>
            </td>

            <td>
                STELLANTIS
            </td>

            <td colspan="2">
                <div class="data">24/06/2026</div>
            </td>
        </tr>

        <tr>
            <td colspan="5">
                CONTABILIZANDO GIRO LINHA FINAL
                <span class="valor-vermelho">-38</span>
            </td>
        </tr>

        <tr>
            <td colspan="5">
                CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
                <span class="valor-vermelho">-38</span>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <table>
        <tr>
            <td>
                Impostada<br>
                <div class="valor-verde">204</div>
            </td>

            <td>
                Teórica<br>
                <div class="valor-verde">204</div>
            </td>

            <td>
                <div class="producao">226</div>
                <div class="titulo">Produção Anteriores</div>
            </td>

            <td>
                Parcial<br>
                <div class="valor-verde">140</div>
            </td>

            <td>
                Delta<br>
                <div class="valor-vermelho">-64</div>
            </td>
        </tr>

        <tr>
            <td colspan="2">
                Giro linha Final<br>
                <div class="amarelo">0</div>
            </td>

            <td>
                STELLANTIS
            </td>

            <td colspan="2">
                Giro Retrabalho<br>
                <div class="amarelo">0</div>
            </td>
        </tr>

        <tr>
            <td colspan="2">
                <div class="hora">16:21:04</div>
            </td>

            <td>
                STELLANTIS
            </td>

            <td colspan="2">
                <div class="data">24/06/2026</div>
            </td>
        </tr>

        <tr>
            <td colspan="5">
                CONTABILIZANDO GIRO LINHA FINAL
                <span class="valor-vermelho">-64</span>
            </td>
        </tr>

        <tr>
            <td colspan="5">
                CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
                <span class="valor-vermelho">-64</span>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
