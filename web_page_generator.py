from tkinter import *
import web_page_gui
import webbrowser



def userInput(self):
    userInput =  self.txt_body.get()

    # Writing to file 
    with open("webPage_generator.html", "a") as file1:
        file1.write("""<html> 
                 <body> 
                    <h1>
                          Stay tuned for our amazing summer sale! 
                    </h1>
                 </body> 
            </html> """)
        file1.writelines(userInput)
    # Reading from file
    with open("webPage_generator.html", "r+") as file1:
        print(file1.read())

    webbrowser.open_new_tab("webPage_generator.html")


if __name__ == "__main__":
    pass

