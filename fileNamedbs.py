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

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute

    for i in fileList:
        if i.endswith('.txt'):
            ("INSERT INTO tbl_persons(File_name) VALUES (?)")
            print(i)
    conn.commit()
conn.close()

        
                       
                           
        
    


        
           
        


        


