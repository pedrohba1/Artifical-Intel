#! /usr/bin/env python3

import random
import time


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
		