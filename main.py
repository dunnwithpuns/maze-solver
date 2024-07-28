from graphics import Window, Line, Point 
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    cell1 = Cell(win)         
    cell2 = Cell(win)

    cell1.draw(50, 50, 70, 70)
    cell2.draw(600, 400, 700, 500)
    
    cell1.draw_move(cell2)
    

    win.wait_for_close()

if __name__ == "__main__":
    main()
