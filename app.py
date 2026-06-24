st.markdown("""
<style>
.card{
    border:1px solid white;
    background:black;
    color:white;
    margin:10px;
}

.topo{
    display:grid;
    grid-template-columns:1fr 1fr 2fr 1fr 1fr;
    border-bottom:1px solid white;
}

.bloco{
    text-align:center;
    padding:5px;
    border-right:1px solid white;
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
    font-size:60px;
    font-weight:bold;
}

.titulo{
    color:#00ff00;
    font-size:28px;
    font-weight:bold;
}

.meio{
    display:grid;
    grid-template-columns:1fr 2fr 1fr;
    border-bottom:1px solid white;
}

.rodape{
    padding:10px;
    text-align:center;
    font-size:26px;
}

.data{
    font-size:18px;
    font-weight:bold;
}

.logo{
    text-align:center;
    padding-top:10px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">

        <div class="topo">

            <div class="bloco">
                Impostada
                <div class="valor-verde">120</div>
            </div>

            <div class="bloco">
                Teórica
                <div class="valor-verde">120</div>
            </div>

            <div class="bloco">
                <div class="producao">551</div>
                <div class="titulo">Produção Anteriores</div>
            </div>

            <div class="bloco">
                Parcial
                <div class="valor-verde">82</div>
            </div>

            <div class="bloco">
                Delta
                <div class="valor-vermelho">-38</div>
            </div>

        </div>

        <div class="meio">

            <div class="bloco">
                Giro linha Final
                <div class="valor-amarelo">0</div>
                <br>
                <div class="data">16:21:04</div>
            </div>

            <div class="logo">
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1d/Stellantis_logo.svg" width="220">
            </div>

            <div class="bloco">
                Giro Retrabalho
                <div class="valor-amarelo">0</div>
                <br>
                <div class="data">24/06/2026</div>
            </div>

        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL
            <span style="color:red;font-weight:bold;"> -38</span>
        </div>

        <div class="rodape">
            CONTABILIZANDO GIRO LINHA FINAL E RETRABALHO
            <span style="color:red;font-weight:bold;"> -38</span>
        </div>

    </div>
    """, unsafe_allow_html=True)
