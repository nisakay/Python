import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
               'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('file.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        File_Name TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('file.db')
with conn:
    cur = conn.cursor()
    cur.execute
    for i in fileList:
        if i.endswith('.txt'):
           print(i) 

    cur.execute("INSERT INTO tbl_file(File_Name) VALUES (?)", (i,))

    conn.commit()
conn.close()





        
                       
                           
        
    


        
           
        


        


