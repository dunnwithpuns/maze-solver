from graphics import Window, Line, Point 
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 14
    num_rows = 16
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
