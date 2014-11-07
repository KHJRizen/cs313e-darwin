from Darwin2 import Species, Creature, Darwin
import random
from random import randrange, seed

def main():

    # ------
    # hopper
    # ------

    hopper = Species()
    hopper.add_instruction("hop")
    hopper.add_instruction("go 0")

    # ----
    # food
    # ---- 
   
    food = Species()
    food.add_instruction("left")
    food.add_instruction("go 0")
        
    # -----
    # rover
    # -----
    
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

    # ----
    # trap
    # ----
    
    trap = Species()
    trap.add_instruction("if_enemy 3")
    trap.add_instruction("left")
    trap.add_instruction("go 0")
    trap.add_instruction("infect")
    trap.add_instruction("go 0")
      

    # ----
    # best
    # ----

    best = Species()
    best.add_instruction("if_enemy 6")
    best.add_instruction("if_empty 4")
    best.add_instruction("left")
    best.add_instruction("go 0")
    best.add_instruction("hop")
    best.add_instruction("go 0")
    best.add_instruction("infect")
    best.add_instruction("go 0")
    
    
    # ----
    # darwin8x8()
    # ----
    
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
        #printed which turn it is
        print("Turn = " + str(i))
        grid.print_grid()
        grid.cycle()
        print()
    
    
    # ----
    # darwin7x9
    # ----
    
    print("*** Darwin 7x9 ***")
    grid = Darwin(7, 9)
    seed(0);
    
    t1 = Creature(trap, "t", 2, 0, 0)
    h1 = Creature(hopper, "h",1, 3, 2)
    r1 = Creature(rover, "r", 0 ,5, 4)
    t2 = Creature(trap, "t", 3 ,6, 8)
    
    grid.add_creature(t1)
    grid.add_creature(t2)
    grid.add_creature(h1)
    grid.add_creature(r1)
    
    for i in range(6):
        print("Turn = " + str(i))
        grid.print_grid()
        grid.cycle()
        print()
        
    # ----
    # darwin 72x72
    # without best
    # ----
    
    print("*** Darwin 72x72 without Best ***")
    seed(0);
    
    grid = Darwin(72, 72)
     
    f1 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f2 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f3 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f4 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f5 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f6 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f7 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f8 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f9 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f10 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    h1 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h2 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h3 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h4 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h5 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h6 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h7 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h8 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h9 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h10 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    r1 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r2 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r3 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r4 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r5 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r6 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r7 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r8 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r9 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r10 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    t1 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t2 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t3 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t4 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t5 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t6 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t7 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t8 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t9 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t10 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    grid.add_creature(f1)
    grid.add_creature(f2)
    grid.add_creature(f3)
    grid.add_creature(f4)
    grid.add_creature(f5)
    grid.add_creature(f6)
    grid.add_creature(f7)
    grid.add_creature(f8)
    grid.add_creature(f9)
    grid.add_creature(f10)
    grid.add_creature(h1)
    grid.add_creature(h2)
    grid.add_creature(h3)
    grid.add_creature(h4)
    grid.add_creature(h5)
    grid.add_creature(h6)
    grid.add_creature(h7)
    grid.add_creature(h8)
    grid.add_creature(h9)
    grid.add_creature(h10)
    grid.add_creature(r1)
    grid.add_creature(r2)
    grid.add_creature(r3)
    grid.add_creature(r4)
    grid.add_creature(r5)
    grid.add_creature(r6)
    grid.add_creature(r7)
    grid.add_creature(r8)
    grid.add_creature(r9)
    grid.add_creature(r10)
    grid.add_creature(t1)
    grid.add_creature(t2)
    grid.add_creature(t3)
    grid.add_creature(t4)
    grid.add_creature(t5)
    grid.add_creature(t6)
    grid.add_creature(t7)
    grid.add_creature(t8)
    grid.add_creature(t9)
    grid.add_creature(t10)
        
    for i in range(1001):
        print("Turn = " + str(i))
        print(t1.direction)
        grid.cycle()
        print()
    grid.print_grid()
    
    
    # ----
    # darwin 72x72
    # with best
    # ----
    
    print("*** Darwin 72x72 with Best ***")
    seed(0);
    
    grid = Darwin(72, 72)
     
    f1 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f2 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f3 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f4 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f5 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f6 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f7 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f8 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f9 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    f10 = Creature(food, "f", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    h1 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h2 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h3 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h4 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h5 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h6 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h7 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h8 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h9 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    h10 = Creature(hopper, "h", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    r1 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r2 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r3 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r4 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r5 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r6 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r7 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r8 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r9 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    r10 = Creature(rover, "r", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    t1 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t2 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t3 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t4 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t5 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t6 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t7 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t8 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t9 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    t10 = Creature(trap, "t", random.randrange(0, 4), random.randrange(0, 72), random.randrange(0, 72))
    
    grid.add_creature(f1)
    grid.add_creature(f2)
    grid.add_creature(f3)
    grid.add_creature(f4)
    grid.add_creature(f5)
    grid.add_creature(f6)
    grid.add_creature(f7)
    grid.add_creature(f8)
    grid.add_creature(f9)
    grid.add_creature(f10)
    grid.add_creature(h1)
    grid.add_creature(h2)
    grid.add_creature(h3)
    grid.add_creature(h4)
    grid.add_creature(h5)
    grid.add_creature(h6)
    grid.add_creature(h7)
    grid.add_creature(h8)
    grid.add_creature(h9)
    grid.add_creature(h10)
    grid.add_creature(r1)
    grid.add_creature(r2)
    grid.add_creature(r3)
    grid.add_creature(r4)
    grid.add_creature(r5)
    grid.add_creature(r6)
    grid.add_creature(r7)
    grid.add_creature(r8)
    grid.add_creature(r9)
    grid.add_creature(r10)
    grid.add_creature(t1)
    grid.add_creature(t2)
    grid.add_creature(t3)
    grid.add_creature(t4)
    grid.add_creature(t5)
    grid.add_creature(t6)
    grid.add_creature(t7)
    grid.add_creature(t8)
    grid.add_creature(t9)
    grid.add_creature(t10)
        
    for i in range(1001):
        print("Turn = " + str(i))
        print(t1.direction)
        grid.cycle()
        print()
    grid.print_grid()
    
   
        
    
main()

#notes

#split of command operations
#species - program list