#! /usr/bin/env python3

import random
import time
import math

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
		print("Temperatura = ", temp)
		if(deltaE > 0):
			return options[prox]
		p = random.random()
		probabilidade = math.exp(deltaE/temp)
		time.sleep(1)
		if(probabilidade > p): 
			return options[prox]