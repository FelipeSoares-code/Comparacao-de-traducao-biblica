import streamlit as st
from pathlib import Path
import processamento as pr
from main import main

PATH_TRADUCOES = Path("traducoes")

livros_nt = {
    "Mateus": "mt",
    "Marcos": "mc",
    "Lucas": "lc",
    "João": "jo",
    "Atos": "at",
    "Romanos": "rm",
    "1 Coríntios": "1co",
    "2 Coríntios": "2co",
    "Gálatas": "gl",
    "Efésios": "ef",
    "Filipenses": "fp",
    "Colossenses": "cl",
    "1 Tessalonicenses": "1ts",
    "2 Tessalonicenses": "2ts",
    "1 Timóteo": "1tm",
    "2 Timóteo": "2tm",
    "Tito": "tt",
    "Filemom": "fm",
    "Hebreus": "hb",
    "Tiago": "tg",
    "1 Pedro": "1pe",
    "2 Pedro": "2pe",
    "1 João": "1jo",
    "2 João": "2jo",
    "3 João": "3jo",
    "Judas": "jd",
    "Apocalipse": "ap"
}

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

livros_escolhidos = st.multiselect(
    "Selecione os livros para analisar:",
    list(livros_nt.keys())
)

if len(livros_escolhidos) > 4:
    st.warning("Escolher muitos livros pode fazer a análise demorar muito", icon="⚠️")

if st.button("Iniciar Análise"):
    sucesso = False
    if traduc1 == traduc2:
        st.error("Você deve escolher duas traduções diferentes", icon="❌")
    elif len(livros_escolhidos) == 0:
        st.error("Escolha pelo menos 1 livro", icon="❌")
    else:
        with st.spinner("Realizando análise..."):
            sucessoJson = False
            try:
                biblia1 = pr.carregarJson(traduc1)
                biblia2 = pr.carregarJson(traduc2)
                sucessoJson = True
            except:
                st.error("Houve um erro ao carregar os arquivos Json", icon="❌")

            if sucessoJson:
                for livro in livros_escolhidos:
                    abrev = livros_nt[livro]
                    sucesso = main(abrev, traduc1, traduc2, biblia1, biblia2, St=True)

    if sucesso: 
        st.success("Análise concluída")