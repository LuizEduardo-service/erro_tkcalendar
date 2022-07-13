from tkcalendar import DateEntry
from tkinter import Tk



__version__ = '0.1.0'

root = Tk()

root.title('teste')
root.geometry("500x300")

data = DateEntry(root,selectmode='day')
data.grid()


root.mainloop()



