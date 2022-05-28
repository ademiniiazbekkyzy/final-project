try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from tkinter import *

import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Text

# root = Tk()
# root.title('Ademi')
# root.geometry('300x700')
# root.iconbitmap('c')


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
        tk.Button(self, text="Copyright", command=lambda: master.switch_frame(CopyRightWindow),).pack()


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


# def forward(image_number):
#     global my_label
#     global button_back
#     global button_forward
#     my_label.grid_forget()
#     my_label = Label(image=image_list[image_number - 1])
#     button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
#     button_back = Button(root, text='<<', command=lambda: backward(image_number-1))
#
#     if image_number == 2:
#         button_forward = Button(root, text='>>', state=DISABLED)
#     my_label.grid(row=0, column=0, columnspan=3)
#     button_back.grid(row=1, column=0)
#     button_forward.grid(row=1, column=2)
#
#
# def backward(image_number):
#     global my_label
#     global button_back
#     global button_forward
#     my_label.grid_forget()
#     my_label = Label(image=image_list[image_number - 1])
#     button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
#     button_back = Button(root, text='<<', command=lambda: backward(image_number - 1))
#
#     if image_number == 2:
#         button_back = Button(root, text='<<', state=DISABLED)
#     my_label.grid(row=0, column=0, columnspan=3)
#     button_back.grid(row=1, column=0)
#     button_forward.grid(row=1, column=2)


# img1 = ImageTk.PhotoImage(Image.open('images/logo1.jpeg'))
# img2 = ImageTk.PhotoImage(Image.open('images/logo2.png'))
# image_list = [img1, img2]
#
# my_label = Label(image=img1)
# button_back = Button(root, text='<<', command=backward, state=DISABLED)
# button_forward = Button(root, text='>>', command=lambda: forward(1))
# button_exit = Button(root, text='Exit App', command=root.quit)
# my_label.grid(row=0, column=0, columnspan=3)
# button_back.grid(row=1, column=0)
# # button_exit.grid(row=1, column=1)
# button_forward.grid(row=1, column=2)


# img2 = ImageTk.PhotoImage(file='images/logo2.jpeg')
#
# my_label = Label(root, image=img2)
# my_label.pack(pady=20)

# button_quit = Button(root, text='Exit Program', command=root.quit)
# button_quit.pack()
