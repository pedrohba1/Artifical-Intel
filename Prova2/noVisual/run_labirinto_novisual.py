#! /usr/bin/env python3
'''
PyMaze driver class. Makes use of the maze class to parse program arguments.
@author: Paul Miller (github.com/138paulmiller)
adpated by Dino Franklin
'''

import os, sys, random, time, threading
import maze_gbc063_novisual as maze
import gbc063


def play_maze(maze_obj, limit):
	
	current = (0,0)
	# em (0,0) pergunta para o labirinto acoes possiveis
	info = maze_obj.move(current)
	current = info[1]
	options = info[2]
		
	move = 0

	# sai qdo a quant de movimentos > limite ou chegou na solucao
	while not (move > limit) and not maze_obj.is_done():
		action = gbc063.algoritmo(current, options)

	#	para debug: escreve a posicao atual e as acoes possiveis
	#	print('pos:',current,'\noptions\n')
	#	for i in range(len(options)):
	#		print(options[i])
	#	print('action:',action)	

		info = maze_obj.move(action)
		current = info[1]
		options = info[2]
		
		move += 1


	# saindo
	if (move < limit):
		print('Objetivo atingido em ',move,' movimentos!');
		print('Solucao (',len(maze_obj.path),' passos ):')
		print(maze_obj.path)
	else:
		print('Vc fez ',move,' movimentos sem sucesso!\n','Tente de novo!\n\n');
		

def main():

	# set opcoes 
	seed = random.random()*10000		
	width = 10	#20
	height = 10 	#12
	limite = 5000
	
	# cria o labirinto
	maze_obj = maze.Maze(width, height, seed)

	# usa seu algoritmo (gbc063) para sair do labirinto
	play_maze(maze_obj,limite)


# main
if __name__ == '__main__':
	main() 
