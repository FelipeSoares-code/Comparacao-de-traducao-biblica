import json
from funcoes import buscarJsonBiblia, organizarLivro, addTokens, contPalavras, palavrSemelhantes, semelhancaTraduc

print("inicio")

#%%----------------------------------
# Abertura do texto original em json
print("Abrindo arquivos json...")
with open('traducoes/ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)

with open('traducoes/NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaNvt = json.load(arquivo)

#%%-----------------------------------
# escolha dos livros
livroArc = buscarJsonBiblia(
    biblia=bibliaArc,
    abrev='Jn'
)

livroNvt = buscarJsonBiblia(
    biblia=bibliaNvt,
    abrev='Jn'
)

#%%-----------------------------------
# Limpeza das palavras e organização dos objetos
print("Organizando livro...")
livroArc = organizarLivro(livroArc, "Arc")
livroNvt = organizarLivro(livroNvt, "Nvt")

#%%-----------------------------------
#tokenização
print("Separando palavras...")
addTokens(livroArc)
addTokens(livroNvt)
tokensTotal = []
for v in livroArc:
    tokensTotal.append(v["tokens"])
for v in livroNvt:
    tokensTotal.append(v["tokens"])

#%%----------------------------------
#contagem de palavras
print("Contando palavras...")
contPalvrArc = contPalavras(livroArc)
contPalavrNvt = contPalavras(livroNvt)

#%%-----------------------------------
#detectar novas palavras
palavrAntigas = set(contPalvrArc) - set(contPalavrNvt) #aparece na ARC e não na NVT
palavrNovas = set(contPalavrNvt) - set(contPalvrArc) #aparece na NVT e não na ARC

#%%------------------------------------
#buscar semelhanças semânticas entre palavras
palavrSemelhante = palavrSemelhantes(tokensTotal)
palavrSemelhante.wv.most_similar('deus')

#%%-------------------------------------
#buscar nível de semelhança entre versiculos
semelhanVers = semelhancaTraduc(livroArc, livroNvt)
print(semelhanVers)



