def geracao_zero(qtd):
    numeros = []
    binarios = []
    for n in range(qtd):
        numeros.append(random.randint(0,32))
    for k in range(qtd):
        binarios.append(converterd_b(numeros[k]))
    binarios = binarios.sort()

    return binarios

def fitness(list):
    fitness = []
    calculo = (100(list[x+1] - (list[x] ** 2) ** 2) + ((list[x] - 1) ** 2))
    somatorio = int

    for x in range(len(list)):
        somatorio += (100(list[x+1] - (list[x] ** 2) ** 2) + ((list[x] - 1) ** 2)) 
        fitness.append()
    
    return fitness

def pais(list):
    pais = []
    ftnspais = []
    ftnspais = fitness(list)

    pais.append(list[ftnspais.index(max(ftnspais))])
    pais.append(list[ftnspais.index(max(ftnspais))-1])

    return pais




geracao = geracao_zero(4)
print (geracao)
print (pais(fitness(geracao)))