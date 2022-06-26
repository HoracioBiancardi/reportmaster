from tkinter import *


class CentreWindow:
    def __init__(self, width, height, winfo_width, winfo_height):

        self.window_width = width
        self.window_height = height
        self.winfoscreenwidth = winfo_width
        self.winfoscreenheight = winfo_height
        self.retorno = 0
        self.calculoScreen()

    def calculoScreen(self):
        self.screen_width = self.winfoscreenwidth
        self.screen_height = self.winfoscreenheight

        self.position_top = int(self.screen_height / 2 - self.window_height / 2)
        self.position_right = int(self.screen_width / 2 - self.window_width / 2)
        self.retorno = str(
            f"{self.window_width}x{self.window_height}+{self.position_right}+{self.position_top}"
        )
