import funcoes as fn
import funcoesGraficos as fg
import json
import matplotlib.pyplot as plt
import streamlit as st
import time

def carregarJson(traduc):
    with open(f'traducoes/{traduc.upper()}.json', 'r', encoding='utf-8') as arquivo:
        biblia = json.load(arquivo)

    return biblia

def organizarLivro(biblia, livroAbrev, traduc):
    livro = fn.buscarJsonBiblia(
        biblia=biblia,
        abrev=livroAbrev
    )

    if livro == None:
        print("erro ao encontrar livro")
        st.error(f"Erro ao encontar livro pela abreviação: {livroAbrev}")
        return

    #%%-----------------------------------
    # Limpeza das palavras e organização dos objetos
    livro = fn.organizarLivro(livro, traduc)

    #%%-----------------------------------
    #tokenização
    fn.addTokens(livro)

    fn.addQuantPalavr(livro)

    return livro

def analisarLivros(livro1, livro2, traduc1, traduc2, St = False):
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
        "semelhanca_vers": semelhanVers,
        "traduc1": traduc1,
        "traduc2": traduc2
    }

    if True:
        chatSt(analise, livro1, livro2)

    return analise


def criarGraficos(dados, livro1, livro2, livroAbrev, St = False):
    palavrExcl_1 = dados["palavr_excl_1"]
    palavrExcl_2 = dados["palavr_excl_2"]
    traduc1 = dados["traduc1"]
    traduc2 = dados["traduc2"]

    semelhanVers = dados["semelhanca_vers"]
    #%%-------------------------------------
    #Criar graficos
    try:
        fig = fg.grafPlavrExcl( #mostra as n palavras exclusivas que mais aparecem
            lista=palavrExcl_1, 
            traducNome=traduc1.upper(), 
            nomeLivro=livro1[0]["livro"],
            abrevLivro=livroAbrev
        )

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar gráfico de palavras exclusivas ({traduc1}): {e}")
        if St: st.error(f"Erro ao criar gráfico de palavras exclusivas ({traduc1}): {e}")
    finally:
        plt.close()
    
    try:
        fig = fg.grafPlavrExcl(
            lista=palavrExcl_2, 
            traducNome=traduc2.upper(), 
            nomeLivro=livro1[0]["livro"],
            abrevLivro=livroAbrev
        )

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar gráfico de palavras exclusivas ({traduc2}): {e}")
        if St: st.error(f"Erro ao criar gráfico de palavras exclusivas ({traduc2}): {e}")
    finally:
        plt.close()

    try:
        fig = fg.histograma( #distribuição do nível de semelhança entre os versiculos
            lista=semelhanVers,
            traducNome1=livro1[0]["traducao"],
            traducNome2=livro2[0]["traducao"],
            abrevLivro=livroAbrev,
            nomeLivro=livro1[0]["livro"]
        )

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar histograma: {e}")
        if St: st.error(f"Erro ao criar histograma: {e}")
    finally:
        plt.close()

    try:
        fig = fg.heatmap( #mapa geral dos versiculos mais semelhantes
            lista=semelhanVers,
            traducNome1=livro1[0]["traducao"],
            traducNome2=livro2[0]["traducao"],
            abrevLivro=livroAbrev,
            nomeLivro=livro1[0]["livro"]
        )

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar heatmap: {e}")
        if St: st.error(f"Erro ao criar heatmap: {e}")
    finally:
        plt.close()

    try:
        fig = fg.grafTopSemelhanca( #mostra os top n versiculos mais semelhantes de cada capitulo do livro
            fn.topSemelhanPorCap(semelhanVers, 3),
            traducNome1=livro1[0]["traducao"],
            traducNome2=livro2[0]["traducao"],
            abrevLivro=livroAbrev,
            nomeLivro=livro1[0]["livro"]
        )

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar gráfico de top de semelhança: {e}")
        if St: st.error(f"Erro ao criar gráfico de top de semelhança: {e}")
    finally:
        plt.close()

    try:
        fig = fg.grafLinhas(livro1, livro2)

        if St: st.pyplot(fig)
    except Exception as e:
        print(f"Erro ao criar gráfico de linhas: {e}")
        if St: st.error(f"Erro ao criar gráfico de linhas: {e}")
    finally:
        plt.close()

def chatSt(dados, livro1, livro2):
    palavrExcl_1 = dados["palavr_excl_1"]
    palavrExcl_2 = dados["palavr_excl_2"]
    traduc1 = dados["traduc1"]
    traduc2 = dados["traduc2"]
    semelhanVers = dados["semelhanca_vers"]
    livroNome = livro1[0]['livro']

    def palavrExcl(traduc, list):
        lista = "\n".join(
            f"• {linha['palavra']} ({linha['quant']} ocorrência{'s' if linha['quant'] > 1 else ''})\n"
            for _, linha in list.iterrows()
        )
        texto = f"As 10 palavras exclusivas da tradução **{traduc}** que aparecem com maior frequência são:\n\n{lista}"
        st.chat_message("assistant").write(texto)
        time.sleep(2)
        print(texto)
    
    palavrExcl(traduc1, palavrExcl_1)
    palavrExcl(traduc2, palavrExcl_2)

    media = sum(v["similaridade"] for v in semelhanVers) / len(semelhanVers)
    texto = (
        f"Considerando todos os versículos analisados, as traduções "
        f"**{traduc1}** e **{traduc2}** apresentam uma similaridade média "
        f"de **{media:.1%}**."
    )
    st.chat_message("assistant").write(texto)
    print(texto)
    time.sleep(2)

    versMin = fn.topSemelhanPorCap(semelhanVers, 1)
    versMin = versMin.loc[versMin["similaridade"].idxmin()]
    for v in livro1:
        if v['cap'] == versMin['cap'] and v['vers'] == versMin['vers']:
            texto1 = v['texto']
            ref = v['id']
    for v in livro2:
        if v['cap'] == versMin['cap'] and v['vers'] == versMin['vers']:
            texto2 = v['texto']

    texto = (
        f"O versículo mais divergênte de **{livroNome}** entre as traduções **{traduc1}** e **{traduc2}** "
        f"é **{ref}**\n\n"
        f"{traduc1}: {texto1}\n\n"
        f"{traduc2}: {texto2}\n\n"
        f"com a similaridade de {versMin['similaridade'] * 100:.2f}%"
    )
    st.chat_message('assistant').write(texto)
    print(texto)
    time.sleep(2)



