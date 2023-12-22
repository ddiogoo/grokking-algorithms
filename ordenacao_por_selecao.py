# Complexidade O(n²)
def busca_menor(arr) -> int:
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr) -> list:
    novoArr = []
    for _ in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

arr = ordenacao_por_selecao([9, 7, 6, 4, 3, 10])
for n in arr:
    print(n)