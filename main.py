from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(800, 600)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")
    p3 = Point(0, 600)
    p4 = Point(800, 0)
    line2 = Line(p3, p4)
    win.draw_line(line2, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()
