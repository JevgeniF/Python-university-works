"""GUI Calculator for PyPi Quadeq Module."""

from quadeq import find_x
from tkinter import *


class QuadeqCalculator:
    """Class for quadratic equation calculator."""

    def __init__(self):
        """init function for tkinter window."""

        window = Tk()  # Window parameters
        window.title("Quadratic Equation Calculator")
        window.geometry('340x170')

        Label(window, text='Please input variables a, b & c.').grid(row=0)  # Window entries

        Label(window, text='variable a').grid(column=0, row=1, sticky=E)  # Variable 'a' entry field
        self.aVar = StringVar()
        Entry(window, width=10, textvariable=self.aVar).grid(column=1, row=1)
        Label(window, text='variable b').grid(column=0, row=2, sticky=E)  # Variable 'b' entry field
        self.bVar = StringVar()
        Entry(window, width=10, textvariable=self.bVar).grid(column=1, row=2)
        Label(window, text='variable c').grid(column=0, row=3, sticky=E)  # Variable 'c' entry field
        self.cVar = StringVar()
        Entry(window, width=10, textvariable=self.cVar).grid(column=1, row=3)

        Label(window, text='The equation has the following solution(s):').grid(row=5)  # Window output
        self.Solution = StringVar()
        Entry(window, width=15, textvariable=self.Solution).grid(column=1, row=6)

        Button(window, text='Calculate', command=self.compute).grid(column=1, row=4)  # Button to run process

        window.mainloop()

    def compute(self):
        """Implementation of find_x tool from quadeq package."""

        try:
            solution = find_x(float(self.aVar.get()), float(self.bVar.get()), float(self.cVar.get()))
            self.Solution.set(solution)
        except ValueError:
            self.Solution.set("Check variables!")


QuadeqCalculator()
