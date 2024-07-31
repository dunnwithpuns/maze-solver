import time
import random
from cell import Cell
from graphics import Line, Point

class Maze:
    def __init__(
            self,
            x1, 
            y1,
            num_rows, 
            num_cols,
            cell_size_x, 
            cell_size_y,
            win=None,
            seed=None,
        ):

        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            self._seed = random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):

        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # check if each neighbor has been visited and if so add it to next_coords list 
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j)) 
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1)) 
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if no possible_directions 
            # break out of loop
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
           
            # choose random cell 
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]
            
            # knock down the walls between current and chosen cell           
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            
            # left 
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False 

            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
 
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])
                        
    def _reset_cells_visited(self):

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
        
    def solve(self):
        print(f"starting to solve {self._num_rows} rows, {self._num_cols} cols")
        return self._solve_r(i=0, j=0)
 
    def _solve_r(self, i, j):
        if not (0 <= i < self._num_cols and 0 <= j < self._num_rows):
            print(f"Out of bounds: ({i}, {j})")
            return False

        print(f"visiting cell: ({i}, {j})")
        self._animate()

        self._cells[i][j].visited = True

        if self._cells[i][j] == self._cells[self._num_cols - 1][self._num_rows - 1]:
            print("reached the end cell")
            return True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            d_i, d_j = direction
            new_i = i + d_i
            new_j = j + d_j

            if (
                0 <= new_i < self._num_cols and 
                0 <= new_j < self._num_rows and 
                not self._cells[new_i][new_j].visited and
                not self.walls_blocking(i, j, new_i, new_j)
            ):
                print(f"moving to: {new_i}, {new_j}")
                self._cells[i][j].draw_move(self._cells[new_i][new_j])

                if self._solve_r(new_i, new_j):
                    return True
            
                self._cells[new_i][new_j].draw_move(self._cells[i][j], undo=True)

        return False

    def walls_blocking(self, i, j, new_i, new_j):
        direction = new_i - i, new_j - j

        # left
        if (
            direction == (-1, 0)
            and not self._cells[i][j].has_left_wall
            and not self._cells[new_i][new_j].has_right_wall
        ):
            return False
        
        # right
        if (
            direction == (1, 0)
            and not self._cells[i][j].has_right_wall
            and not self._cells[new_i][new_j].has_left_wall
        ):
            return False
        
        # up
        if (
            direction == (0, -1)
            and not self._cells[i][j].has_top_wall
            and not self._cells[new_i][new_j].has_bottom_wall
        ):
            return False
        
        # down
        if (
            direction == (0, 1)
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[new_i][new_j].has_top_wall
        ):
            return False
        
        return True

