import getch,os,sys
class RiverCrossing():
	def __init__(self):

		self.on_river_left = ["F","G","C","H"]
		self.on_river_right = [" "," "," "," "]

		self.left_side_safe = False
		self.right_side_safe = False

		self.unsafe_pairs = [["F","G"],["G","C"]]

		self.allowed_moves = ["F","G","C","H"]

		self.clear = ""
		if sys.platform == "linux":
			self.clear = "clear"
		elif sys.platform == "win32":
			self.clear = "cls"

	def start_screen(self):
		os.system(self.clear)
		print('''
  ##########################################
  #             CROSS THE RIVER            #
  ##########################################
  
  # OBJECTIVE
  human wants to cross the river with his fox,goat and corn,
  he has only got one boat which can carry two things at a time
  and only human can navigate the boat. Objective of the game is
  to carry human belongings to the right side of river.

  goat is unsafe if left alone with fox,
  corn is unsafe if left alone with goat,
  everything is safe on the side where human is present

  F -> FOX
  G -> GOAT
  C -> CORN
  H -> HUMAN

  press any key to start....
			''')
		x = getch.getch()

	def display(self):
		print(f'''
	[{self.on_river_left[0]}]  |- _|  [{self.on_river_right[0]}]
	[{self.on_river_left[1]}]  | _-|  [{self.on_river_right[1]}]
	[{self.on_river_left[2]}]  |-_ |  [{self.on_river_right[2]}]
	[{self.on_river_left[3]}]  |  -|  [{self.on_river_right[3]}]
''')

	def safety_check(self):
		self.left_side_safe = True
		self.right_side_safe = True

		if "H" in self.on_river_left:
			for i in self.unsafe_pairs:
				if i[0] in self.on_river_right and i[1] in self.on_river_right:
					self.right_side_safe = False
					break

		elif "H" in self.on_river_right:
			for i in self.unsafe_pairs:
				if i[0] in self.on_river_left and i[1] in self.on_river_left:
					self.left_side_safe = False
					break

	def player_move(self):
		self.on_river_left_revert = self.on_river_left.copy()
		self.on_river_right_revert = self.on_river_right.copy()
		while True:
			pass
			print(f"  Allowed Moves :: {self.allowed_moves}\n\n  Enter Your Move Here :: ")
			move = getch.getch().upper()
			if move in self.allowed_moves:
				if move == "H":
					if "H" in self.on_river_left:
						self.on_river_left[3] = " "
						self.on_river_right[3] = "H"
						break
					else:
						self.on_river_right[3] = " "
						self.on_river_left[3] = "H"
						break
				else:
					if move in self.on_river_left and "H" in self.on_river_left:
						index = self.on_river_left.index(move)
						self.on_river_left[3] = " "
						self.on_river_left[index] = " "
						
						self.on_river_right[3] = "H"
						self.on_river_right[index] = move

						break
						
					elif move in self.on_river_right and "H" in self.on_river_right:
						index = self.on_river_right.index(move)
						self.on_river_right[3] = " "
						self.on_river_right[index] = " "
						
						self.on_river_left[3] = "H"
						self.on_river_left[index] = move

						break

					else:
						print("Character and Human not on same side")
			else:
				print("Incorrect Move")
		self.safety_check()
		if (self.left_side_safe and self.right_side_safe) == False:
			self.on_river_right = self.on_river_right_revert
			self.on_river_left = self.on_river_left_revert
			print("\n  One or more character can be harmed")
			print("  press any key to continue.....")
			x = getch.getch()

	def check_win(self):
		if self.on_river_right == self.allowed_moves:
			os.system(self.clear)
			self.display()
			print("  $$ BOOYAH!!!!! YOU WON $$")
			return True

	def init_v1(self):
		self.start_screen()
		while True:
			os.system(self.clear)
			self.display()
			self.player_move()
			if self.check_win():
				break
				
game = RiverCrossing()

game.init_v1()
