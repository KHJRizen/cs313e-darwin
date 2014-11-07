#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Darwin import Species, Creature, Darwin

# -----------
# TestCollatz
# -----------

class TestDarwin (TestCase) :
    # ----
    # read
    # ----


    def test_species_add_instruction1(self):
        x = Species()
        y = "hop"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["hop"] )
    def test_species_add_instruction2(self):
        x = Species()
        y = "yo"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["yo"] )
    def test_species_add_instruction3(self):
        x = Species()
        y = "hop"
        x.add_instruction(y)
        x.add_instruction("YUH")
        z = x.program
        self.assertEqual(z, ["hop", "YUH"] )
    def test_species_add_instruction4(self):
        x = Species()
        y = "hop"
        x.add_instruction(y)
        x.add_instruction("YUH sup")
        z = x.program
        self.assertEqual(z, ["hop", "YUH sup"] )
    def test_species_add_instruction5(self):
        x = Species()
        y = "bo"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["bo"] )
    def test_species_add_instruction6(self):
        x = Species()
        y = "123"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["123"] )
    def test_species_add_instruction7(self):
        x = Species()
        y = "bo343"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["bo343"] )
    def test_species_add_instruction8(self):
        x = Species()
        y = "12356"
        x.add_instruction(y)
        z = x.program
        self.assertEqual(z, ["12356"] )


    def test_creature_next_row1(self):
        y = Species()
        x = Creature(y, "Bob", 0, 0, 0)
        z = x.next_row()
        self.assertEqual(z, -1)
    def test_creature_next_row2(self):
        y = Species()
        x = Creature(y, "Bob", 1, 0, 0)
        z = x.next_row()
        self.assertEqual(z, 0)
    def test_creature_next_row3(self):
        y = Species()
        x = Creature(y, "Bob", 2, 0, 0)
        z = x.next_row()
        self.assertEqual(z, 1)
    def test_creature_next_row4(self):
        y = Species()
        x = Creature(y, "Bob", 3, 0, 0)
        z = x.next_row()
        self.assertEqual(z, 0)
    def test_creature_next_row5(self):
        y = Species()
        x = Creature(y, "Bob", 0, 1, 0)
        z = x.next_row()
        self.assertEqual(z, 0)

    def test_creature_next_column1(self):
        y = Species()
        x = Creature(y, "Bob", 0, 0, 0)
        z = x.next_column()
        self.assertEqual(z, 0)
    def test_creature_next_column2(self):
        y = Species()
        x = Creature(y, "Bob", 1, 0, 0)
        z = x.next_column()
        self.assertEqual(z, 1)
    def test_creature_next_column3(self):
        y = Species()
        x = Creature(y, "Bob", 2, 0, 0)
        z = x.next_column()
        self.assertEqual(z, 0)
    def test_creature_next_column4(self):
        y = Species()
        x = Creature(y, "Bob", 3, 0, 0)
        z = x.next_column()
        self.assertEqual(z, -1)
    def test_creature_next_column5(self):
        y = Species()
        x = Creature(y, "Bob", 0, 1, 0)
        z = x.next_column()
        self.assertEqual(z, 0)


    def test_creature_left1(self):
        y = Species()
        x = Creature(y, "Bob", 0, 0, 0)
        z = x.left()
        a = x.direction
        self.assertEqual(a, 3)
    def test_creature_left2(self):
        y = Species()
        x = Creature(y, "Bob", 1, 0, 0)
        z = x.left()
        a = x.direction
        self.assertEqual(a, 0)
    def test_creature_left3(self):
        y = Species()
        x = Creature(y, "Bob", 2, 0, 0)
        z = x.left()
        a = x.direction
        self.assertEqual(a, 1)
    def test_creature_left4(self):
        y = Species()
        x = Creature(y, "Bob", 3, 0, 0)
        z = x.left()
        a = x.direction
        self.assertEqual(a, 2)


    def test_creature_right1(self):
        y = Species()
        x = Creature(y, "Bob", 0, 0, 0)
        z = x.right()
        a = x.direction
        self.assertEqual(a, 1)
    def test_creature_right2(self):
        y = Species()
        x = Creature(y, "Bob", 1, 0, 0)
        z = x.right()
        a = x.direction
        self.assertEqual(a, 2)
    def test_creature_right3(self):
        y = Species()
        x = Creature(y, "Bob", 2, 0, 0)
        z = x.right()
        a = x.direction
        self.assertEqual(a, 3)
    def test_creature_right4(self):
        y = Species()
        x = Creature(y, "Bob", 3, 0, 0)
        z = x.right()
        a = x.direction
        self.assertEqual(a, 0)

    def test_darwin_add_creature1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 0, 0)
        a = x.add_creature(z)
        self.assertEqual(a, True)

    def test_darwin_add_creature2(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 1, 1)
        a = x.add_creature(z)
        self.assertEqual(a, True)

    def test_darwin_add_creature3(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 1, 0)
        a = x.add_creature(z)
        self.assertEqual(a, True)

    def test_darwin_hop1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 0, 0)
        x.add_creature(z)
        y.add_instruction("hop")
        x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 0)

    def test_darwin_infect1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 0)

    def test_darwin_cycle1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 0)

    def test_darwin_take_action(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        y.add_instruction("hop")
        y.add_instruction("left")
        y.add_instruction("right")
        y.add_instruction("if_empty 5")
        y.add_instruction("if_wall 6")
        y.add_instruction("if_enemy 7")
        y.add_instruction("if_random 0")
        y.add_instruction("go 0")
        
        for i in range(50):
            x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 1)  

    def test_darwin_take_action2(self):
        x = Darwin(5, 5)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        y.add_instruction("hop")
        y.add_instruction("left")
        y.add_instruction("right")
        y.add_instruction("if_empty 5")
        y.add_instruction("if_wall 6")
        y.add_instruction("if_enemy 7")
        y.add_instruction("if_random 0")
        y.add_instruction("go 0")
        
        for i in range(50):
            x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 4)  

    def test_darwin_take_action3(self):
        x = Darwin(3, 10)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        y.add_instruction("hop")
        y.add_instruction("left")
        y.add_instruction("right")
        y.add_instruction("if_empty 5")
        y.add_instruction("if_wall 6")
        y.add_instruction("if_enemy 7")
        y.add_instruction("if_random 0")
        y.add_instruction("go 0")
        
        for i in range(50):
            x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 2) 

    def test_darwin_take_action4(self):
        x = Darwin(5, 10)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        t = Species()
        r = Creature(t, "Joe", 2, 1, 0)
        x.add_creature(z)
        y.add_instruction("infect")
        y.add_instruction("hop")
        y.add_instruction("left")
        y.add_instruction("right")
        y.add_instruction("if_empty 5")
        y.add_instruction("if_wall 6")
        y.add_instruction("if_enemy 7")
        y.add_instruction("if_random 0")
        y.add_instruction("go 0")
        
        for i in range(50):
            x.cycle()
        a = z.c
        b = z.r
        self.assertEqual(a, 0)
        self.assertEqual(b, 4) 

    def test_facing_empty1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        x.add_creature(z)
        a = x.facing_empty(0, 0)    
        self.assertEqual(a, True)

    def test_facing_empty2(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 0, 0)
        x.add_creature(z)
        a = x.facing_empty(0, 0)    
        self.assertEqual(a, False)

    def test_facing_empty3(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 1, 0, 0)
        x.add_creature(z)
        a = x.facing_empty(0, 0)    
        self.assertEqual(a, True)

    def test_facing_empty4(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 3, 0, 0)
        x.add_creature(z)
        a = x.facing_empty(0, 0)    
        self.assertEqual(a, False)


    def test_facing_wall1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        x.add_creature(z)
        a = x.facing_wall(0, 0)
        self.assertEqual(a, False)
    def test_facing_wall2(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 0, 0, 0)
        x.add_creature(z)
        a = x.facing_wall(0, 0)
        self.assertEqual(a, True)
    def test_facing_wall3(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 1, 0, 0)
        x.add_creature(z)
        a = x.facing_wall(0, 0)
        self.assertEqual(a, False)
    def test_facing_wall4(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 3, 0, 0)
        x.add_creature(z)
        a = x.facing_wall(0, 0)
        self.assertEqual(a, True)

    def test_facing_enemy1(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        x.add_creature(z)
        a = x.facing_enemy(0, 0)    
        self.assertEqual(a, False)


    def test_facing_enemy2(self):
        x = Darwin(2, 2)
        y = Species()
        o = Species()
        z = Creature(y, "Bob", 1, 0, 0)
        u = Creature(o, "Joe", 1, 0, 1)
        x.add_creature(z)
        x.add_creature(u)
        a = x.facing_enemy(0, 0)    
        self.assertEqual(a, True)


    def test_facing_enemy3(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        u = Creature(y, "Joe", 1, 0, 1)
        x.add_creature(z)
        x.add_creature(u)
        a = x.facing_enemy(0, 0)    
        self.assertEqual(a, False)

    def test_facing_enemy4(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 3, 0, 0)
        u = Creature(y, "Joe", 1, 0, 1)
        x.add_creature(z)
        x.add_creature(u)
        a = x.facing_enemy(0, 0)    
        self.assertEqual(a, False)

    def test_facing_enemy5(self):
        x = Darwin(2, 2)
        y = Species()
        z = Creature(y, "Bob", 1, 0, 0)
        u = Creature(y, "Joe", 1, 0, 1)
        x.add_creature(z)
        x.add_creature(u)
        a = x.facing_enemy(0, 0)    
        self.assertEqual(a, False)        


    def test_facing_enemy6(self):
        x = Darwin(2, 2)
        y = Species()
        o = Species()
        z = Creature(y, "Bob", 1, 0, 0)
        u = Creature(o, "Joe", 1, 0, 1)
        x.add_creature(z)
        x.add_creature(u)
        a = x.facing_enemy(0, 1)    
        self.assertEqual(a, False)     

    def test_print_grid(self):
        x = Darwin(1,1)
        y = Species()
        z = Creature(y, "Bob", 2, 0, 0)
        x.add_creature(z)
        a = x.print_grid()
        self.assertEqual(a, None)

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      32      1      0      0    97%   78
---------------------------------------------------------
TOTAL            50      1      6      0    98%
"""