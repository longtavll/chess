# tính chất cơ bản của các quân cờ
# mỗi quân cờ sẽ kế thừa lớp Piece và định nghĩa phương thức get_moves
# có thể thêm các method khác nếu cần thiết 
# CHÚ Ý: không nên xử lí quá nhiều logic trong này (kiến thức cơ bản OOP) mỗi class (module) 
#        chỉ nên đảm nhiệm 1 trách nhiệm duy nhất
# cái này đảm nhiệm tính toán các nước đi hợp lệ của từng quân cờ dựa trên vị trí hiện tại
# oke chưa em

class Piece:
    def __init__(self, color):
        self.color = color

    def get_moves(self, board, pos):
        raise NotImplementedError()


class Knight(Piece):
    name = "N"
    offsets = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

    def get_moves(self, board, pos):
        x, y = pos
        moves = []
        for dx, dy in self.offsets:
            nx, ny = x+dx, y+dy
            if board.in_bounds(nx, ny): # kiểm tra tọa độ có thuộc bàn cờ không
                if board.is_empty(nx, ny) or board.is_enemy(nx, ny, self.color):
                    moves.append((nx, ny))
        return moves

class Bishop(Piece):
    name = "B"
    directions = [(1,1),(1,-1),(-1,1),(-1,-1)]

    def get_moves(self, board, pos):
        x, y = pos
        moves = []
        for dx, dy in self.directions:
            nx, ny = x+dx , y+dy
            while board.in_bounds(nx, ny):
                if board.is_empty(nx, ny):
                    moves.append((nx, ny))
                elif board.is_enemy(nx, ny, self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves # trả về các ô có thể đi (chưa check valid)

class Rook(Piece):
    name = "R"
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def get_moves(self, board, pos):
        x, y = pos
        moves = []
        for dx, dy in self.directions:
            nx, ny = x+dx , y+dy
            while board.in_bounds(nx, ny):
                if board.is_empty(nx, ny):
                    moves.append((nx, ny))
                elif board.is_enemy(nx, ny, self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves

class Queen(Piece):
    name = "Q"
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    def get_moves(self, board , pos):
        x, y = pos
        moves = []
        for dx, dy in self.directions:
            nx, ny = x+dx , y+dy
            while board.in_bounds(nx, ny):
                if board.is_empty(nx, ny):
                    moves.append((nx, ny))
                elif board.is_enemy(nx, ny, self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy
        return moves
    

class King(Piece):
    name = "K"
    offsets = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    def get_moves(self, board, pos):
        x, y = pos
        moves = []
        for dx, dy in self.offsets:
            nx, ny = x+dx, y+dy
            if board.in_bounds(nx, ny):
                if board.is_empty(nx, ny) or board.is_enemy(nx, ny, self.color):
                    moves.append((nx, ny))
        return moves

class Pawn(Piece):
    name = "P"

    def get_moves(self, board, pos):
        x, y = pos
        moves = []
        direction = 1 if self.color == 'white' else -1
        # đi thẳng
        if board.in_bounds(x, y + direction) and board.is_empty(x, y + direction):
            moves.append((x, y + direction))
            # bước 1 cso thể đi 2 bước
            if (self.color == 'white' and y == 1) or (self.color == 'black' and y == 6):
                if board.is_empty(x, y + 2 * direction):
                    moves.append((x, y + 2 * direction))
        # đớp
        for dx in [-1, 1]:
            nx, ny = x + dx, y + direction
            if board.in_bounds(nx, ny) and board.is_enemy(nx, ny, self.color):
                moves.append((nx, ny))
        return moves
    