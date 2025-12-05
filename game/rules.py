# check rule of chess game
#checkmate, stalemate, draw, en passant, castling, promotion bla bla bla
# legal move ... etc

class ChessRules:
    def __init__(self, board):
        self.board = board

    def is_checked(self, board , color , pos: tuple) -> bool :
        directions = [(1,0,"R"),(-1,0,"R"),(0,1,'R'),(0,-1,"R"),(1,1,"B"),(1,-1,"B"),(-1,1,"B"),(-1,-1,"B")]
        x, y, name = pos
        for dx, dy in directions:
            nx, ny = x+dx , y+dy
            enemy_name = board.get_piece(nx, ny).name
            while board.in_bounds(nx, ny):
                if board.is_enemy(nx, ny, self.color) and enemy_name in name or enemy_name  == "Q":
                    return True
                nx += dx
                ny += dy
        offsets = [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for dx, dy in offsets:
            nx, ny = x+dx, y+dy
            enemy_name = board.get_piece(nx, ny).name
            if board.in_bounds(nx, ny):
                if board.is_enemy(nx, ny, self.color) and enemy_name == "N":
                    return True
        return False
    def promotion(self, board, color, pos: tuple) -> list:
        x, y, name = pos
        enemy_name = name
        while board.in_bounds(x,y):
            if board.promoted = True:
                return ['R','B','N','Q']
    # thêm các phương thức kiểm tra luật chơi ở đây nhé em
    # ví dụ như is_checkmate, is_stalemate, is_draw, can_castle, can_en_passant, can_promote ...
    # mỗi method sẽ trả về True/False hoặc các thông tin cần thiết khác
    # nhớ viết theo OOP và đừng nhét quá nhiều logic vào đây nhé
    # mỗi class/module chỉ nên đảm nhiệm 1 trách nhiệm duy nhất
    # cái này đảm nhiệm việc kiểm tra luật chơi của cờ vua dựa trên trạng thái hiện tại của bàn cờ (board) 
