import json
from funcoes import returnTxtBiblico

with open('ARC.json', 'r', encoding='utf-8') as arquivo:
    bibliaArc = json.load(arquivo)


txt = returnTxtBiblico(
    biblia=bibliaArc,
    livro="João",
    cap=1,
    vers=1
)

print(txt)


