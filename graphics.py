from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
 
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
 
    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()
        print("window closed...")
 
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.is_running = False

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


class Cell:
    def __init__(
            self, 
            window,     
            left=True, right=True, top=True, bottom=True,
            ):

        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
       
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall:
            self.left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(self.left_wall)

        if self.has_right_wall:
            self.right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(self.right_wall)

        if self.has_top_wall:
            self.top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(self.top_wall)
        
        if self.has_bottom_wall:
            self.bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(self.bottom_wall)
            




