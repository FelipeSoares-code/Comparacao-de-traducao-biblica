import streamlit as st
from pathlib import Path

PATH_TRADUCOES = Path("traducoes")

traducoes = sorted(
    arquivo.stem
    for arquivo in PATH_TRADUCOES.glob("*.json")
)

st.title("Análise Comparativa de Traduções Bíblicas")

traduc1 = st.selectbox(
    "Escolha a primeira tradução",
    traducoes
)

traduc2 = st.selectbox(
    "Escolha a segunda tradução",
    traducoes
)
