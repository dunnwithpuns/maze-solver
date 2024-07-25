from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(400, 300)
    line1 = Line(p1, p2)
    # win.draw_line(line1, "red")
    p3 = Point(800, 0)
    line2 = Line(p2, p3)
    win.draw_line(line2, "green")
    win.wait_for_close()

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="white")
        self.canvas.pack()
        self.is_running = False
 
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
 
    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()
 
    def close(self):
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


if __name__ == "__main__":
    main()
