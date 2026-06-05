import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as fn
import numpy as np
import pandas as pd


def histograma(lista, traducNome1 = None, traducNome2 = None, abrevLivro = None, nomeLivro = None):
    sim = []
    for l in lista:
        sim.append(l["similaridade"])

    plt.figure(figsize=(12, 6))

    sns.histplot(
        sim,
        bins=20,
        kde=False,
        edgecolor="black",
        linewidth=1
    )

    plt.axvline(np.mean(sim), linestyle="--", linewidth=2, label="Média")
    plt.axvline(np.median(sim), linestyle=":", linewidth=2, label="Mediana")

    plt.grid(axis="y", alpha=0.3)
    plt.legend()

    titulo = \
        f"Distribuição de Similaridade Entre {traducNome1.upper()} e {traducNome2.upper()} - Livro: {nomeLivro}" \
        if (None not in (traducNome1, traducNome2, nomeLivro)) \
        else "Distribuição de Similaridade Entre as Traduções"

    plt.title(titulo)
    plt.xlabel("Similaridade")
    plt.ylabel("Quantidade de Versículos")

    plt.tight_layout()
    nomeFig = f"histograma_{traducNome1}_{traducNome2}_{abrevLivro}.png" if None not in (traducNome1, traducNome2, abrevLivro) else "histograma.png"
    plt.savefig(nomeFig)
    plt.show()

    return plt

def grafLinhas(livro1, livro2):
    if len(livro1) <= 100:
        list1 = [v["quant_palavras"] for v in livro1]
        list2 = [v["quant_palavras"] for v in livro2]
        eixoX = range(1, len(list1) + 1)
        xlabel = "Versículo"
    else:
        # mostra média por capítulo
        list1 = fn.calcMediaCap(livro1)
        list2 = fn.calcMediaCap(livro2)
        eixoX = range(1, len(list1) + 1)
        xlabel = "Capítulo"

    plt.figure(figsize=(14,6))

    lenCapitulos = range(1, len(list1) + 1) #pega a quantidade de capitulos pela tamanho do array
    nomeTraduc1 = livro1[0]["traducao"].upper()
    nomeTraduc2 = livro2[0]["traducao"].upper()
    abrev = livro1[0]["abrev"]

    plt.plot(eixoX, list1, label=nomeTraduc1)
    plt.plot(eixoX, list2, label=nomeTraduc2)

    # plt.xticks(lenCapitulos) #marca quais devem ser as marcações em no eixo x
    plt.grid(axis="y", alpha=0.3)

    plt.title(f"Quantidade Média de Palavras por Versiculo - Livro: {livro1[0]['livro']}")
    plt.xlabel(xlabel)
    plt.ylabel("Quantidade de Palavras")

    plt.legend()
    plt.tight_layout()
    
    nomeFig = f"linhas_{nomeTraduc1.lower()}_{nomeTraduc2.lower()}_{abrev}" if None not in (nomeTraduc1, nomeTraduc2, abrev) else "linhas.png"
    plt.savefig(nomeFig)
    plt.show()

    return plt

def heatmap(lista, traducNome1 = None, traducNome2 = None, abrevLivro = None, nomeLivro = None):
    df = pd.DataFrame(lista)

    matriz = df.pivot(
        index="cap",
        columns="vers",
        values="similaridade"
    )

    plt.figure(figsize=(20, 8))

    plt.xticks(rotation=90)

    ax = sns.heatmap(
        matriz,
        linewidths=0.2,
        cmap="Greens",
        cbar_kws={"label": "Similaridade"}
    )

    

    ax.set_xticks(ax.get_xticks()[::2])
    ax.tick_params(axis='x', rotation=90)

    titulo = \
        f"Divergência Entre {traducNome1.upper()} e {traducNome2.upper()} - Livro: {nomeLivro}" \
        if (None not in (traducNome1, traducNome2, nomeLivro)) \
        else "Divergência Entre as Traduções"
    
    nomeFig = f"heatmap_{traducNome1}_{traducNome2}_{abrevLivro}.png" \
        if None not in (traducNome1, traducNome2, abrevLivro) else "heatmap.png"
    
    plt.title(titulo)
    plt.xlabel("Versículo")
    plt.ylabel("Capítulo")
    plt.savefig(nomeFig)
    plt.show()

    return plt

def grafTopSemelhanca(topPorCap, traducNome1 = None, traducNome2 = None, nomeLivro = None, abrevLivro = None):
    topPorCap["ref"] = (
        topPorCap["cap"].astype(str)
        + ":"
        + topPorCap["vers"].astype(str)
    )

    plt.figure(figsize=(15, 6))

    sns.barplot(
        data=topPorCap,
        x="ref",
        y="similaridade",
        color="blue",
        hue="similaridade"
    )

    plt.xticks(rotation=45)

    titulo = \
        f"Versículos Mais Divergentes Entre {traducNome1.upper()} e {traducNome2.upper()} Por Capítulo - Livro: {nomeLivro}" \
        if (None not in (traducNome1, traducNome2, nomeLivro)) \
        else "Versículos Mais Divergentes"

    plt.title(titulo)
    plt.ylabel("Similaridade")

    nomeFig = f"semelhanPorCap{traducNome1}_{traducNome2}_{abrevLivro}.png" \
        if None not in (traducNome1, traducNome2, abrevLivro) else "semelhanPorCap.png"

    plt.tight_layout()
    plt.savefig(nomeFig)
    plt.show()