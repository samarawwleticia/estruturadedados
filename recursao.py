# primeira forma que usa várias funções diferentes :( 

def procure_pela_chave(caixa_principal):
    pilha = caixa_principal.cria_pilha()
    while pilha is not vazia:
        caixa = pilha.get_caixa()
        for item in caixa:
            if item.ser_caixa():
                pilha.append(item)
            elif item.ser_chave():
                print ("achei a chave!")


# segunda forma - utilizando recursao :D

def procure_pela_chave(caixa):
    for item in caixa:
        if item.eh_caixa():
            procure_pela_chave(item)
        elif item.eh_chave():
            print "achei a chave!"
