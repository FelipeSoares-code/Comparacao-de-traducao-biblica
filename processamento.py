import funcoes as fn
import funcoesGraficos as fg
import json
import matplotlib.pyplot as plt
import streamlit as st

def carregarJson(traduc):
    with open(f'traducoes/{traduc.upper()}.json', 'r', encoding='utf-8') as arquivo:
        biblia = json.load(arquivo)

    return biblia

def organizarLivro(biblia, livroAbrev, traduc):
    livro = fn.buscarJsonBiblia(
        biblia=biblia,
        abrev=livroAbrev
    )

    print(f"----------\nAnalisando o livro: {livro['name']}...\n")

    #%%-----------------------------------
    # Limpeza das palavras e organização dos objetos
    print("Organizando livro...")
    livro = fn.organizarLivro(livro, traduc)

    #%%-----------------------------------
    #tokenização
    print("Separando palavras...")
    fn.addTokens(livro)

    fn.addQuantPalavr(livro)

    return livro

def analisarLivros(livro1, livro2):
    #%%----------------------------------
    #contagem de palavras
    print("Contando palavras...")
    contPalavr1 = fn.contPalavras(livro1)
    contPalavr2 = fn.contPalavras(livro2)

    #%%-----------------------------------
    #detectar novas palavras
    print("Buscando palavras exclusivas...")
    palavrExcl_1 = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalavr1) - set(contPalavr2)),
        livro=livro1,
        quantPalavras=10
    )

    palavrExcl_2 = fn.topPalavrExcl(
        listPalvrExcl=(set(contPalavr2) - set(contPalavr1)),
        livro=livro2,
        quantPalavras=10
    )
    
    #%%-------------------------------------
    #buscar nível de semelhança entre versiculos
    print("Analisando nível de semelhança entre os versículos...")
    semelhanVers = fn.semelhanTraduc(livro1, livro2)

    analise = {
        "cont_palavr_1": contPalavr1,
        "cont_palavr_2": contPalavr2,
        "palavr_excl_1": palavrExcl_1,
        "palavr_excl_2": palavrExcl_2,
        "semelhanca_vers": semelhanVers
    }

    return analise


def criarGraficos(dados, livro1, livro2, traduc1, traduc2, livroAbrev, St = False):
    palavrExcl_1 = dados["palavr_excl_1"]
    palavrExcl_2 = dados["palavr_excl_2"]

    semelhanVers = dados["semelhanca_vers"]
    #%%-------------------------------------
    #Criar graficos
    print("Criando gráficos...")
    fig = fg.grafPlavrExcl( #mostra as n palavras exclusivas que mais aparecem
        lista=palavrExcl_1, 
        traducNome=traduc1.upper(), 
        nomeLivro=livro1[0]["livro"],
        abrevLivro=livroAbrev
    )

    if St: st.pyplot(fig)

    plt.close()
    
    fig = fg.grafPlavrExcl(
        lista=palavrExcl_2, 
        traducNome=traduc2.upper(), 
        nomeLivro=livro1[0]["livro"],
        abrevLivro=livroAbrev
    )

    if St: st.pyplot(fig);

    plt.close()

    fig = fg.histograma( #distribuição do nível de semelhança entre os versiculos
        lista=semelhanVers,
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    if St: st.pyplot(fig)

    plt.close()

    fig = fg.heatmap( #mapa geral dos versiculos mais semelhantes
        lista=semelhanVers,
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    if St: st.pyplot(fig)

    plt.close()

    fig = fg.grafTopSemelhanca( #mostra os top n versiculos mais semelhantes de cada capitulo do livro
        fn.topSemelhanPorCap(semelhanVers, 3),
        traducNome1=livro1[0]["traducao"],
        traducNome2=livro2[0]["traducao"],
        abrevLivro=livroAbrev,
        nomeLivro=livro1[0]["livro"]
    )

    if St: st.pyplot(fig)

    plt.close()

    fig = fg.grafLinhas(livro1, livro2)

    if St: st.pyplot(fig)

    plt.close()