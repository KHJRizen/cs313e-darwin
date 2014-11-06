from random import randint, sample, seed

class Species:
    def __init__(self, program=[]):
        #self.name = name
        self.program = program

    # to add to the program
    def add_instruction(self, instruction):
        self.program.append(instruction)

    # used when infecting to make sure classes are different
    def different_species(self, creature):
        #return self.name != creature.species()#species.name?
        
        #creature should be species class
        return self.program != creature.program
        
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
        if self.direction == 1 or self.direction == 3:
            return self.r
        if self.direction == 2:
            return self.r + 1
        else:
            return self.r - 1

    # gets column of one space in front of where creature is facing, given direction
    def next_column(self):
        if self.direction == 0 or self.direction == 2:
            return self.c
        if self.direction == 1:
            return self.c + 1
        else:
            return self.c - 1

    def left(self):
        if self.direction == 0:
            self.direction = 3
        elif self.direction == 1:
            self.direction = 0
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 2

    def right(self):
        if self.direction == 0:
            self.direction = 1
        elif self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 3
        elif self.direction == 3:
            self.direction = 0
            
class Darwin:
    def __init__(self, width, height):
        self.rows = height
        self.columns = width
        #N E S W
        self.direction = [0, 1, 2, 3]
        self.grid = []
        
        #no empty grids
        assert self.rows > 0 and self.columns > 0
        
        #create the grid
        for r in range(self.rows):
            self.grid.append([])
            for c in range(self.columns):
                self.grid[r].append(0)

    def add_creature(self, creature):
    
        #assert (r <= self.rows and c <= self.columns)
        #assert (r >= 0 and c >= 0)
        
        #add creature at desired position
        #creature instantiated in RUnDarwin
        self.grid[creature.r][creature.c] = creature
        return True

    def cycle(self):
        #traverse through every spot on the grid
        for r in range(self.rows):
            for c in range(self.columns):
            
                #if we detect a creature in this spot
                if (self.grid[r][c] != 0 and self.grid[r][c].checked is False):
                    temp = self.take_action(r,c)
                    
                    #while action is not taken, keep running through instructions
                    while temp is False:
                        temp = self.take_action(r,c)
                        
                    
                    #print(self.facing_wall(r, c))
                    #print(self.facing_empty(r, c))
                    
                    #temp = self.grid[r][c].next()
                    #while (temp != 0 and not take_action()):
                    #    temp = grid[r][c].next()
        # resets checked variable for all creatures
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] != 0:
                    self.grid[r][c].checked = False
      
    def take_action(self, r, c):
        if self.grid[r][c].species.program[self.grid[r][c].program_count]== "hop":
            self.grid[r][c].hop(r, c)
            return True
        if self.grid[r][c].species.program[self.grid[r][c].program_count] == "left":
            self.grid[r][c].left()
            self.grid[r][c].program_count += 1
            self.grid[r][c].checked = True
            return True
        if self.grid[r][c].species.program[self.grid[r][c].program_count] == "right":
            self.grid[r][c].right()
            self.grid[r][c].program_count += 1
            self.grid[r][c].checked = True
            return True
        if self.grid[r][c].species.program[self.grid[r][c].program_count] == "infect":
            self.grid[r][c].infect(r, c)
            #same as hop
            return True

            
        jump_num = 0
        instruction = self.grid[r][c].species.program[self.grid[r][c].program_count]
        #split to get last digit; make sure to convert it to integer for use else where
        # how to get jump_num. it's the last digits of the program at index program count
        instruction_split = instruction.split()
        if len(instruction_split)==2:
            jump_num = int(instruction_split[-1])
        
        if "if_empty" in instruction:
            if facing_empty(r, c):
                self.grid[r][c].program_count = jump_num
            else:
                self.grid[r][c].program_count += 1
            return False

        if "if_wall" in instruction:
            if facing_wall(r, c):
                self.grid[r][c].program_count = jump_num
            else:
                self.grid[r][c].program_count += 1
            return False

        if "if_random" in instruction:
            if random.randint % 2:
                self.grid[r][c].program_count = jump_num
            else:
                self.grid[r][c].program_count += 1
            return False

        if "if_enemy" in instruction:
            if facing_enemy(r, c):
                self.grid[r][c].program_count = jump_num
            else:
                self.grid[r][c].program_count += 1
            return False

        if "go" in instruction:
            grid[r][c].program_count = jump_num
            return False
            
        #return True if nothing happened
        return True
        
    # do all the direction checks within the iteration
    def facing_empty(self, r, c):
        nr = self.grid[r][c].next_row()
        nc = self.grid[r][c].next_column()
        
        # if false from facing_wall, and no species in space, then facing_empty
        return not self.facing_wall(r, c) and self.grid[nr][nc] == 0
        
    # tells if creature at spot (row,column) is facing a wall
    def facing_wall(self, r, c):
        nr = self.grid[r][c].next_row()
        nc = self.grid[r][c].next_column()
        
        #if out of bounds, return True, facing wall
        return nr >= self.rows or nr < 0 or nc >= self.columns or nc < 0
        
    def facing_enemy(self, r, c):
        #self.direction = self.grid[r][c]
        nr = self.grid[r][c].next_row()
        nc = self.grid[r][c].next_column()
        
        # TRUE > not facing wall, not empty, not facing enemy, and make sure species in front is not same species 
        return not facing_wall and not facing_empty and self.grid[r][c].species != self.grid[nr][nc].species
    
    def hop(self, r , c):
        nr = self.grid[r][c].next_row()
        print(nr)
        nc = self.grid[r][c].next_column()
        print(nc)
                
        if facing_empty(r, c) is True:
            grid[nr][nc] = grid[r][c]
            grid[r][c] = 0
            grid[nr][nc].program_count += 1
            grid[nr][nc].checked = True
        else:
            grid[r][c].program_count += 1
            grid[r][c].checked = True
            
    # tries to infect space in front of creature. if failure, wastes turn
    def infect(self, r,c):
        #self.direction = self.grid[r][c]
        nr = self.grid[r][c].next_row()
        nc = self.grid[r][c].next_column()
        if facing_enemy(r, c) is True:
            self.grid[nr][nc].species = self.grid[r][c].species
            self.grid[nr][nc].program_count = 0
        self.grid[r][c].program_count += 1
        self.grid[r][c].checked = True