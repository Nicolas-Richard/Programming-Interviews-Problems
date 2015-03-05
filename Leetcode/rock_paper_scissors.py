
class Player():
	def __init__(self, name):
		self.name = name
		self.move = ''

	def pick(self):
		print self.name + ': type rock, paper or scissors then hit enter'
		self.move = ''
		self.move = raw_input()
		while self.move not in ['rock', 'paper', 'scissors']:
			print 'not a legal move'
			print self.name + ': type rock, paper or scissors then hit enter'
			self.move = raw_input()

		return self.move


def fight(player1, player2):
	if player1.move == player2.move:
		return "it's a draw"
	
	elif player1.move == "rock":
		if player2.move == "paper":
			return player2.name + " won"
		else:
			return player1.name + " won"

	elif player1.move == "paper":
		if player2.move == "scissors":
			return player2.name + " won"
		else:
			return player1.name + " won"

	elif player1.move == "scissors":
		if player2.move == "rock":
			return player2.name + " won"
		else:
			return player1.name + " won"			


if __name__ == "__main__":

	Players = []
	draw = True

	for i in [1, 2]:
		print 'Player %d pick a name' %(i)
		Players.append(Player(raw_input()))

	while draw == True:

		for player in Players:
			player.pick()

		if fight(Players[0], Players[1]) == "it's a draw":
			print fight(Players[0], Players[1])
			print "Let's play again \n"
		else:
			draw = False	
			print fight(Players[0], Players[1])






