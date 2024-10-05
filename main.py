import random

winner1 = {"draw" : "Draw!\n", "p1" : "You won!\n" ,"bot" : "You lost!\n"}
winner2 = {"draw" : "Draw!\n", "p1" : "Player 1 wins!\n" ,"bot" : "Player 2 wins!\n"}
controls = {'q' : 1, 'w' : 2, 'e' : 3,
			'a' : 4, 's' : 5, 'd' : 6,
			'z' : 7, 'x' : 8, 'c' : 9}
def intro():
	print("\nGreetings! ")
	print("Here's the coordinates of the board:")
	for item in controls:
		print(item, end=" ")
		if (controls[item] % 3 == 0):
			print("")
	print("Please use these to represent the position where you want to put 'X'")
	print("Now let the game begin!\n")


def display_board(board):
	for line in board:
		for char in line:
			if char == 'X' or char == 'O':
				print(f'{char}', end = '  ')
			else:
				print(f'_ ', end = ' ')
		print("")

def p1_turn(board, set):
	end_turn = False
	while (end_turn == False):
		try:
			pos = input("\nSelect position to put 'X': ")
			pos = controls[pos] - 1
			if pos in set:
				i = pos//3
				j = pos % 3
				board[i][j] = 'X'
				set.remove(pos)
				display_board(board)
				end_turn = True
			else:
				print("Move not possible, please try again\n")
		except:
			print("Move not possible, please try again\n")

def check_status(board, set):
	if len(set) == 0:
		return "draw"

	elif win_horizontals(board) != None:
		return win_horizontals(board)

	elif win_verticals(board) != None:
		return win_verticals(board)

	elif win_left_diagonal(board) != None:
		return win_left_diagonal(board)

	elif win_right_diagonal(board) != None:
		return win_right_diagonal(board)




def win_horizontals(board):
	i = 0
	while (i < 3):
		if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
			return "p1"
		elif board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
			return "bot"
		i+=1

def win_verticals(board):
	i = 0
	while (i < 3):
		if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
			return "p1"
		elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
			return "bot"
		i+=1

def win_left_diagonal(board):
	if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
		return "p1"
	elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
		return "bot"

def win_right_diagonal(board):
	if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
		return "p1"
	elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
		return "bot"

def check(board, set, sym, a, b, c): #if two adjacent O, puts another O to win.
						#if two adjacent X, puts a O to stop you from winning.
	if a == sym and b == sym:
		pos = c
	elif b == sym and c == sym:
		pos = a
	elif c == sym and a == sym:
		pos = b
	else:
		pos = None

	if pos in set:
		return pos
	else:
		return None

def bot_check(board, set):
	temp = check(board, set,'O',*board[0])
	if temp != None:
		return temp

	temp = check(board, set,'O',*board[1])
	if temp != None:
		return temp

	temp = check(board,set,'O',*board[2])
	if temp != None:
		return temp

	temp = check(board,set,'O',board[0][0], board[1][0], board[2][0])
	if temp != None:
		return temp

	temp = check(board, set, 'O', board[0][1], board[1][1], board[2][1])
	if temp != None:
		return temp

	temp = check(board, set, 'O', board[0][2], board[1][2], board[2][2])
	if temp != None:
		return temp

	temp = check(board, set, 'O', board[0][0], board[1][1], board[2][2])
	if temp != None:
		return temp

	temp = check(board, set, 'O', board[0][2], board[1][1], board[2][0])
	if temp != None:
		return temp

	#tries to win

	temp = check(board,set,'X',*board[0])
	if temp != None:
		return temp

	temp = check(board,set,'X',*board[1])
	if temp != None:
		return temp

	temp = check(board,set,'X',*board[2])
	if temp != None:
		return temp

	temp = check(board,set,'X',board[0][0], board[1][0], board[2][0])
	if temp != None:
		return temp

	temp = check(board, set, 'X', board[0][1], board[1][1], board[2][1])
	if temp != None:
		return temp

	temp = check(board, set, 'X', board[0][2], board[1][2], board[2][2])
	if temp != None:
		return temp

	temp = check(board, set, 'X', board[0][0], board[1][1], board[2][2])
	if temp != None:
		return temp

	temp = check(board, set, 'X', board[0][2], board[1][1], board[2][0])
	if temp != None:
		return temp
	# stops you from winning

	pos = int(random.choice(list(set)))
	return pos

def game_mode():
	end = False
	while (end == False):
		print("1 - Easy Mode")
		print("2 - Standard Mode")
		print("3 - PVP Mode")
		print("4 - Exit")
		try:
			mode = int(input("Select Game Mode Using Numbers: "))
			if mode == 1:
				easy_game()
			elif mode == 2:
				hard_game()
			elif mode == 3:
				pvp_game()
			elif mode == 4:
				return
			else:
				print("Please try again\n")

			if mode == 1 or mode == 2 or mode == 3:
				input("Press 'Enter' to Continue: ")

		except:
			print("Please try again")



def bot_turn(board, pos, set):
	pos = int(float(pos))
	i = pos // 3
	j = pos % 3
	board[i][j] = 'O'
	set.remove(pos)


def hard_game():
	board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
	set = {0,1,2,3,4,5,6,7,8}

	while(True):
		p1_turn(board,set)

		temp = check_status(board,set)
		if temp != None:
			print(winner1[temp])
			return

		print("bot:\n")

		temp = bot_check(board,set)
		bot_turn(board,temp,set)
		display_board(board)

		temp = check_status(board, set)
		if temp != None:
			print(winner1[temp])
			return

def easy_bot(board, set):
	pos = int(random.choice(list(set)))
	pos = int(float(pos))
	i = pos // 3
	j = pos % 3
	board[i][j] = 'O'
	set.remove(pos)


def easy_game():
	board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
	set = {0, 1, 2, 3, 4, 5, 6, 7, 8}

	while(True):
		p1_turn(board,set)

		temp = check_status(board,set)
		if temp != None:
			print(winner1[temp])
			return
		print("bot:\n")

		easy_bot(board, set)
		display_board(board)

		temp = check_status(board, set)
		if temp != None:
			print(winner1[temp])
			return


def p2_turn(board, set):
	end_turn = False
	while (end_turn == False):
		try:
			pos = input("Select position to put 'O': ")
			pos = controls[pos] - 1
			if pos in set:
				i = pos//3
				j = pos % 3
				board[i][j] = 'O'
				set.remove(pos)
				display_board(board)
				end_turn = True
			else:
				print("Move not possible, please try again\n")
		except:
			print("Move not possible, please try again\n")


def pvp_game():
	board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
	set = {0, 1, 2, 3, 4, 5, 6, 7, 8}


	while(True):
		print("\nPlayer 1:")
		p1_turn(board,set)

		temp = check_status(board,set)
		if temp != None:
			print(winner2[temp])
			return

		print("\nPlayer 2:")
		p2_turn(board, set)

		temp = check_status(board, set)
		if temp != None:
			print(winner2[temp])
			return

intro()
game_mode()