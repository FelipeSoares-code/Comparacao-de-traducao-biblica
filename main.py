import json, re
from funcoes import buscarTxtBiblico

with open('traducoes/ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)

with open('traducoes/NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaNvt = json.load(arquivo)

joaoArc = buscarTxtBiblico(
    biblia=bibliaArc,
    abrev="Jo"
)

joaoNvt = buscarTxtBiblico(
    biblia=bibliaNvt,
    abrev="jo"
)

joaoArcLimpo = {}
joaoNvtLimpo = {}
for i, cap in enumerate(joaoArc["chapters"], start=1):
    for j, vers in enumerate(cap, start=1):
        textoLimpo = re.sub(r'[^\w\s]', '', vers.lower())
        joaoArcLimpo[(i, j)] = re.sub(r'[^\w\s]', '', vers.lower())

for i, cap in enumerate(joaoNvt["chapters"], start=1):
    for j, vers in enumerate(cap, start=1):
        textoLimpo = re.sub(r'[^\w\s]', '', vers.lower())
        joaoNvtLimpo[(i, j)] = re.sub(r'[^\w\s]', '', vers.lower())

#estrutura de busca de versículo: João 3:16 -> joaoArcLimpo[(3, 16)]

print(joaoArcLimpo[(1,1)])

