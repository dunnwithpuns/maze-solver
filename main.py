from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)    
    cell_noright = Cell(win, right=False)
    cell_TR = Cell(win, left=False, bottom=False)
    cell_nobot = Cell(win, bottom=False) 
    cell_notop = Cell(win, top=False)
    cell_BL = Cell(win, right=False, top=False)

    cell.draw(400, 400, 475, 475)
    cell_noright.draw(100, 50, 150, 100)
    cell_nobot.draw(375, 275, 425, 325)    
    cell_TR.draw(200, 200, 300, 300)
    cell_BL.draw(50, 400, 100, 450)
    cell_notop.draw(700, 500, 750, 550)

    win.wait_for_close()

if __name__ == "__main__":
    main()
