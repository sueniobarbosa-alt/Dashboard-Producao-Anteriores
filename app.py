from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=60000, key="refresh")

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime


import pandas as pd
df = pd.read_csv(
    "Dados.csv",
    sep=";",
    encoding="latin1"
)
st.set_page_config(
    page_title="Produção Anteriores",
    layout="wide"
)

hora = datetime.now().strftime("%H:%M:%S")
data = datetime.now().strftime("%d/%m/%Y")


def card(impostada, teorica, linha,
         parcial, delta,
         giro_lf, giro_rt):

    return f"""
    <div class="card">

        <table>

            <tr>
                <td>
                    Impostada<br>
                    <span class="verde">{impostada}</span>
                </td>

                <td>
                    Teórica<br>
                    <span class="verde">{teorica}</span>
                </td>

                <td class="centro">
                    <div class="linha">{linha}</div>
                    <div class="titulo">
                        Produção Anteriores
                    </div>
                </td>

                <td>
                    Parcial<br>
                    <span class="verde">{parcial}</span>
                </td>

                <td>
                    Delta<br>
                    <span class="vermelho">{delta}</span>
                </td>
            </tr>

            <tr>

                <td colspan="2">
                    Giro Linha Final<br>
                    <span class="amarelo">
                        {giro_lf}
                    </span>
                </td>

                <td>
                    STELLANTIS
                </td>

                <td colspan="2">
                    Giro Retrabalho<br>
                    <span class="amarelo">
                        {giro_rt}
                    </span>
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
    """


html = f"""
<html>

<head>

<style>

body {{
    background-color: black;
    color: white;
    font-family: Arial;
}}

h1 {{
    margin-bottom: 5px;
}}

h2 {{
    margin-top: 0;
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}}

.card {{
    border: 1px solid white;
    background: black;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    text-align: center;
}}

td {{
    border: 1px solid white;
    padding: 8px;
}}

.verde {{
    color: #00ff00;
    font-size: 40px;
    font-weight: bold;
}}

.vermelho {{
    color: red;
    font-size: 40px;
    font-weight: bold;
}}

.amarelo {{
    color: yellow;
    font-size: 35px;
    font-weight: bold;
}}

.linha {{
    font-size: 65px;
    font-weight: bold;
}}

.titulo {{
    color: #00ff00;
    font-size: 28px;
    font-weight: bold;
}}

.hora {{
    font-size: 30px;
    font-weight: bold;
}}

.data {{
    font-size: 26px;
    font-weight: bold;
}}

.centro {{
    width: 300px;
}}

</style>

</head>

<body>

<h1>STELLANTIS - JABOATÃO</h1>
<h2>REPORT PRODUÇÃO ANTERIORES</h2>

<div class="grid">

    {card(120,120,"551",82,-38,0,0)}

    {card(204,204,"226",140,-64,0,0)}

    {card(168,168,"521",126,-42,0,0)}

    {card(260,260,"363 / 376",161,-99,0,0)}

</div>

</body>

</html>
"""

components.html(
    html,
    height=950,
    scrolling=True
)
