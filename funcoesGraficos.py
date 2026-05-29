import matplotlib.pyplot as plt


def criarHistograma(lista):
    sim = []
    for l in lista:
        sim.append(l["similaridade"])

    plt.hist(sim, bins=20)
    plt.title("Distribuição de Similaridade Entre as Traduções")
    plt.xlabel("Pontos de Similaridade")
    plt.ylabel("Quantidade de Versículos")

    plt.show()
    plt.savefig("histograma.png")

    return plt

def criarGrafLinhas(livro1, livro2):
    def calcMediaCap(livro): 
        medias = []
        capAtual = livro[0]["capitulo"]
        soma = 0
        quantV = 0
        for v in livro:
            if capAtual == v["capitulo"]:
                soma += v["quant_palavras"]
                quantV += 1
            else:
                medias.append(soma / quantV)
                capAtual = v["capitulo"]
                soma = v["quant_palavras"] #reinicia pelo primeiro vers
                quantV = 1

        # adiciona último capítulo
        medias.append(soma / quantV)
        return medias

    list1 = calcMediaCap(livro1)
    list2 = calcMediaCap(livro2)    

    plt.figure(figsize=(14,6))

    lenCapitulos = range(1, len(list1) + 1) #pega a quantidade de capitulos pela tamanho do array

    plt.plot(lenCapitulos, list1, label=livro1[0]["traducao"])
    plt.plot(lenCapitulos, list2, label=livro2[0]["traducao"])

    plt.xticks(lenCapitulos) #marca quais devem ser as marcações em no eixo x

    plt.title("Quantidade Média de Palavras por Versiculo")
    plt.xlabel("Capítulo")
    plt.ylabel("Quantidade de Palavras")

    plt.legend()

    plt.show()
    plt.savefig("linhas.png")

    return plt