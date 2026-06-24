import streamlit as st

st.set_page_config(
    page_title="Produção Anteriores",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: black;
}

div[data-testid="stMetric"] {
    background-color: black;
    border: 1px solid white;
    padding: 15px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

st.title("STELLANTIS - JABOATÃO")
st.subheader("REPORT PRODUÇÃO ANTERIORES")

def card(impostada, teorica, producao, parcial,
         delta, giro, retrabalho):

    st.write(f"**Impostada:** {impostada}")
    st.write(f"**Teórica:** {teorica}")

    st.metric(
        label="Produção Anteriores",
        value=producao,
        delta=delta
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Giro Linha Final",
            giro
        )

    with col2:
        st.metric(
            "Retrabalho",
            retrabalho
        )

    st.divider()

col1, col2 = st.columns(2)

with col1:
    card(120,120,551,-38,-38,0,0)

with col2:
    card(204,204,226,-64,-64,0,0)

col3, col4 = st.columns(2)

with col3:
    card(168,168,521,-42,-42,0,0)

with col4:
    card(260,260,363,-99,-99,0,0)
