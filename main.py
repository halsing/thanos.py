#!/usr/bin/python3

import os
import time
import tkinter as tk
from tkinter import ttk, filedialog

from thanos import ThanosGlove


class ThanosMind(tk.Tk):
    """
    Main container for all frames include base setings and frames names
    """

    length_del_files = 0
    all_files = []
    error_files = []
    directory = ""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, DirnamePage, LoadingPage, FinalPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    """
    First page just show the button to start
    """

    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StartPage")
        label.pack()
        start_button = ttk.Button(
            self, text="Let's start!", command=lambda: controler.show_frame(DirnamePage)
        )
        start_button.pack()

        exit_button = ttk.Button(self, text="Exit", command=controler.destroy)
        exit_button.pack()


class DirnamePage(tk.Frame):
    """
    This frame get value from user input about path to directory
    """

    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        self.controler = controler
        self.parent = parent

        label = tk.Label(self, text="Where do You want use Thanos ?")
        label.pack()

        dir_location = tk.Entry(self, width=100)
        dir_location.pack()
        dir_location.delete(0, tk.END)
        dir_location.insert(0, str(os.getcwd()))

        confirm_button = ttk.Button(
            self,
            text="Confirm",
            command=lambda: self.thanos_confirm(dir_location.get()),
        )
        confirm_button.pack()

        exit_button = ttk.Button(self, text="Exit", command=controler.destroy)
        exit_button.pack()

    def thanos_confirm(self, location: str) -> None:
        correct_dirname = ThanosGlove.check_dirname(str(location))
        if correct_dirname is True:
            self.controler.directory = str(location)
            self.controler.show_frame(LoadingPage)
        else:
            pass


class LoadingPage(tk.Frame):
    """
    After load button all process will start. 
    At first, program will get all files from current directory 
    and all subdirectories. After that, thanos.py will remove randomly 
    half of files. 
    """

    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        self.controler = controler
        label = tk.Label(self, text="Loading Page")
        label.pack()

        load_button = ttk.Button(
            self,
            text="Are You sure to do this ?",
            command=lambda: self.check_directory(),
        )
        load_button.pack()

        exit_button = ttk.Button(self, text="Exit", command=controler.destroy)
        exit_button.pack()

    def check_directory(self):
        all_files = ThanosGlove.list_of_files(self.controler.directory)
        del_list_length = ThanosGlove.remove_files(all_files)
        self.controler.length_del_files = del_list_length


class FinalPage(tk.Frame):
    """
    Just a final page
    """

    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StartPage")
        label.pack()

        exit_button = ttk.Button(self, text="Exit", command=controler.destroy)
        exit_button.pack()


if __name__ == "__main__":
    app = ThanosMind()
    app.title("Thanos.py")
    app.geometry("280x100")
    app.mainloop()
