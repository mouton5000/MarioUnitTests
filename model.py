import curses
EMPTY = 0
GROUND = 1
SPIKE = 2
OUT = 3


MUSHROOM = 0

symbols = [' ', 'T', 'X', 'O']
items_symbol = ['P']
mariosymb = 'M'

class Level:
    def __init__(self, stdscr, width, height, ml, mc):
        self.width = width
        self.height = height
        self.cells = [[Cell(EMPTY, l, c) for c in range(width)] for l in range(height)]
        self.mario = Mario(ml, mc)
        self.stdscr = stdscr

    def set_platform(self, l, c, w):
        for cp in range(w):
            self.cells[l][c + cp].type = GROUND
            
    def set_spikes(self, l, c, w):
        for cp in range(w):
            self.cells[l][c + cp].type = SPIKE

    def set_items(self, l, c , it):
        self.cells[l][c].item = it

    def move_mario(self, dc, display=False):
        if self.mario.c == 0 and dc == -1:
            return
        if self.mario.c == self.width -1 and dc == 1:
            return
        self.mario.c += dc

        if self.get_cell_below_mario().type == SPIKE:
            self.kill_mario()

        if self.get_cell_on_mario().item == MUSHROOM:
            self.mario.grows()
            self.get_cell_on_mario().item = None

        


    def get_cell_below_mario(self):
        return self.cells[self.mario.l + 1][self.mario.c]

    def get_cell_on_mario(self):
        return self.cells[self.mario.l][self.mario.c]

    def jump_mario(self):
        if self.mario.vl != 0 or self.get_cell_below_mario().type != GROUND:
            return
        self.mario.vl = 2

    def update(self):
        if self.mario.vl != 0 or self.get_cell_below_mario().type != GROUND:
            if self.mario.vl > 0:
                for l in range(self.mario.l - 1, self.mario.l - self.mario.vl - 1, -1):
                    if self.cells[l][self.mario.c].type == GROUND:
                        self.mario.vl = 0
                        self.mario.l = l + 1
                        break
                    elif self.cells[l][self.mario.c].type == SPIKE:
                        self.kill_mario()
                else:
                    self.mario.l -= self.mario.vl
                    self.mario.vl -= 1
            else:
                for l in range(self.mario.l + 1, self.mario.l - self.mario.vl + 1):
                    if self.cells[l][self.mario.c].type == GROUND:
                        self.mario.vl = 0
                        self.mario.l = l - 1
                        break
                    elif self.cells[l][self.mario.c].type == SPIKE:
                        self.kill_mario()


                else:
                    self.mario.l -= self.mario.vl
                    self.mario.vl -= 1


    def kill_mario(self) :
        self.mario.vl = 0
        self.mario.c = 0
        self.mario.l = self.height - 2
        self.mario.size = 1

    def display(self):
        for line in self.cells:
            for cell in line:
                cell.display(self.stdscr)
        self.mario.display(self.stdscr)
        self.stdscr.refresh()



class Cell:
    def __init__(self, t, l, c, item=None):
        self.type = t
        self.l = l
        self.c = c
        self.item = item
    
    @property
    def type(self):
        return self.__t

    @type.setter
    def type(self, t):
        self.__t = t

    def display(self, stdscr, refresh=False):
        stdscr.addstr(self.l, self.c, symbols[self.type])
        if self.item is not None:
            stdscr.addstr(self.l, self.c, items_symbol[self.item])
        if refresh:
            stdscr.refresh()


class Mario:
    def __init__(self, l, c):
        self.l = l
        self.c = c
        self.vl = 0
        self.size = 1

    def display(self, stdscr, refresh=False):
        stdscr.addstr(self.l, self.c, mariosymb)
        if self.size == 2:
            stdscr.addstr(self.l -1, self.c, mariosymb)

        if refresh:
            stdscr.refresh()

    def grows(self):
        self.size = 2
