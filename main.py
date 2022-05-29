try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Text, filedialog


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
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        self.uni_logo = Image.open("images/logo1.jpeg")
        self.uni_logo = ImageTk.PhotoImage(image=self.uni_logo)
        tk.Label(self, image=self.uni_logo,).pack()
        tk.Button(
            self,
            text="Image Processing",
            command=lambda: master.switch_frame(ImageProcessingPage),
        ).pack()
        tk.Button(self, text="Copyright", command=lambda: master.switch_frame(CopyRightWindow), ).pack()


class ImageProcessingPage(tk.Frame):
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

        tk.Button(self, text="Resize", command=self.resize, ).pack()

    def resize(self):
        max_size = (590, 350)
        self.path = filedialog.askopenfilename()

        if self.path:
            self.image = Image.open(self.path)
            self.image.thumbnail(max_size)
            self.image = self.image.resize((100, 100), Image.ANTIALIAS)
            import warnings
            warnings.filterwarnings('error')

            try:
                warnings.warn("deprecated", DeprecationWarning)
            except Warning as e:
                print(e)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor="nw")


class CopyRightWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Copyright Page").pack(
            side="top", fill="x", pady=10)
        text_box = Text(self, height=12, width=45)
        text_box.pack(expand=True)
        text_box.insert("end", self.copyright)
        tk.Button(self, text="Return to Home page", command=lambda: master.switch_frame(MainWindow),).pack()

    @property
    def copyright(self):
        copyright_symbol = "\u00A9"

        return f"""
        {copyright_symbol} 
        """


if __name__ == "__main__":
    app = MarkApp()
    app.mainloop()
