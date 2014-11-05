from random import randint, sample, seed


class Darwin:
	def __init__(self, width, height):
		self.rows = height
		self.columns = width
		self.direction = [0, 1, 2, 3]
		self.grid = []
		assert self.rows > 0 and self.columns > 0
		for r in range(self.rows):
			self.grid.append([])
			for c in range(self.columns):
				self.grid[r].append(0)
				
	def cycle(self):
		for r in range(self.rows):
			for c in range(self.columns):
				if (self.grid[r][c] != 0 and not self.grid[r][c].checked):
					temp = self.take_action(r,c)
					while not temp:
						temp = self.take_action(r,c)
						
		# reset all of creatures for next cycle
		for r in range(self.rows):
			for c in range(self.columns):
				if self.grid[r][c] != 0:
					self.grid[r][c].checked = False
						
	def take_action(self, r, c):
		if self.grid[r][c].species.program[self.grid[r][c].program_count]== "hop":
			self.hop(r, c)
			#self.hop(r,c)
			return True
		if program[program_count] == "left":
			self.grid[r][c].left()
			self.grid[r][c].program_count += 1
			self.grid[r][c].checked = True
			return True
		if program[program_count] == "right":
			self.grid[r][c].right()
			self.grid[r][c].program_count += 1
			self.grid[r][c].checked = True
			return True
		if program[program_count] == "infect":
			self.grid[r][c].infect(r, c)
			#same as hop
			return True			
			
	def add_creature(self, species, direction, r, c):
		assert (r >= 0 and c >= 0)
		assert (r <= self.rows and c <= self.columns)
		self.grid[r][c] = Creature(species, direction, r, c)
		return True
					
					
	def facing_wall(self, r, c):
		nr = self.grid[r][c].next_row()
		nc = self.grid[r][c].next_column()
		return nr >= self.rows or nr < 0 or nc >= self.columns or nc < 0


	def facing_empty(self, r, c):
		nr = self.grid[r][c].next_row()
		nc = self.grid[r][c].next_column()
		return not self.facing_wall(r, c) and self.grid[nr][nc] == 0

		
	def facing_enemy(self):
		self.direction = self.grid[r][c]
		nr = next_row()
		nc = next_column()
		return not facing_wall and not facing_empty and self.grid[r][c].species != self.grid[nr][nc].species
	
	def hop(self):
		nr = next_row()
		nc = next_column()
		if facing_empty():
			self.grid[nr][nc] = grid[r][c]
			self.grid[r][c] = 0
			self.grid[nr][nc].program_count += 1
			self.grid[nr][nc].checked = True
		else:
			self.grid[r][c].program_count += 1
			self.grid[r][c].checked = True
	
	def print_grid(self):
		print()
		print(" ", end = "")
		for i in range(self.columns):
			print(i % 10, end="")
		print()
		for i in range(self.rows):
			print(i % 10, end="")
			for j in range(self.columns):
				if self.grid[i][j] == 0:
					print(".", end="")
				else:
					print(self.grid[i][j].species.name, end = "")
			print()

class Species:
	def __init__(self, name, program=[]):
		self.name = name
		self.program = program
		
	def add_instruction(self, instruction):
		self.program.append(instruction)

class Creature:
	def __init__(self, species, direction, r, c, program_count=0):
		self.species = species
		self.direction = direction
		self.program_count = program_count
		self.checked = False
		self.r = r
		self.c = c
		
	# gets row of one space in front of where creature is facing, given direction
	def next_row(self):
		if self.direction == 0 or self.direction == 2:
			return self.r
		if self.direction == 1:
			return self.r + 1
		else:
			return self.r - 1

	# gets column of one space in front of where creature is facing, given direction
	def next_column(self):
		if self.direction == 1 or self.direction == 3:
			return self.c
		if self.direction == 0:
			return self.c + 1
		else:
			return self.c - 1

	def right(self):
		if self.direction == 0:
			self.direction = 1
		elif self.direction == 1:
			self.direction = 2
		elif self.direction == 2:
			self.direction = 3
		elif self.direction == 3:
			self.direction = 0
			
	def left(self):
		if self.direction == 0:
			self.direction = 3
		elif self.direction == 1:
			self.direction = 0
		elif self.direction == 2:
			self.direction = 1
		elif self.direction == 3:
			self.direction = 2
