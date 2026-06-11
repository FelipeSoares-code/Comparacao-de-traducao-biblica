import streamlit as st
from pathlib import Path
import processamento as pr
from main import main

PATH_TRADUCOES = Path("traducoes")

livros = ['mt']

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

if st.button("Iniciar Análise"):
    with st.spinner("Calculando similaridades..."):
        biblia1 = pr.carregarJson(traduc1)
        biblia2 = pr.carregarJson(traduc2)

        for livro in livros:
            main(livro, traduc1, traduc2, biblia1, biblia2, St=True)

    st.success