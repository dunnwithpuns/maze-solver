from graphics import Window, Line, Point 
from cell import Cell
from maze import Maze

def main():
    num_cols = 12
    num_rows = 14
    margin = 20
    win_x = 800
    win_y = 600
    cell_size_x = (win_x - 2 * margin) / num_cols
    cell_size_y = (win_y - 2 * margin) / num_rows
    win = Window(win_x, win_y)
    
    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    m1.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
