def buscaMenor(arr):
    menor = arr[0]      #armazena menor valor
    menor_indice = 0    #armazena indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


meu_array = [10, 15, 8, 3, 20, 5]


def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #encontra o menor elemento e adiciona ao array
        novoArr.append(arr.pop(menor)) #o pop "arranca" o menor elemento do array!
    return novoArr


print(ordenacaoPorSelecao(meu_array))


