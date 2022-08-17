from calendar import firstweekday, month
from logging import root
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

my_w = tk.Tk()
my_w.geometry("400x400+200+100")
cal = Calendar(my_w,selectmode='none',firstweekday='sunday',weekenddays=[6,7],borderwidth=10)
# cal.grid(row=1,column=1,padx=10)
cal.pack(fill='both',expand=True)
my_w.mainloop()