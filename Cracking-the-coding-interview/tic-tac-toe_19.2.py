'''
Cracking the coding interview problem 19.2 in Python
Design an algorithm to figure out if someone has won in a game of tic-tac-toe
'''

from random import randint
from random import choice

def tic(game):
	'''checks if someone has won the game'''
	
	# check the lines
	for line in game: 
		if line[0] == line[1] and line[1] == line[2]:
			return line[0]

	
	# check the diagonals
	if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
		return game[0][0]	
	if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
		return game[0][2]	
	
	# check the columns
	for i in range(3):
		if game[0][i] == game[1][i] and game[1][i] == game[2][i]:
			return game[0][i]

	return -1

def printgame(game):
	'''pretty print the game'''
	print '#'*25
	for line in game:
		print line[0], line[1], line[2]
	print '#'*25


def new_game():
	'''plays a tic-tac-toe game. Moves are picked randomly'''
	result = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
	seq = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
	plays = [1,0,1,0,1,0,1,0,1]

	while seq != []:
		position = choice(seq)
		seq.remove(position)
		result[position[0]][position[1]] = plays.pop()

	return result

# tests
# Runs severals games and measures the number of games that have been won.
counter_1 = 0
counter_0 = 0
counter_draw = 0
total = 100
for i in range(total):
	game = new_game()
	result = tic(game)
	if result == 1:
		counter_1 += 1
	elif result == 0:
		counter_0 += 1
	else:
		counter_draw += 1		

print 'player 1 won %f per cent of games' % (100.*counter_1/total) 
print 'player 0 won %f per cent of games' % (100.*counter_0/total)
print '%f per cent of games were draw' % (100.*counter_draw/total)
print 'Stats over %d games' % (total)
