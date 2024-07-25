from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    cell = Cell(win)    
    p1 = Point(50, 50)
    p2 = Point(55, 55)
    p3 = Point(100, 50)
    p4 = Point(150, 100)

    cell.draw(p1, p2)
    cell.draw(p3, p4)

    win.wait_for_close()

if __name__ == "__main__":
    main()
