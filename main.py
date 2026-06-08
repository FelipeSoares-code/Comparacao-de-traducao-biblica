import json
import funcoes as fn
import funcoesGraficos as fg

print("inicio")

#%%----------------------------------
# Abertura do texto original em json
traduc1 = input("Digite a tradução 1: ")
traduc2 = input("Digite a tradução 2: ")

print("Abrindo arquivos json...")
with open(f'traducoes/{traduc1.upper()}.json', 'r', encoding='utf-8') as arquivo:
    biblia1 = json.load(arquivo)

with open(f'traducoes/{traduc2.upper()}.json', 'r', encoding='utf-8') as arquivo:
    biblia2 = json.load(arquivo)

def main(livroAbrev):
#%%-----------------------------------
    # escolha dos livros
    livro1 = fn.buscarJsonBiblia(
        biblia=biblia1,
        abrev=livroAbrev
    )

    livro2 = fn.buscarJsonBiblia(
        biblia=biblia2,
        abrev=livroAbrev
    )

    print(f"----------\nAnalisando o livro: {livro1['name']}...\n")

    #%%-----------------------------------
    # Limpeza das palavras e organização dos objetos
    print("Organizando livro...")
    livro1 = fn.organizarLivro(livro1, traduc1)
    livro2 = fn.organizarLivro(livro2, traduc2)

    #%%-----------------------------------
    #tokenização
    print("Separando palavras...")
    fn.addTokens(livro1)
    fn.addTokens(livro2)

    fn.addQuantPalavr(livro1)
    fn.addQuantPalavr(livro2)

    #%%----------------------------------
    #contagem de palavras
    print("Contando palavras...")
    contPalvr1 = fn.contPalavras(livro1)
    contPalavr2 = fn.contPalavras(livro2)

    #%%-----------------------------------
    #detectar novas palavras
    print("Buscando palavras exclusivas...")
    palavrExcl_1 = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalvr1) - set(contPalavr2)),
        livro=livro1,
        quantPalavras=10
    )

    palavrExcl_2 = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalavr2) - set(contPalvr1)),
        livro=livro2,
        quantPalavras=10
    )
    
    #%%-------------------------------------
    #buscar nível de semelhança entre versiculos
    print("Analisando nível de semelhança entre os versículos...")
    semelhanVers = fn.semelhanTraduc(livro1, livro2)

    #%%-------------------------------------
    #Criar graficos
    print("Criando gráficos...")
    fg.grafPlavrExcl( #mostra as n palavras exclusivas que mais aparecem
        palavrExcl_1, traduc1.upper(), 
        nomeLivro=livro1[0]["livro"],
        abrevLivro=livroAbrev
    ) 
    fg.grafPlavrExcl(
        palavrExcl_2, traduc2.upper(), 
        nomeLivro=livro1[0]["livro"],
        abrevLivro=livroAbrev
    )

    fg.histograma( #distribuição do nível de semelhança entre os versiculos
        semelhanVers,
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    fg.heatmap( #mapa geral dos versiculos mais semelhantes
        lista=semelhanVers,
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    fg.grafTopSemelhanca( #mostra os top n versiculos mais semelhantes de cada capitulo do livro
        fn.topSemelhanPorCap(semelhanVers, 3),
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    fg.grafLinhas(livro1, livro2)


if __name__ == "__main__":
    for l in ['mt','mc', 'lc', 'jo']:
        main(l)
  






