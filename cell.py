from graphics import Line, Point

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

    def draw_move(self, to_cell, undo=False):

        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        middle1 = Point(x1, y1)

        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        middle2 = Point(x2, y2)
        
        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(middle1, middle2) 
        
        self._win.draw_line(line, fill_color)


