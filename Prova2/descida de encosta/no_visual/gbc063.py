#! /usr/bin/env python3

import random
import time


def distanciaManhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

""" def distanciaEuclidiana(x, y):
    return math.sqrt(pow(x[0] - x[1], 2) + pow(y[0] - y[1], 2)) """
   
def calcMenorDistancia(pos,end,options):
    menorCaminho = pos
    menorDistancia = distanciaManhattan(pos, end)
    for i in options:
        distancia = distanciaManhattan(pos, i)
        if distancia < menorDistancia:
            menorCaminho = i
            menorDistancia = distancia
    if menorCaminho == pos:
        return False
    return menorCaminho

def subidaEncosta(current, options):
    menorCaminho = current
    while True:
        resposta = calcMenorDistancia(menorCaminho,(9,9),options)
        if resposta == False:
            break
        menorCaminho = resposta
    return menorCaminho