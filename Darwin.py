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

	def add_creature(self, species, direction, r, c):
		assert (r >= 0 and c >= 0)
		assert (r <= self.rows and c <= self.columns)
		self.grid[r][c] = Creature(species, direction, r, c)
		return True


class Species:
	def __init__(self, name, program=[]):
		self.name = name
		self.program = program


class Creature:
	def __init__(self, species, direction, r, c, program_count=0):
		self.species = species
		self.direction = direction
		self.program_count = program_count
		self.checked = False
		self.r = r
		self.c = c
