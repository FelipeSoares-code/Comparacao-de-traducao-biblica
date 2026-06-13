import processamento as pr
from pathlib import Path
import funcoesGraficos as fg
import streamlit as st
import funcoes as fn

def main(livroAbrev, traduc1, traduc2, biblia1, biblia2, St = False):
    sucesso = False

    print(f"-----------\nIniciando análise de: '{livroAbrev.capitalize()}'\n")
    
    if St:
        st.chat_message("assistant").write(f"Analisando '{livroAbrev.capitalize()}'")
        st.chat_message("assistant").write("Organizando livros...")
    try:
        livro1 = pr.organizarLivro(biblia1, livroAbrev, traduc1)
        livro2 = pr.organizarLivro(biblia2, livroAbrev, traduc2)
    except:
        print("Erro ao organizar livros")
        if St: st.chat_message("assistant").error("Erro ao organizar livros", icon="❌")
        return

    print("Analisando traduções...")
    if St: st.chat_message("assistant").write("Analisando traduções...")

    try:
        dadosAnalise = pr.analisarLivros(livro1, livro2, traduc1, traduc2, St= St)
    except:
        print("Erro ao analisar dados")
        if St: st.chat_message("assistant").error("Erro ao analisar dados", icon="❌")
        return

    print("Criando gráficos...")
    if St: st.chat_message("assistant").write("Criando gráficos...")

    pr.criarGraficos(
        dados=dadosAnalise,
        livro1=livro1,
        livro2=livro2,
        livroAbrev=livroAbrev,
        St=St
    ) 
    
    sucesso = True
    return sucesso 

if __name__ == "__main__":
    print("Início...")

    fg.saveFig = True

    # Lista de todos os livros do Novo Testamento (abreviações comuns em português)
    livros = ['mt','mc','lc','jo']

    PATH_TRADUCOES = Path("traducoes")
    traducoes = sorted(
        arquivo.stem
        for arquivo in PATH_TRADUCOES.glob("*.json")
    )

    print("Traduções disponíveis:", [t for t in traducoes])
    traduc1 = input("Digite a primeira tradução: ").upper()
    traduc2 = input("Digite a segunda tradução: ").upper()

    while traduc1 == traduc2:
        print("Você deve escolher duas traduções diferentes...")
        traduc1 = input("Digite a primeira tradução: ").upper()
        traduc2 = input("Digite a segunda tradução: ").upper()

    while traduc1 not in traducoes or traduc2 not in traducoes:
        print("Uma ou mais traduções digitadas não estão disponíveis...")
        traduc1 = input("Digite a primeira tradução: ").upper()
        traduc2 = input("Digite a segunda tradução: ").upper()

    sucessoJson = False
    try:
        print("Abrindo arquivos json...")
        biblia1 = pr.carregarJson(traduc1)
        biblia2 = pr.carregarJson(traduc2)
        sucessoJson = True
    except:
        print("Houve um erro ao abrir o arquivo Json...")

    if sucessoJson:
        for livro in livros:
            main(livro, traduc1, traduc2, biblia1, biblia2)
  






