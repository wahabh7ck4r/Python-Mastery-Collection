import tkinter as tk
from time import strftime


def time():
    string = strftime('%H:%M:%S %p')  
    label.config(text=string)
    label.after(1000, time) 
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100") 


label = tk.Label(root, font=('calibri', 35, 'bold'), background='gray', foreground='white')
label.pack(anchor='center')

time()

root.mainloop()
