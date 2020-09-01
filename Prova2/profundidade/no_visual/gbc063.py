#! /usr/bin/env python3

import random
import time

def algoritmo_profundidade(pos,options,visitados):
	visitados.append(pos)
	for i in options:
		if not (i in visitados):
			return i
	for i in range(len(visitados)):
		if(visitados[i] == pos):
			return visitados[i-1]
