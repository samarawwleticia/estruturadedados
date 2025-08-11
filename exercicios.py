def soma(arr):
    if len(arr) == 0: #forma de checar se a lista esta vazia
        return 0
    else:
        return arr[0] + soma(arr[1:]) #soma o primeiro indice e divide o resto

aray = [1, 2, 3, 4]
print (soma(aray))

def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])

print (count(aray))

def buscaMaior(arr):
    maior = arr[0]      #armazena menor valor
    maior_indice = 0    #armazena indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            maior_indice = i
    return maior_indice

def buscaMaior_recursivo(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        head = arr[0]
        maior = buscaMaior_recursivo(arr[1:])
    if head > maior:
        return head
    else:
        return maior


aray = [1, 2, 3, 4]
print (buscaMaior_recursivo(aray))

