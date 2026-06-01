import matplotlib.pyplot as plt
import seaborn as sns
import funcoes as fn
import numpy as np


def criarHistograma(lista, traducName1 = None, traducNome2 = None, abrevLivro = None, nomeLivro = None):
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
        f"Distribuição de Similaridade Entre {traducName1.upper()} e {traducNome2.upper()} - Livro: {nomeLivro}" \
        if (None not in (traducName1, traducNome2, nomeLivro)) \
        else "Distribuição de Similaridade Entre as Traduções"

    plt.title(titulo)
    plt.xlabel("Similaridade")
    plt.ylabel("Quantidade de Versículos")

    plt.tight_layout()
    nomeFig = f"histograma_{traducName1}_{traducNome2}_{abrevLivro}.png" if None not in (traducName1, traducNome2, abrevLivro) else "histograma.png"
    plt.savefig(nomeFig)
    plt.show()

    return plt

def criarGrafLinhas(livro1, livro2):
    list1 = fn.calcMediaCap(livro1)
    list2 = fn.calcMediaCap(livro2)    

    plt.figure(figsize=(14,6))

    lenCapitulos = range(1, len(list1) + 1) #pega a quantidade de capitulos pela tamanho do array
    nomeTraduc1 = livro1[0]["traducao"].upper()
    nomeTraduc2 = livro2[0]["traducao"].upper()
    abrev = livro1[0]["abrev"]

    plt.plot(lenCapitulos, list1, label=nomeTraduc1)
    plt.plot(lenCapitulos, list2, label=nomeTraduc2)

    # plt.xticks(lenCapitulos) #marca quais devem ser as marcações em no eixo x
    plt.grid(axis="y", alpha=0.3)

    plt.title(f"Quantidade Média de Palavras por Versiculo - Livro: {livro1[0]['livro']}")
    plt.xlabel("Capítulo")
    plt.ylabel("Quantidade de Palavras")

    plt.legend()
    plt.tight_layout()
    
    nomeFig = f"linhas_{nomeTraduc1.lower()}_{nomeTraduc2.lower()}_{abrev}" if None not in (nomeTraduc1, nomeTraduc2, abrev) else "linhas.png"
    plt.savefig(nomeFig)
    plt.show()

    return plt