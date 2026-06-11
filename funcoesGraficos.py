import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as fn
import numpy as np
import pandas as pd

saveFig = False

def histograma(lista, traducNome1, traducNome2, abrevLivro, nomeLivro):
    sim = []
    for l in lista:
        sim.append(l["similaridade"])

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.histplot(
        sim,
        bins=20,
        kde=False,
        edgecolor="black",
        linewidth=1,
        ax=ax
    )

    ax.axvline(np.mean(sim), linestyle="--", linewidth=2, label="Média")
    ax.axvline(np.median(sim), linestyle=":", linewidth=2, label="Mediana")

    ax.grid(axis="y", alpha=0.3)
    ax.legend()

    titulo = f"Distribuição de Similaridade Entre {traducNome1.upper()} e {traducNome2.upper()} - Livro: {nomeLivro}"

    ax.set_title(titulo)
    ax.set_xlabel("Similaridade")
    ax.set_ylabel("Quantidade de Versículos")

    fig.tight_layout()
    nomeFig = f"histograma_{traducNome1}_{traducNome2}_{abrevLivro}.png"

    if saveFig: fig.savefig("graficos/" + nomeFig);

    return fig

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

    fig, ax = plt.subplots(figsize=(14,6))

    # lenCapitulos = range(1, len(list1) + 1) #pega a quantidade de capitulos pela tamanho do array
    nomeTraduc1 = livro1[0]["traducao"].upper()
    nomeTraduc2 = livro2[0]["traducao"].upper()
    abrev = livro1[0]["abrev"].lower()

    ax.plot(eixoX, list1, label=nomeTraduc1)
    ax.plot(eixoX, list2, label=nomeTraduc2)

    # plt.xticks(lenCapitulos) #marca quais devem ser as marcações em no eixo x
    ax.grid(axis="y", alpha=0.3)

    ax.set_title(f"Quantidade Média de Palavras por Versiculo - Livro: {livro1[0]['livro']}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Quantidade de Palavras")

    ax.legend()
    fig.tight_layout()
    
    nomeFig = f"linhas_{nomeTraduc1.lower()}_{nomeTraduc2.lower()}_{abrev}"

    if saveFig: fig.savefig("graficos/" + nomeFig);

    return fig

def heatmap(lista, traducNome1, traducNome2, abrevLivro, nomeLivro):
    df = pd.DataFrame(lista)

    matriz = df.pivot(
        index="cap",
        columns="vers",
        values="similaridade"
    )

    fig, ax = plt.subplots(figsize=(20, 8))

    sns.heatmap(
        matriz,
        linewidths=0.2,
        cmap="Greens",
        cbar_kws={"label": "Similaridade"}
    )

    ax.set_xticks(ax.get_xticks()[::2])
    ax.tick_params(axis='x', rotation=90)

    titulo = f"Divergência Entre {traducNome1.upper()} e {traducNome2.upper()} - Livro: {nomeLivro}"
    
    nomeFig = f"heatmap_{traducNome1}_{traducNome2}_{abrevLivro}.png"
    
    ax.set_title(titulo)
    ax.set_xlabel("Versículo")
    ax.set_ylabel("Capítulo")
    if saveFig: fig.savefig("graficos/" + nomeFig);

    return fig    

def grafTopSemelhanca(topPorCap, traducNome1, traducNome2, nomeLivro, abrevLivro):
    topPorCap["ref"] = (
        topPorCap["cap"].astype(str)
        + ":"
        + topPorCap["vers"].astype(str)
    )

    fig, ax = plt.subplots(figsize=(15, 6))

    sns.barplot(
        data=topPorCap,
        x="ref",
        y="similaridade",
        palette="dark:blue",
        hue="similaridade"
    )

    ax.grid(
        axis='y',      # linhas horizontais
        linestyle='--',# tracejado
        linewidth=0.8, # espessura
        alpha=0.5      # transparência
    )

    ax.tick_params(axis="x", rotation=90)

    titulo = f"Versículos Mais Divergentes Entre {traducNome1.upper()} e {traducNome2.upper()} Por Capítulo - Livro: {nomeLivro}"

    ax.set_title(titulo)
    ax.set_ylabel("Similaridade")
    ax.set_xlabel("Versículos")

    nomeFig = f"semelhanca_por_cap_{traducNome1}_{traducNome2}_{abrevLivro}.png"

    fig.tight_layout()
    if saveFig: fig.savefig("graficos/" + nomeFig);

    return fig 

def grafPlavrExcl(lista, traducNome, nomeLivro, abrevLivro):
    fig, ax = plt.subplots(figsize=(15,6))

    ax.grid(
        axis='y',      # linhas horizontais
        linestyle='--',# tracejado
        linewidth=0.8, # espessura
        alpha=0.5      # transparência
    )

    sns.barplot(
        data=lista,
        x="palavra",
        y="quant",
        color="orange",
    )

    ax.set_ylabel("Quantidade de Aparições")

    titulo = f"Palavras Exclusivas da Tradução {traducNome} Que Mais se Repetem - Livro: {nomeLivro}"
    nomeFig = f"palavras_exclusivas_{traducNome}_{abrevLivro}.png"

    ax.set_title(titulo)
    fig.tight_layout()
    if saveFig: fig.savefig("graficos/" + nomeFig);

    return fig

    

    

    

