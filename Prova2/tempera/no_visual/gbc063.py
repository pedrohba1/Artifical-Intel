#! /usr/bin/env python3

import random
import math
import time

def algoritmo_profundidade(pos,options,visitados):
	visitados.append(pos)
	for i in options:
		if not (i in visitados):
			return i
	for i in range(len(visitados)):
		if(visitados[i] == pos):
			return visitados[i-1]

def algoritmo_aprofundamento_iterativo(pos,options,pilha,visitados,nivel):
	if not (pos in visitados):
		pilha.append(pos)
	visitados.append(pos)
	if pilha == []:
		nivel+=1
		return []
	if(len(pilha) == (nivel)+1):
		pilha.pop()
		return pilha[len(pilha)-1]
	else:
		for i in options:
			if not (i in visitados):
				return i
		for i in range(len(visitados)):
			if(visitados[i] == pos):
				pilha.pop()
				return visitados[i-1]

def subidaEncosta(current, options):
	menorCaminho = current
	resposta = calcMenorDistancia(menorCaminho,(9,9),options)
	if (resposta == current):
		return False
	menorCaminho = resposta
	return menorCaminho

def calcMenorDistancia(pos,end,options):
	menorCaminho = pos
	menorDistancia = distanciaManhattan(pos, end)
	for i in options:
			distancia = distanciaManhattan(i, (9,9))
			if distancia < menorDistancia:
				menorCaminho = i
				menorDistancia = distancia
	return menorCaminho

def distanciaManhattan(x, y):
	return abs(x[0] - y[0]) + abs(x[1] - y[1])

""" def distanciaEuclidiana(x, y):
    return math.sqrt(pow(x[0] - x[1], 2) + pow(y[0] - y[1], 2)) """
def tempera(pos,options,temp):
	if temp == 0:
		return 1
	while 1:
		prox = random.randint(0,len(options)-1)
		distAtual = distanciaManhattan(pos, (9,9))
		distaProx = distanciaManhattan(options[prox], (9,9))
		deltaE = distaProx - distAtual
		if(deltaE > 0):
			return options[prox]
		p = random.random()
		probabilidade = math.exp(deltaE/temp)
		if(probabilidade > p): 
			return options[prox]