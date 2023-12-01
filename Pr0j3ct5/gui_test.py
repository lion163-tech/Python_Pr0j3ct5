
#Imports
import tkinter as tk
from tkinter import ttk
#window
window = tk.Tk()
window.title('Welcome')
window.geometry('300x150')
#title
title_label = ttk.Label(master=window, text='Miles to Kilometres', font='ComicSans 20')
title_label.pack()
#NOTHING BEYOND THIS ONE LINE
window.mainloop()