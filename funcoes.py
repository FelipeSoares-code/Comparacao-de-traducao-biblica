def returnTxtBiblico(biblia, livro = None, abrev = None, cap = None, vers = None):
    #estrutura do json:
    #"abbrev"[], "chapters"[[...]], "name"[]
    #como pegar um versiculo: livro[chapters][capitulo - 1][versiculo - 1]
    Livro = None
    
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
        return Livro["chapters"][cap - 1]
    
    if vers > len(Livro["chapters"][cap - 1]):
        return None
    
    return Livro["chapters"][cap - 1][vers - 1]
    
    
    
