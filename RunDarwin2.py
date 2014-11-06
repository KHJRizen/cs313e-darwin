from Darwin2 import Species, Creature, Darwin

import random

hopper = Species()
hopper.add_instruction("hop")
hopper.add_instruction("goto 0")

#N E S W
#0 1 2 3

h1 = Creature(hopper, "h", 0, 0, 0)
h2 = Creature(hopper, "h", 1, 1, 1)

x = Darwin(5, 5)

x.add_creature(h1)
x.add_creature(h2)

print(x.grid)

x.print_grid()

#notes

#split of command operations
#species - program list