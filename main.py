import json
import funcoes as fn
import funcoesGraficos as fg

print("inicio")

#%%----------------------------------
# Abertura do texto original em json
print("Abrindo arquivos json...")
with open('traducoes/ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)

with open('traducoes/NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaNvt = json.load(arquivo)


def main(livroAbrev):
#%%-----------------------------------
    # escolha dos livros
    livroArc = fn.buscarJsonBiblia(
        biblia=bibliaArc,
        abrev=livroAbrev
    )

    livroNvt = fn.buscarJsonBiblia(
        biblia=bibliaNvt,
        abrev=livroAbrev
    )

    #%%-----------------------------------
    # Limpeza das palavras e organização dos objetos
    print("Organizando livro...")
    livroArc = fn.organizarLivro(livroArc, "Arc")
    livroNvt = fn.organizarLivro(livroNvt, "Nvt")

    #%%-----------------------------------
    #tokenização
    print("Separando palavras...")
    fn.addTokens(livroArc)
    fn.addTokens(livroNvt)
    tokensTotal = []
    for v in livroArc:
        tokensTotal.append(v["tokens"])
    for v in livroNvt:
        tokensTotal.append(v["tokens"])

    fn.addQuantPalavr(livroArc)
    fn.addQuantPalavr(livroNvt)

    #%%----------------------------------
    #contagem de palavras
    print("Contando palavras...")
    contPalvrArc = fn.contPalavras(livroArc)
    contPalavrNvt = fn.contPalavras(livroNvt)

    #%%-----------------------------------
    #detectar novas palavras
    palavrExclArc = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalvrArc) - set(contPalavrNvt)),
        livro=livroArc,
        quantPalavras=10
    )

    palavrExclNvt = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalavrNvt) - set(contPalvrArc)),
        livro=livroNvt,
        quantPalavras=10
    )
    
    #%%-------------------------------------
    #buscar nível de semelhança entre versiculos
    semelhanVers = fn.semelhanTraduc(livroArc, livroNvt)

    #%%------------------------------------
    #buscar semelhanças semânticas entre palavras
    # palavrSemelhante = fn.palavrSemelhantes(tokensTotal)

    #%%-------------------------------------
    #Criar graficos
    fg.grafPlavrExcl(palavrExclArc, "ARC", #mostra as n palavras exclusivas que mais aparecem
                     nomeLivro=livroArc[0]["livro"],
                     abrevLivro=livroAbrev
    ) 
    fg.grafPlavrExcl(palavrExclNvt, "NVT", 
                     nomeLivro=livroArc[0]["livro"],
                     abrevLivro=livroAbrev
    )

    fg.histograma( #distribuição do nível de semelhança entre os versiculos
        semelhanVers,
        traducNome1=livroArc[0]["traducao"],
        traducNome2=livroNvt[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livroArc[0]["livro"]
    )

    fg.heatmap( #mapa geral dos versiculos mais semelhantes
        lista=semelhanVers,
        traducNome1=livroArc[0]["traducao"],
        traducNome2=livroNvt[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livroArc[0]["livro"]
    )

    fg.grafTopSemelhanca( #mostra os top n versiculos mais semelhantes de cada capitulo do livro
        fn.topSemelhanPorCap(semelhanVers, 3),
        traducNome1=livroArc[0]["traducao"],
        traducNome2=livroNvt[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livroArc[0]["livro"]
    )

    fg.grafLinhas(livroArc, livroNvt)



# for l in ['mt','mc', 'lc', 'jo']:
#     main(l)
  
main('mc')





