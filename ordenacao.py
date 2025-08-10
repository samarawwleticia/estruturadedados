def buscaMenor(arr):
    menor = arr[0]      #armazena menor valor
    menor_indice = 0    #armazena indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


meu_array = [10, 15, 3, 8, 20, 5]

print (meu_array[buscaMenor(meu_array)])

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #encontra o menor elemento e adiciona ao array
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoPorSelecao(meu_array))
