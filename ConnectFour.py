import tkinter as tk
import time

class Connect4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four")
        self.canvas = tk.Canvas(self.root, width=700, height=600, bg='white')
        self.canvas.pack()
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.player = 1
        self.animation_done = False
        self.draw_board()
        self.ai_move()
        self.canvas.bind("<Button>", self.on_click)
        self.root.mainloop()
        
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                self.canvas.create_rectangle(100 * col, 100 * row, 100 * (col + 1), 100 * (row + 1), fill="blue")
                self.canvas.create_oval(100 * col + 10, 100 * row + 10, 100 * (col + 1) - 10, 100 * (row + 1) - 10, fill="white")

                if self.board[row][col] == 1:
                    self.canvas.create_oval(100 * col + 10, 100 * row + 10, 100 * (col + 1) - 10, 100 * (row + 1) - 10, fill="red")
                elif self.board[row][col] == 2:
                    self.canvas.create_oval(100 * col + 10, 100 * row + 10, 100 * (col + 1) - 10, 100 * (row + 1) - 10, fill="yellow")

        if (self.winner() and self.animation_done):
            if self.player == 1:
                t = "Game Over! \n   P1 Wins!" 
            else:
                t="Game Over! \n   P2 Wins!"
            self.canvas.create_text(350, 75, text=t, font=("Helvetica", 45), fill="red")
            
    def evaluate(self):
        score = 0
        center_array = [self.board[i][3] for i in range(6)]
        score += center_array.count(1) * 3 - center_array.count(2) * 3

        for row in range(6):
            for col in range(4):
                window = [self.board[row][col+i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Vertical
        for col in range(7):
            for row in range(3):
                window = [self.board[row+i][col] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Positive Diagonal
        for row in range(3):
            for col in range(4):
                window = [self.board[row+i][col+i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Negative Diagonal
        for row in range(3):
            for col in range(3, 7):
                window = [self.board[row+i][col-i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        return score

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = 2 if piece == 1 else 1

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 5

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 80

        return score
    
    def find_row_for_col(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                return row
        return -1
    
    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.winner():
            return self.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            for col in range(7):
                row = self.find_row_for_col(col)
                if row != -1:
                    self.board[row][col] = 1
                    eval = self.minimax(depth - 1, alpha, beta, False)
                    self.board[row][col] = 0
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for col in range(7):
                row = self.find_row_for_col(col)
                if row != -1:
                    self.board[row][col] = 2
                    eval = self.minimax(depth - 1, alpha, beta, True)
                    self.board[row][col] = 0
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval


    def ai_move(self):
        best_score = float('-inf')
        best_col = 0
        for col in range(7):
            row = self.find_row_for_col(col)
            if row != -1:
                self.board[row][col] = 1 
                score = self.minimax(5, float('-inf'), float('inf'), False)
                self.board[row][col] = 0
                if score > best_score:
                    best_score = score
                    best_col = col

        self.drop_piece(best_col)
        self.player = 2

                    
    def on_click(self, event):
        col = event.x // 100
        if self.board[0][col] == 0:
            self.drop_piece(col)
            if not self.winner():
                self.ai_move()
    
    def game_over(self, event):
        print("Game is over!")
        
    def winner(self):
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != 0:
                    return True

        for row in range(3):
            for col in range(7):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return True

        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0:
                    return True

        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row + 1][col - 1] == self.board[row + 2][col - 2] == self.board[row + 3][col - 3] != 0:
                    return True
                
        return False
    
    def drop_piece(self, column):
        row = None
        for i in range(5, -1, -1):
            if self.board[i][column] == 0:
                row = i
                break

        if row is not None:
            for animation_row in range(0, row + 1):
                self.animation_done = False
                self.board[animation_row][column] = self.player
                self.draw_board()
                self.board[animation_row][column] = 0
                self.root.update()
                time.sleep(0.1)
                self.canvas.bind("<Button>", self.game_over)
            self.animation_done = True

            self.board[row][column] = self.player
            self.canvas.bind("<Button>", self.on_click)
            if self.winner():
                print(f"p{self.player} wins")
                self.canvas.bind("<Button>", self.game_over)
            
            self.draw_board()
            self.player = 2 if self.player == 1 else 1


board_game = Connect4()