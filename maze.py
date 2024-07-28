import time
from cell import Cell
from graphics import Line, Point

class Maze:
    def __init__(
            self,
            x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win,
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self): 
        
        for i in self._num_cols:
            col = []
            for j in self._num_rows:
                col.append(Cell(self._win))
            self._num_cols.append(col)

        for i in range(len(self._cells)):
            for j in range(len(col)):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        
        for i in range(len(self._cells)):
            for j in range(i):
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
        time.sleep(0.05)
