import json
import funcoes as fn
import funcoesGraficos as fg

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
livroArc = fn.buscarJsonBiblia(
    biblia=bibliaArc,
    abrev='cl'
)

livroNvt = fn.buscarJsonBiblia(
    biblia=bibliaNvt,
    abrev='cl'
)

#%%-----------------------------------
# Limpeza das palavras e organização dos objetos
print("Organizando livro...")
livroArc = fn.organizarLivro(livroArc, "Arc")
livroNvt = fn.organizarLivro(livroNvt, "Nvt")

#%%-----------------------------------
#tokenização
print("Separando palavras...")
fn.addTokens(livroArc)
fn.addTokens(livroNvt)
tokensTotal = []
for v in livroArc:
    tokensTotal.append(v["tokens"])
for v in livroNvt:
    tokensTotal.append(v["tokens"])

fn.addQuantPalavr(livroArc)
fn.addQuantPalavr(livroNvt)

#%%----------------------------------
#contagem de palavras
print("Contando palavras...")
contPalvrArc = fn.contPalavras(livroArc)
contPalavrNvt = fn.contPalavras(livroNvt)

#%%-----------------------------------
#detectar novas palavras
palavrAntigas = set(contPalvrArc) - set(contPalavrNvt) #aparece na ARC e não na NVT
palavrNovas = set(contPalavrNvt) - set(contPalvrArc) #aparece na NVT e não na ARC

#%%------------------------------------
#buscar semelhanças semânticas entre palavras
# palavrSemelhante = fn.palavrSemelhantes(tokensTotal)

#%%-------------------------------------
#buscar nível de semelhança entre versiculos
semelhanVers = fn.semelhancaTraduc(livroArc, livroNvt)

fg.criarHistograma(
    semelhanVers,
    traducName1=livroArc[0]["traducao"],
    traducNome2=livroNvt[0]["traducao"],
    abrevLivro=livroArc[0]["abrev"],
    nomeLivro=livroArc[0]["livro"]
)

#%%-------------------------------------
#comparar quantidade média de palavras por versiculo no capítulo
fg.criarGrafLinhas(livroArc, livroNvt)

fg.criarHeatmap(
    lista=semelhanVers,
    traducName1=livroArc[0]["traducao"],
    traducNome2=livroNvt[0]["traducao"],
    abrevLivro=livroArc[0]["abrev"],
    nomeLivro=livroArc[0]["livro"]
)

print(fn.topSemelhanPorCap(semelhanVers, 3))




