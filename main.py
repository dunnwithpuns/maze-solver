from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)    
    cell_noright = Cell(win, right=False)
    cell_nobot = Cell(win, bottom=False) 

    cell.draw(400, 400, 475, 475)
    cell_noright.draw(100, 50, 150, 100)
    cell_nobot.draw(375, 275, 425, 325)    

    win.wait_for_close()

if __name__ == "__main__":
    main()
