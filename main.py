import json
from collections import Counter
from funcoes import buscarJsonBiblia, organizarLivro, addTokens, contarPalavras

print("inicio")

#----------------------------------
# Abertura do texto original em json
print("Abrindo arquivos json...")
with open('traducoes/ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)

with open('traducoes/NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaNvt = json.load(arquivo)

#-----------------------------------
# escolha dos livros
joaoArc = buscarJsonBiblia(
    biblia=bibliaArc,
    abrev="Jo"
)

joaoNvt = buscarJsonBiblia(
    biblia=bibliaNvt,
    abrev="jo"
)

#-----------------------------------
# Limpeza das palavras e organização dos objetos
print("Organizando livro...")
joaoArc = organizarLivro(joaoArc, "Arc")
joaoNvt = organizarLivro(joaoNvt, "Nvt")

#-----------------------------------
#tokenização
print("Separando palavras...")
addTokens(joaoArc)
addTokens(joaoNvt)

#----------------------------------
#contagem de palavras
print("Contando palavras...")
totalPalavrasArc = contarPalavras(joaoArc)
totalPalavrasNvt = contarPalavras(joaoNvt)



