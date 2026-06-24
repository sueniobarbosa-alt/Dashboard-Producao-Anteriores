import streamlit as st

st.set_page_config(
    page_title="Produção Anteriores",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#000000;
    color:white;
}

.card{
    border:1px solid white;
    background:black;
    padding:0;
    margin-bottom:20px;
}

.linha{
    display:flex;
}

.bloco{
    flex:1;
    text-align:center;
    border-right:1px solid white;
    padding:5px;
}

.bloco:last-child{
    border-right:none;
}

.valor-verde{
    color:#00ff00;
    font-size:28px;
    font-weight:bold;
}

.valor-amarelo{
    color:yellow;
    font-size:28px;
    font-weight:bold;
}

.valor-vermelho{
    color:red;
    font-size:28px;
    font-weight:bold;
}

.producao{
    font-size:55px;
    font-weight:bold;
    color:white;
}

.titulo{
    color:#00ff00;
    font-size:28px;
    font-weight:bold;
}

.hora{
    font-size:24px;
    font-weight:bold;
}

.rodape{
    text-align:center;
    font-size:18px;
    padding:8px;
}

.delta{
    color:red;
    font-size:24px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

col1, col2 = st.columns(2)

with col1:

    st.markdown(f"""
    <div class="card">

        <div class="linha">
            <div class="bloco">
                Impostada<br>
                <div class="valor-verde">120</div>
            </div>

            <div class="bloco">
                Teórica<br>
                <div class="valor-verde">120</div>
            </div>

            <div class="bloco">
                <div class="producao">551</div>
                <div class="titulo">Produção Anteriores</div>
            </div>

            <div class="bloco">
                Parcial<br>
                <div class="valor-verde">82</div>
            </div>

            <div class="bloco">
                Delta<br>
                <div class="valor-vermelho">-38</div>
            </div>
        </div>

        <div class="linha">
            <div class="bloco">
                Giro Linha Final<br>
                <div class="valor-amarelo">0</div>
            </div>

            <div class="bloco">
                <br>
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Stellantis.svg/512px-Stellantis.svg.png" width="220">
            </div>

            <div class="bloco">
                Giro Retrabalho<br>
                <div class="valor-amarelo">0</div>
            </div>
        </div>

        <div class="linha">
            <div class="bloco">
                <div class="hora">16:21:04</div>
            </div>

            <div class="bloco">
            </div>

            <div class="bloco">
                <div class="hora">
                24/06/2026<br>
                Wednesday
                </div>
            </div>
        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL
            <span class="delta"> -38</span>
        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
            <span class="delta"> -38</span>
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="card">

        <div class="linha">
            <div class="bloco">
                Impostada<br>
                <div class="valor-verde">204</div>
            </div>

            <div class="bloco">
                Teórica<br>
                <div class="valor-verde">204</div>
            </div>

            <div class="bloco">
                <div class="producao">226</div>
                <div class="titulo">Produção Anteriores</div>
            </div>

            <div class="bloco">
                Parcial<br>
                <div class="valor-verde">140</div>
            </div>

            <div class="bloco">
                Delta<br>
                <div class="valor-vermelho">-64</div>
            </div>
        </div>

        <div class="linha">
            <div class="bloco">
                Giro Linha Final<br>
                <div class="valor-amarelo">0</div>
            </div>

            <div class="bloco">
                <br>
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Stellantis.svg/512px-Stellantis.svg.png" width="220">
            </div>

            <div class="bloco">
                Giro Retrabalho<br>
                <div class="valor-amarelo">0</div>
            </div>
        </div>

        <div class="linha">
            <div class="bloco">
                <div class="hora">16:21:04</div>
            </div>

            <div class="bloco">
            </div>

            <div class="bloco">
                <div class="hora">
                24/06/2026<br>
                Wednesday
                </div>
            </div>
        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL
            <span class="delta"> -64</span>
        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
            <span class="delta"> -64</span>
        </div>

    </div>
    """, unsafe_allow_html=True)
