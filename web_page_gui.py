from tkinter import *
import tkinter as tk

import web_page_generator

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        
        self.btn_add = tk.Button(self.master,width=30,height=2,text='Set a new body text of your choice',command=lambda: web_page_generator.addToBody(self))
        self.btn_add.grid(row=0,column=2,padx=(100,80),pady=(10,0),sticky=W)

        self.txt_body = tk.Entry(self.master,text='')
        self.txt_body.grid(row=1,column=2,rowspan=1,columnspan=2,padx=(100,80),pady=(30,40),sticky=N+E+W)
        

       
        

                   






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

