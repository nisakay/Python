import glob
import os
import datetime
import shutil
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox, filedialog 



class ParentWindow(Frame):
        def __init__ (self, master, *args, **kwargs):

            Frame.__init__(self, master, *args, **kwargs)

            self.master = master
            self.master.minsize(820,130) #(Height, Width)
            self.master.maxsize(820,130)
            self.master.title('File Transfer')
            self.master.config(bg='lightgray')

            link_Label = Label(root, text ="Select The File To Copy : ",bg = "#E8D579") 
            link_Label.grid(row = 1, column = 0, pady = 5, padx = 5)

            root.sourceText = Entry(root, width = 50, textvariable =lambda: setSourceDir(self)) 
            root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2)

            self.btnSource = Button(self.master, text="Browse", width=10, height=2, command=lambda: setSourceDir(self))
            self.btnSource.grid(row=1,column=3,padx=(5,0), pady=(5,0), sticky=NE)

            destinationLabel = Label(root, text ="Select The Destination  : ",bg ="#E8D579") 
            destinationLabel.grid(row = 2, column = 0,pady = 5, padx = 5) 
    

            root.destinationText = Entry(root, width = 50,textvariable =lambda: setDestDir(self)) 
            root.destinationText.grid(row = 2, column = 1,pady = 5, padx = 5,columnspan = 2)

            self.btnDest = Button(self.master, text="Browse", width=10, height=2, command=lambda: setDestDir(self))
            self.btnDest.grid(row=2,column=3,padx= 5, pady= 5, sticky=NE)

            self.moveFiles = Button(root, text ="Move File",command=lambda: MoveFile(self), width = 15)
            self.moveFiles.grid(row = 3, column = 2, pady = 5, padx = 5) 


def GetFileList(path, type):
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)


def setSourceDir(self):

                root.source = os.path.normpath(askdirectory())

                root.sourceText.insert('1', root.source)

def setDestDir(self):
    
                root.destination = os.path.normpath(askdirectory())

                root.destinationText.insert('1', root.destination)

def MoveFile(self):

    fileType = ".txt"

    # Create list of text filenames in Origin folder
    fileList = GetFileList(root.source, fileType)

    for file in fileList:
        # Get last modified date and today's date
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
        
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        # If the file was edited less then 24 hours ago then copy it
        if modifyDateLimit > todaysDate:
             shutil.copy2(file, setDestDir + filename)

    messagebox.showinfo("SUCCESSFULL") 



if __name__ == "__main__":
   root = tk.Tk()
   App = ParentWindow(root)
   root.mainloop()



             



       
 

     
     

    
