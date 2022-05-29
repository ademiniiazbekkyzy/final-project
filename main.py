try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import copyright


class MarkApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainWindow)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Main Window").pack(side="top", fill="x", pady=10)
        self.uni_logo = Image.open("images/logo1.jpeg")
        self.uni_logo = ImageTk.PhotoImage(image=self.uni_logo)
        tk.Label(self, image=self.uni_logo,).pack()
        tk.Button(
            self,
            text="Image Processing",
            command=lambda: master.switch_frame(ImageProcessingPage),
        ).pack()
        tk.Button(self, text="Copyright", command=lambda: master.switch_frame(copyright.CopyRightWindow), ).pack()


class ImageProcessingPage(tk.Frame):
    """
    Changes the size of the image
    Applies black & white filter to the image
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.path = None
        self.canvas = None
        tk.Label(self, text="Image Processing").pack(
            side="top", fill="x", pady=20
        )
        self.configure()
        tk.Button(
            self,
            text="Return to Home page",
            command=lambda: master.switch_frame(MainWindow),
        ).pack()
        self.image = None
        self.filter_image = None

    def configure(self, *args, **kwargs):
        self.canvas = Canvas(self, width=650, height=350)
        self.canvas.pack()

        tk.Button(self, text="Black and White Filter", command=self.black_and_white_filter, ).pack()
        tk.Button(self, text="Resize", command=self.resize, ).pack()

    def resize(self):
        max_size = (600, 400)
        self.path = filedialog.askopenfilename()

        if self.path:
            self.image = Image.open(self.path)
            self.image.thumbnail(max_size)
            self.image = self.image.resize((350, 350), Image.ANTIALIAS)
            import warnings
            warnings.filterwarnings('error')

            try:
                warnings.warn("deprecated", DeprecationWarning)
            except Warning as e:
                print(e)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor="nw")

    def black_and_white_filter(self):
        max_size = (600, 400)
        self.path = filedialog.askopenfilename()

        if self.path:
            self.image = Image.open(self.path)
            self.image.thumbnail(max_size)
            self.image = self.image.convert(mode='L')
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor="nw")


if __name__ == "__main__":
    app = MarkApp()
    app.geometry("600x500")
    app.mainloop()
