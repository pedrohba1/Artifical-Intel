#! /usr/bin/env python3
'''
PyMaze driver class. Makes use of the maze class to parse program arguments.
@author: Paul Miller (github.com/138paulmiller)
adapted by Dino Franklin
'''

import os, sys, random, time, threading
import maze_gbc063_novisual as maze
from concluded_maze import *
import csv
import matplotlib.pyplot as plt
import gbc063





# defalt ANSI settings from user
COLOR_DEFAULT = u'\u001b[0m'
# foreground colors (text)
COLOR_BLACK = u'\u001b[30m'
COLOR_RED =  u'\u001b[31m'
COLOR_GREEN = u'\u001b[32m'
COLOR_YELLOW = u'\u001b[33m'
COLOR_BLUE  =u'\u001b[34m'
COLOR_MAGENTA = u'\u001b[35m'
COLOR_CYAN = u'\u001b[36m'
COLOR_WHITE = u'\u001b[37m'
# background colors 
COLOR_BG_BLACK = u'\u001b[40m'
COLOR_BG_RED =	u'\u001b[41m'
COLOR_BG_GREEN =  u'\u001b[42m'
COLOR_BG_YELLOW = u'\u001b[43m'
COLOR_BG_BLUE = u'\u001b[44m'
COLOR_BG_MAGENTA =  u'\u001b[45m'
COLOR_BG_CYAN = u'\u001b[46m'
COLOR_BG_WHITE= u'\u001b[47m'






def play_maze(maze_obj, limit,tinkle):
	
	#clear the screen clear if linux, cls if windows
	os.system('clear' if os.name!='nt' else 'cls')	
	
	# mostra o labirinto
	#print(maze_obj.to_str())	
	current = (0,0)
	# em (0,0) pergunta para o labirinto acoes possiveis
	info = maze_obj.move(current)
	current = info[1]
	options = info[2]
		
	move = 0


	# sai qdo atinge o max de passos ou chega no objetivo
	temp = 1000
	fator_diminuicao = 2
	while not (move > limit) and not maze_obj.is_done():
		action = gbc063.tempera(current, options,temp)
		if(action ==1):
			break 
		temp-= fator_diminuicao
		info = maze_obj.move(action)
		current = info[1]
		options = info[2]
		move += 1

	# saindo
	if (move < limit):
		print('O objetivo foi atingido com ',move,' movimentos')
		print('Solucao (',len(maze_obj.path),' passos)')
		print(maze_obj.path)
		distanciaTotal = len(maze_obj.path)
		distancia_ao_final = gbc063.distanciaManhattan(maze_obj.player,(9,9))
		cMaze = make_concluded_maze(move, distanciaTotal, distancia_ao_final)
		return cMaze
	else:
		print('O objetivo nao foi atingido em ',move,' movimentos.')
		distanciaTotal = len(maze_obj.path)
		distancia_ao_final = gbc063.distanciaManhattan(maze_obj.player,(9,9))
		cMaze = make_concluded_maze(move, distanciaTotal, distancia_ao_final)
		return cMaze
		


def main():

	clock = 0.1
	width = 10 	#20
	height = 10 	#12
	limite = 999
	is_block = True
	is_color = True
	block_symbol = u'\u2588'#unicode FullBlock
	block_symbols = {
		'start' : u'O',
		'end' : u'X',
		'wall_v' : block_symbol, 
		'wall_h' : block_symbol,
		'wall_c' : block_symbol,
		'visited' : block_symbol,
	}
	color_symbols = {
		'empty_color' : COLOR_DEFAULT,
		'visited_color' : COLOR_WHITE,   # incluido
		'wall_color' : COLOR_BLUE,
		'head_color' : COLOR_RED,
		'tail_color' : COLOR_CYAN,
		'start_bg_color' : COLOR_BG_YELLOW,
		'end_bg_color' : COLOR_BG_YELLOW,
		# if color, full block for player too
		'head' : block_symbol,
		'tail' : block_symbol,
		'visited' : block_symbol,   # incluido
	}
	#default symbols (not unicode or ANSI coloring)
	symbols = {
		# default symbols
		'start' : 'S',
		'end' : 'X',
		'wall_v'  : '|',
		'wall_h' : '-',
		'wall_c' : '+',
		'head' :  '#',
		'tail' : 'o',	
		'empty' : ' ',
		'visited' : 'v',
	}

	# se quiser desenho em blocos - necessario monospaced font
	# se  nao, comente com #
	symbols.update(block_symbols)
	symbols.update(color_symbols)
				
	# cria o labirinto
	

	# usa seu algoritmo (gbc063) para sair do labirinto
	
	""" rodar o labirinto 100 vezes
		colocar o resultado de cada labirinto em uma classe com a quantidade de passos e movimentos resultantes
		gerar um boxplot de labirintos x quantidade de passos e labirinto x movivmentos
		algo do tipo plt.boxplot(labiritos, movimentos) 
	 """
	

	with open('labirinto_1.csv', 'w', newline='') as csvfile:
		fieldnames = ['movimentos', 'caminho_total', 'distancia_ao_final']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for x in range(0,100):
			seed = random.random()*10000		
			maze_obj = maze.Maze(width, height, seed)
			cMaze = play_maze(maze_obj,limite,clock)
			writer.writerow({'movimentos': cMaze.total_moves, 'caminho_total': cMaze.steps, 'distancia_ao_final': cMaze.distancia_ao_final})
	return
	
	
			

# main
if __name__ == '__main__':
	main() 
