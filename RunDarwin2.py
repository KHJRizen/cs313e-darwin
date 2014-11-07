from Darwin2 import Species, Creature, Darwin

import random

def main():

    hopper = Species()
    hopper.add_instruction("hop")
    hopper.add_instruction("go 0")
        
    food = Species()
    food.add_instruction("left")
    food.add_instruction("go 0")
        
    rover = Species()
    rover.add_instruction("if_enemy 9")
    rover.add_instruction("if_empty 7")
    rover.add_instruction("if_random 5")
    rover.add_instruction("left")
    rover.add_instruction("go 0")
    rover.add_instruction("right")
    rover.add_instruction("go 0")
    rover.add_instruction("hop")
    rover.add_instruction("go 0")
    rover.add_instruction("infect")
    rover.add_instruction("go 0")
        
    trap = Species()
    trap.add_instruction("if enemy 3")
    trap.add_instruction("left")
    trap.add_instruction("go 0")
    trap.add_instruction("infect")
    trap.add_instruction("go 0")
        
    best = Species()
    best.add_instruction("if_enemy 6")
    best.add_instruction("if_empty 4")
    best.add_instruction("left")
    best.add_instruction("go 0")
    best.add_instruction("hop")
    best.add_instruction("go 0")
    best.add_instruction("infect")
    best.add_instruction("go 0")
        
    #0123
    #3012
    
    #darwin8x8()
    print("*** Darwin 8x8 ***")
    grid = Darwin(8, 8)
      
    f1 = Creature(food, "f", 1, 0, 0)
    h1 = Creature(hopper, "h", 0, 3, 3)
    h2 = Creature(hopper, "h", 1, 3, 4)
    h3 = Creature(hopper, "h", 2, 4, 4)
    h4 = Creature(hopper, "h", 3, 4, 3)
    f2 = Creature(food, "f", 0, 7, 7)
        
    grid.add_creature(f1)
    grid.add_creature(f2)
    grid.add_creature(h1)
    grid.add_creature(h2)
    grid.add_creature(h3)
    grid.add_creature(h4)
    
    for i in range(6):
        print("Turn = " + str(i))
        grid.print_grid()
        grid.cycle()
        print()
    
    
    
    #darwin7x9
    print("*** Darwin 7x9 ***")
    grid = Darwin(7, 9)
    
    t1 = Creature(trap, "t", 3, 0, 0)
    h1 = Creature(hopper, "h",2, 3, 2)
    r1 = Creature(rover, "r", 1,5, 4)
    t2 = Creature(trap, "t", 0,6, 8)
    b1 = Creature(best, "b", 0, 1, 2)
    
    grid.add_creature(t1)
    grid.add_creature(t2)
    grid.add_creature(h1)
    grid.add_creature(r1)
    grid.add_creature(b1)
    
    for i in range(10):
        print("Turn = " + str(i))
        grid.print_grid()
        grid.cycle()
        print()
    
    
    
    
    
        
#N E S W
#0 1 2 3

main()

#notes

#split of command operations
#species - program list