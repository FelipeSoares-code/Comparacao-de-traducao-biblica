import json
from collections import Counter
from funcoes import buscarTxtBiblico, limparLivro, tokenizarLivro, contarPalavras


#----------------------------------
# Abertura do texto original em json
with open('traducoes/ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)

with open('traducoes/NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaNvt = json.load(arquivo)

#-----------------------------------
# escolha dos livros
joaoArc = buscarTxtBiblico(
    biblia=bibliaArc,
    abrev="Jo"
)

joaoNvt = buscarTxtBiblico(
    biblia=bibliaNvt,
    abrev="jo"
)

#-----------------------------------
# Limpeaza das palavras
joaoArcLimpo = limparLivro(joaoArc)
joaoNvtLimpo = limparLivro(joaoNvt)


#-----------------------------------
#tokenização
joaoArcTokens = tokenizarLivro(joaoArcLimpo)
joaoNvtTokens = tokenizarLivro(joaoNvtLimpo)

#----------------------------------
#contagem de palavras
totalPalavrasArc = contarPalavras(joaoArcTokens)
totalPalavrasNvt = contarPalavras(joaoNvtTokens)

