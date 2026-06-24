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
    <div style="border:1px solid white; background:black; color:white;">

        <table style="width:100%; border-collapse:collapse; text-align:center;">
            <tr>
                <td style="border:1px solid white;">
                    Impostada<br>
                    <span style="color:#00ff00;font-size:40px;"><b>120</b></span>
                </td>

                <td style="border:1px solid white;">
                    Teórica<br>
                    <span style="color:#00ff00;font-size:40px;"><b>120</b></span>
                </td>

                <td style="border:1px solid white;">
                    <span style="font-size:70px;"><b>551</b></span><br>
                    <span style="color:#00ff00;font-size:30px;">
                    Produção Anteriores
                    </span>
                </td>

                <td style="border:1px solid white;">
                    Parcial<br>
                    <span style="color:#00ff00;font-size:40px;"><b>82</b></span>
                </td>

                <td style="border:1px solid white;">
                    Delta<br>
                    <span style="color:red;font-size:40px;"><b>-38</b></span>
                </td>
            </tr>

            <tr>
                <td colspan="2" style="border:1px solid white;">
                    Giro Linha Final<br>
                    <span style="color:yellow;font-size:35px;">0</span>
                </td>

                <td style="border:1px solid white;">
                    STELLANTIS
                </td>

                <td colspan="2" style="border:1px solid white;">
                    Giro Retrabalho<br>
                    <span style="color:yellow;font-size:35px;">0</span>
                </td>
            </tr>

            <tr>
                <td colspan="5" style="padding:20px;">
                    CONTABILIZANDO GIRO LINHA FINAL
                    <span style="color:red;font-size:35px;"><b>-38</b></span>
                </td>
            </tr>

            <tr>
                <td colspan="5" style="padding:20px;">
                    CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
                    <span style="color:red;font-size:35px;"><b>-38</b></span>
                </td>
            </tr>

        </table>

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
