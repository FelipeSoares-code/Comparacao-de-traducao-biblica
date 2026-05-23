import json
from funcoes import buscarTxtBiblico, limparLivro, tokenizarLivro


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

print(joaoArcTokens[(1,1)])
print(joaoNvtTokens[(1,1)])
print(joaoArcLimpo[(1,1)])
print(joaoNvtLimpo[(1,1)])

#----------------------------------
#contagem de palavras


