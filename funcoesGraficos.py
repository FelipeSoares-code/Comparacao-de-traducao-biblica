import matplotlib.pyplot as plt


def criarHistograma(lista):
    sim = []
    for l in lista:
        sim.append(l["similaridade"])

    plt.hist(sim, bins=20)
    plt.title("Distribuição de Similaridade")
    plt.xlabel("Score de Similaridade")
    plt.ylabel("Quantidade de Versículos")

    plt.show()
    plt.savefig("histograma.png")