from Darwin import Darwin, Species, Creature

import random

hopper = Species("Hopper")
hopper.add_instruction("hop")
print(hopper.program)

x = Darwin(5,5)
print(x.grid)

y = x.add_creature(hopper, 0, 1, 0)
print(x.grid)