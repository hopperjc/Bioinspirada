import random
import math

def geracao_zero(qtd):
    a = -2.048
    b = 2.048
    numeros = []
    for n in range(qtd):
        numeros.append(random.uniform(a,b))

    return numeros

def calculo(x):
    resultado = (100*((x - (x**2))**2) + ((x - 1)**2))

    return resultado

def fitness(list):
    fitness = []
    
    for x in range(len(list)):
        fitness.append(math.fabs(calculo(x)))

    return fitness

def pais(list):
    pais = []
    ftnspais = []
    ftnspais = fitness(list)

    pais.append(list[ftnspais.index(min(ftnspais))])
    
    list[ftnspais.index(min(ftnspais))] = 1500
    
    pais.append(list[ftnspais.index(min(ftnspais))])

    return pais




geracao = geracao_zero(4)
print (calculo(-0.24))
print (fitness(geracao))
print (geracao)
print (pais(fitness(geracao)))