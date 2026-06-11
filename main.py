import processamento as pr
from pathlib import Path
import funcoesGraficos as fg
import streamlit as st

def main(livroAbrev, traduc1, traduc2, biblia1, biblia2, St = False):
    sucesso = False
    
    if St: st.chat_message(f"Analisando '{livroAbrev}'")

    if St: st.chat_message("Organizando livros...")
    livro1 = pr.organizarLivro(biblia1, livroAbrev, traduc1)
    livro2 = pr.organizarLivro(biblia2, livroAbrev, traduc2)

    if St: st.chat_message("Analisando livros...")
    dadosAnalise = pr.analisarLivros(livro1, livro2)

    if St: st.chat_message("Criando gráficos...")
    pr.criarGraficos(
        dados=dadosAnalise,
        livro1=livro1,
        livro2=livro2,
        livroAbrev=livroAbrev,
        traduc1=traduc1,
        traduc2=traduc2,
        St=St
    )   
    
    sucesso = True
    return sucesso 

if __name__ == "__main__":
    print("Início...")

    fg.saveFig = True

    livros = ['mt', 'mc', 'lc', 'jo']

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
  






