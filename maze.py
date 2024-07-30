import time
import random
from cell import Cell
from graphics import Line, Point

class Maze:
    def __init__(
            self,
            x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win,
            seed=None,
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = 0
        if seed:
            self._seed = random.seed(seed)
        self._create_cells()
        
    def _create_cells(self):

        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(col)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        
       # calculate x1 based on current col index (i) and cell size 
        x1 = self._x1
        if i != 0: 
            x1 += i * self._cell_size_x   
       
        # calculate y1 based on current row index (i) and cell size 
        y1 = self._y1
        if j != 0:
            y1 += j * self._cell_size_y
        
        # calculate x2 and y2 using x1 and y1 and cell_size
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        for k in range():
            possible_dirs = []

            # check if each neighbor has been visited and if so add it to next_coords list 
            if self._cells[i][j + 1] and self._cell[i][j + 1].visited == False:
                possible_dirs.append([i, j + 1])
            if self._cells[i + 1][j] and self._cell[i + 1][j].visited == False:
                possible_dirs.append([i + 1, j])
            if self._cells[i - 1][j] and self._cell[i - 1][j].visited == False:
                possible_dirs.append([i - 1, j])
            if self._cells[i][j - 1] and self._cell[i][j - 1].visited == False:
                possible_dirs.append([i, i - 1]) 
           
            if len(possible_dirs) == 0:
                return
            
                        
            


