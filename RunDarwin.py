from Darwin import Darwin, Species, Creature

import random

hopper = Species("Hopper")
hopper.add_instruction("if_empty 1")
hopper.add_instruction("hop")
hopper.add_instruction("hop")
print(hopper.program)

x = Darwin(5,5)
print(x.grid)

y = x.add_creature(hopper, 0, 1, 0)
y = x.add_creature(hopper, 0, 2, 0)
print(x.grid)

x.print_grid()

for i in range(3):
	x.cycle()
	x.print_grid()
