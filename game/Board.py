class board:
    def __init__(self):
        self.grid = [[None]*8 for _ in range(8)]
        self.turn = "white"

    def in_bounds(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def get(self, x, y):
        return self.grid[x][y]

    def promoted(self, name, x, y):
        if name == 'P':
            if y==8 or y==0:
                return True

    def is_empty(self, x, y):
        return self.get(x, y) is None

    def is_enemy(self, x, y, color):
        p = self.get(x, y)
        return p and p.color != color
