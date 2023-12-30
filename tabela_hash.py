caderno = dict()
caderno["maçã"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49
print(caderno)

lista_telefonica = {}
lista_telefonica["jenny"] = 31989763123
lista_telefonica["emergency"] = 911
print(lista_telefonica)

votaram = {}

def verificar_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = "True"
        print("Deixe votar!")

verificar_eleitor("diogo")
verificar_eleitor("diogo")

cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = "dados de hello.com"
        cache[url] = "dados de hello.com"
        return dados
    
print(pega_pagina("hello.com"))
print(pega_pagina("hello"))