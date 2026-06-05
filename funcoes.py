import re, spacy
from collections import Counter
from gensim.models import FastText
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def buscarJsonBiblia(biblia, livro = None, abrev = None, cap = None, vers = None):
    #estrutura do json:
    #"abbrev"[], "chapters"[[...]], "name"[]
    #como pegar um versiculo: livro[chapters][capitulo - 1][versiculo - 1]
    Livro = None
    if cap in (0, None):
        cap = None
    else: 
        cap = cap - 1 if cap > 0 else cap

    if vers in (0, None): 
        vers = None
    else:
        vers = vers - 1 if vers > 0 else vers
    
    if livro is not None:
        livro = livro.lower()

    if abrev is not None:
        abrev = abrev.lower()

    for l in biblia:
        if l["name"].lower() == livro or l["abbrev"].lower() == abrev:
            Livro = l
            break
    
    if Livro == None:
        return None
    
    if cap == None:
        return Livro
    
    if cap > len(Livro["chapters"]):
        return None
    
    if vers == None:
        return Livro["chapters"][cap]
    
    if vers > len(Livro["chapters"][cap]):
        return None
    
    return Livro["chapters"][cap][vers]
    
    
def organizarLivro(livro, nomeTraducao):
    #estrutura de busca de versículo: João 3:16 -> joaoArcLimpo[(3, 16)]
    livroLimpo = []
    for i, cap in enumerate(livro["chapters"], start=1):
        for j, vers in enumerate(cap, start=1):
            if isinstance(vers, list): #para caso o versiculo seja uma list
                vers = " ".join(vers)
            versLimpo = {
                "id": f'{livro["name"]} {i}:{j}',
                "traducao": nomeTraducao.lower(),
                "livro": livro["name"],
                "abrev": livro["abbrev"],
                "cap": i,
                "vers": j,
                "texto": vers,
                "texto_limpo": re.sub(r'[^\w\s]', '', vers.lower()),                
            }
            livroLimpo.append(versLimpo)

    return livroLimpo

def addTokens(livro):
    nlp = spacy.load("pt_core_news_sm")

    for v in livro:
        doc = nlp(v['texto_limpo'])

        v.update({
            "tokens": [
                token.text
                for token in doc
                if not token.is_stop and not token.is_punct #remove artigos, preposições etc
            ]
        })

def contPalavras(livro):
    contador = Counter()
    for v in livro:
        contador.update(v['tokens'])
    return contador

def palavrSemelhantes(tokens):
    modelo = FastText(
        sentences=tokens,
        vector_size=100,
        window=5,
        min_count=1
    )
    return modelo

def semelhanTraduc(traduc1, traduc2):
    resultados = []

    modelo = SentenceTransformer(
        'paraphrase-multilingual-MiniLM-L12-v2'
    )

    emb_traduc2 = {}

    for v2 in traduc2:
        chave = (v2["cap"], v2["vers"])

        emb_traduc2[chave] = modelo.encode(
            v2["texto_limpo"]
        )

    for v1 in traduc1:
        chave = (v1["cap"], v1["vers"])

        if chave in emb_traduc2:
            emb1 = modelo.encode(v1["texto_limpo"])
            emb2 = emb_traduc2[chave]

            sim = cosine_similarity(
                [emb1],
                [emb2]
            )[0][0]

            resultados.append({
                "cap": v1["cap"],
                "vers": v1["vers"],
                "similaridade": float(sim)
            })

    return resultados

def addQuantPalavr(livro):
    for v in livro:
        quant = len(v["tokens"])
        v.update({
            "quant_palavras": quant
        })

def calcMediaCap(livro): 
    medias = []
    capAtual = livro[0]["cap"]
    soma = 0
    quantV = 0
    for v in livro:
        if capAtual == v["cap"]:
            soma += v["quant_palavras"]
            quantV += 1
        else:
            medias.append(soma / quantV)
            capAtual = v["cap"]
            soma = v["quant_palavras"] #reinicia pelo primeiro vers
            quantV = 1

    # adiciona último capítulo
    medias.append(soma / quantV)
    return medias

def topSemelhanPorCap(lista, quantPorCap):
    df = pd.DataFrame(lista)

    topPorCap = (
        df.sort_values("similaridade")
            .groupby("cap")
            .head(quantPorCap)
            .sort_values(["cap", "vers"])
            .reset_index(drop=True)
    )

    return topPorCap

def topPalavrExcl(listPalvrExcl, livro, quantPalavras):
    dados = []
    for p in listPalvrExcl:
        quant_p = 0

        for v in livro:
            quant_p += v['tokens'].count(p)

        dados.append({
            "palavra" : p,
            "quant" : quant_p
        })

    df = pd.DataFrame(dados)

    topPalavr = (
        df.sort_values("quant", ascending=False)
            .head(quantPalavras)
            .reset_index(drop=True)
    )

    return topPalavr
        
