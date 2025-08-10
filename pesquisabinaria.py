def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 # len(lista) retorna a qtd de elementos no array e nao o tamanho dele

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item: # se acertar, retorna item
            return meio
        if chute > item:
            alto = meio - 1 # se o chute for alto, atualiza o alto
        else: 
            baixo = meio + 1 # se chute for baixo, atualiza o baixo
    return None # se o item nao estiver na lista, nao retorna nada

    #se o chute for muito baixo - atualiza variavel baixo

    if chute < item:
        baixo = meio + 1


minha_lista = [1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 26] # a lista deve ser ordenada 

print (pesquisa_binaria(minha_lista, 26))
print (pesquisa_binaria(minha_lista, -1))