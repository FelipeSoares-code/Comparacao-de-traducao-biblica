import re, spacy
from collections import Counter
from gensim.models import FastText
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

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
            versLimpo = {
                "traducao": nomeTraducao.lower(),
                "livro": livro["name"],
                "capitulo": i,
                "vers": j,
                "texto": vers,
                "texto_limpo": re.sub(r'[^\w\s]', '', vers.lower()),                
            }
            livroLimpo.append(versLimpo)

    return livroLimpo

def addTokens(livroLimpo):
    nlp = spacy.load("pt_core_news_sm")

    for v in livroLimpo:
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
    for l in livro:
        contador.update(l['tokens'])
    return contador

def palavrSemelhantes(tokens):
    modelo = FastText(
        sentences=tokens,
        vector_size=100,
        window=5,
        min_count=1
    )
    return modelo

def semelhancaTraduc(traduc1, traduc2):
    resultados = []
    modelo = SentenceTransformer(
        'paraphrase-multilingual-MiniLM-L12-v2'
    )
    #Gerar embeddings
    for v1 in traduc1:
        emb1 = modelo.encode(v1["texto_limpo"])
        for v2 in traduc2:
            if (
                v2["capitulo"] == v1["capitulo"] and 
                v2["vers"] == v1["vers"]
            ):
                emb2 = modelo.encode(v2["texto_limpo"])
            break
        
        sim = cosine_similarity(
            [emb1],
            [emb2]
        )[0][0]

        resultados.append({
            "capitulo": v1["capitulo"],
            "versiculo": v2["vers"],
            "similaridade": float(sim)
        })

    return resultados