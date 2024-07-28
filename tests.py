import unittest
from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    
    
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols, 
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_1(self):
        win = Window(800, 600)
        num_cols = 20
        num_rows = 15
        m1 = Maze(50, 50, num_rows, num_cols, 25, 25, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def tests_maze_create_cells_2(self):
        win = Window(800, 600)
        num_cols = 5
        num_rows = 5
        m1 = Maze(100, 50, num_rows, num_cols, 100, 100, win)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
if __name__ == "__main__":
    unittest.main()
