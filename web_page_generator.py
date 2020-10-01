from tkinter import *
import web_page_gui

def addToBody(self):
    f = open("webPage_generator.html", "a")
    f.write("""<html> 
                 <body> 
                    <h1>
                          Stay tuned for our amazing summer sale! 
                    </h1>
                 </body> 
            </html> """)
    f.close()

    #open and read the file after the appending:
    f = open("webPage_generator.html", "r")
    print(f.read())




if __name__ == "__main__":
    pass

