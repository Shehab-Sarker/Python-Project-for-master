import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.current_letter = 'X'  # Human starts first

        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            btn = tk.Button(frame, text=' ', font=('Helvetica', 20), height=3, width=6,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] == ' ' and self.current_letter == 'X':
            self.make_move(index, 'X')
            if self.current_winner:
                messagebox.showinfo("Game Over", "You win!")
                self.root.quit()
                return

            if ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.quit()
                return

            self.root.after(500, self.computer_move)

    def computer_move(self):
        available = [i for i, x in enumerate(self.board) if x == ' ']
        if available:
            index = random.choice(available)
            self.make_move(index, 'O')
            if self.current_winner:
                messagebox.showinfo("Game Over", "Computer wins!")
                self.root.quit()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.quit()

    def make_move(self, index, letter):
        self.board[index] = letter
        self.buttons[index].config(text=letter, state='disabled')
        if self.check_winner(index, letter):
            self.current_winner = letter
        self.current_letter = 'O' if letter == 'X' else 'X'

    def check_winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diag2]):
                return True

        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
