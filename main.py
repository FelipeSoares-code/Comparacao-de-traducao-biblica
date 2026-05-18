import json
from funcoes import returnTxtBiblico

with open('NVT.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)


txt = returnTxtBiblico(
    biblia=bibliaArc,
    abrev='Jo',
    cap=1,
    vers=1
)

print(txt)


