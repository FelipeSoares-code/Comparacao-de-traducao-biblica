def buscarTxtBiblico(biblia, livro = None, abrev = None, cap = None, vers = None):
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
    
    
    
