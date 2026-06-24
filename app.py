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

