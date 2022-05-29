import tkinter as tk
from tkinter import Text
import main


class CopyRightWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Copyright Page").pack(
            side="top", fill="x", pady=10)
        text_box = Text(self, height=12, width=45)
        text_box.pack(expand=True)
        text_box.insert("end", self.copyright)
        tk.Button(self, text="Return to Home page", command=lambda: master.switch_frame(main.MainWindow),).pack()

    @property
    def copyright(self):
        copyright_symbol = "\u00A9"

        return f"""
        {copyright_symbol} 
        """

