## Caso-base e caso recursivo
def regressiva(i):
    print(i)
    if i <= 1: ## Caso-base
        return
    else: ## Caso recursivo
        regressiva(i-1)

regressiva(10)

'''
## Pseudocódigo: a execução dos códigos abaixo não vai funcionar

def procure_pela_chave(caixa_principal):
    pilha = main_box.crie_uma_pilha_para_busca()
    while pilha is not vazia:
        caixa = pilha.pegue_uma_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("achei a chave!")
                
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item) ## Recursão!
        elif item.e_uma_chave():
            print("achei uma chave!")
'''