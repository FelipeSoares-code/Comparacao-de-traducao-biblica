import processamento as pr

livros = ['mt','mc', 'lc', 'jo']

def main(livroAbrev, traduc1, traduc2, biblia1, biblia2):
    livro1 = pr.organizarLivro(biblia1, livroAbrev, traduc1)
    livro2 = pr.organizarLivro(biblia2, livroAbrev, traduc2)

    dadosAnalise = pr.analisarLivros(livro1, livro2)

    pr.criarGraficos(
        dados=dadosAnalise,
        livro1=livro1,
        livro2=livro2,
        livroAbrev=livroAbrev,
        traduc1=traduc1,
        traduc2=traduc2
    )    

if __name__ == "__main__":
    print("Início...")
    #%%----------------------------------
    # Abertura do texto original em json
    traduc1 = input("Digite a primeira tradução: ").upper()
    traduc2 = input("Digite a segunda tradução: ").upper()

    print("Abrindo arquivos json...")
    biblia1 = pr.carregarJson(traduc1)
    biblia2 = pr.carregarJson(traduc2)
    for livro in livros:
        main(livro, traduc1, traduc2, biblia1, biblia2)
  






