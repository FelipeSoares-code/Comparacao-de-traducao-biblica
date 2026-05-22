import json
from funcoes import buscarTxtBiblico, limparLivro


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

print(joaoArcLimpo["capitulo"][0])


#-----------------------------------
#tokenização


