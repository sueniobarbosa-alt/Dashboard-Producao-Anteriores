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
    margin-bottom:20px;
}

.linha{
    display:flex;
    border-bottom:1px solid white;
}

.bloco{
    flex:1;
    text-align:center;
    padding:8px;
    border-right:1px solid white;
}

.bloco:last-child{
    border-right:none;
}

.verde{
    color:#00ff00;
    font-size:24px;
    font-weight:bold;
}

.amarelo{
    color:yellow;
    font-size:24px;
    font-weight:bold;
}

.vermelho{
    color:red;
    font-size:24px;
    font-weight:bold;
}

.producao{
    font-size:55px;
    font-weight:bold;
    color:white;
}

.titulo{
    color:#00ff00;
    font-size:22px;
    font-weight:bold;
}

.hora{
    font-size:20px;
    font-weight:bold;
}

.rodape{
    text-align:center;
    padding:10px;
    font-size:22px;
    border-bottom:1px solid white;
}

.delta{
    color:red;
    font-size:26px;
    font-weight:bold;
}

.logo{
    text-align:center;
    padding-top:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

        <div class="linha">

            <div class="bloco">
                Impostada<br>
                <div class="verde">120</div>
            </div>

            <div class="bloco">
                Teórica<br>
                <div class="verde">120</div>
            </div>

            <div class="bloco">
                <div class="producao">551</div>
                <div class="titulo">
                Produção Anteriores
                </div>
            </div>

            <div class="bloco">
                Parcial<br>
                <div class="verde">82</div>
            </div>

            <div class="bloco">
                Delta<br>
                <div class="vermelho">-38</div>
            </div>

        </div>

        <div class="linha">

            <div class="bloco">
                Giro linha Final
                <div class="amarelo">0</div>
            </div>

            <div class="bloco logo">
                STELLANTIS
            </div>

            <div class="bloco">
                Giro Retrabalho
                <div class="amarelo">0</div>
            </div>

        </div>

        <div class="linha">

            <div class="bloco">
                <div class="hora">
                16:21:04
                </div>
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

    st.markdown("""
    <div class="card">

        <div class="linha">

            <div class="bloco">
                Impostada<br>
                <div class="verde">204</div>
            </div>

            <div class="bloco">
                Teórica<br>
                <div class="verde">204</div>
            </div>

            <div class="bloco">
                <div class="producao">226</div>
                <div class="titulo">
                Produção Anteriores
                </div>
            </div>

            <div class="bloco">
                Parcial<br>
                <div class="verde">140</div>
            </div>

            <div class="bloco">
                Delta<br>
                <div class="vermelho">-64</div>
            </div>

        </div>

        <div class="linha">

            <div class="bloco">
                Giro linha Final
                <div class="amarelo">0</div>
            </div>

            <div class="bloco logo">
                STELLANTIS
            </div>

            <div class="bloco">
                Giro Retrabalho
                <div class="amarelo">0</div>
            </div>

        </div>

        <div class="linha">

            <div class="bloco">
                <div class="hora">
                16:21:04
                </div>
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
