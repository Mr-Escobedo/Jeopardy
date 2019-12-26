#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
import sys
import os
from board_class import JeopardyBoard
from tkinter import filedialog
###TODO###
#Fix button commands (Don't want to make 30 different buttons)
#Implement importing boards
    
class BoardGUI:
    def __init__(self, height = 336, width = 648):
        '''GUI constructor'''
        self.root_window = tkinter.Tk()
        self.height = height
        self.width = width
        self.button_width = 14
        self.button_height = 3
        self.root_window.geometry("{}x{}".format(self.width, self.height))
        self.root_window.iconbitmap(self.resource_path("jeopardy.ico"))
        self.root_window.title("Jeopardy Board")
        self.root_window.resizable(False, False)
        self.score = tkinter.StringVar()
        self.show_score = tkinter.Label(self.root_window, textvariable = self.score, height = self.button_height, width = self.button_width)
        self.game = JeopardyBoard()
        self.score.set(str(self.game.get_score()))

        self.correct = "#33FF3C"
        self.blank = "#F0F0ED"
        self.wrong = "#F03320"


        for i in range(self.game.rows):
            for j in range(self.game.columns):
                button_code = """
self.button_{r}{c} = tkinter.Button(self.root_window, text = '{value:4}', command = lambda: self.f({r}, {c}))
self.button_{r}{c}.config(width = self.button_width, height = self.button_height)
self.button_{r}{c}.grid(row = {r}+1, column = {c})""".format(r=i, c=j, value = self.game.values[i])
                exec(button_code)


    def update(self, r:int, c:int):
        code = """
    if self.game.board[{row}][{col}] == None:
        self.button_{row}{col}.config(bg = self.correct)
        self.game.board[{row}][{col}] = True

    elif self.game.board[{row}][{col}] == False:
        self.button_{row}{col}.config(bg = self.blank)
        self.game.board[{row}][{col}] = None

    elif self.game.board[{row}][{col}] == True:
        self.button_{row}{col}.config(bg = self.wrong)
        self.game.board[{row}][{col}] = False
        """.format(row = r, col = c)

        exec(code)
                
        self.score.set(self.game.get_score())
    
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_board(self):
        file_path = filedialog.askopenfilename()
        file_name = file_path.split("/")[-1]
        self.game.import_board(file_name)
            
    def run(self):
        self.show_score.grid(row = 0, column = 0, columnspan = 6)
        self.export = tkinter.Button(self.root_window, text = "Export", command = self.game.export_board)
        self.export.config(height = self.button_height, width = self.button_width)
        self.export.grid(row = 0, column = 0)

        self.import_board = tkinter.Button(self.root_window, text = "Import", command = self.get_board)
        self.import_board.config(height = self.button_height, width = self.button_width)
        self.import_board.grid(row = 0, column = 5)
        
        
        self.root_window.mainloop()


if __name__ == "__main__":
    BoardGUI().run()
