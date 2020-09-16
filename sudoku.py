from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror,showinfo
from main import sudoku
main = Tk()
e = []
n = []
for i in range(9):
    n.append([])
    for j in range(9):
        n[i].append(0)
for i in range(9):
    e.append([])
    for j in range(9):
        e[i].append(0)
for i in [0,1,3,4,6,7]:
    for j in [0,1,3,4,6,7]:
        e[i][j]  = Entry(main,width=3)
        e[i][j].grid(row=i,column=j)
for i in [2,5,8]:
    for j in range(9):
        e[i][j]  = Entry(main,width=3)
        e[i][j].grid(row=i,column=j,pady=(0,5))
for  i in range(9):
    for j in [2,5,8]:
        e[i][j]  = Entry(main,width=3)
        e[i][j].grid(row=i,column=j,padx=(0,5))
def clear():
    for i in range(9):
        for j in range(9):
            e[i][j].delete(0,END)
def run():
    for i in range(9):
        n.append([])
        for j in range(9):
            temp = e[i][j].get()
            if temp.strip()=='':
                n[i][j] = int(0)
            elif temp.isnumeric() and int(temp) in range(1,10):
                n[i][j] = int(temp)
            else:
                showerror("Error!","Enter a valid number")
                return
    if sudoku(n):
        clear()
        for i in range(9):
            for j in range(9):
                e[i][j].insert(0,n[i][j])
    else:
        showinfo("Oops", "No solution for current entry")

Button(main,text='Solve',command=run).grid(row=10,column=10)
Button(main,text='Clear',command=clear).grid(row=11,column=10)

mainloop()