import tkinter
from tkinter import *

root=tkinter.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#1716b")

label_result= Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=100)

root.mainloop()