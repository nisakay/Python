import glob
import os
import datetime
import shutil

def GetFileList(path, type):
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)

originPath = '/Users/lione/OneDrive/Desktop/Folder A//'
destinationPath = '/Users/lione/OneDrive/Desktop/Folder B//'
fileType = ".txt"

# Create list of text filenames in Origin folder
fileList = GetFileList(originPath, fileType)

for file in fileList:
    # Get last modified date and today's date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()
    
    filePathList = file.split("\\") # Create a list from the filepath
    filename = filePathList[-1] # The last element is a the filename
    
    # If modified within last 24 hours, then copy to destination folder
    modifyDateLimit = modifyDate + datetime.timedelta(days=1)

    # If the file was edited less then 24 hours ago then copy it
    if modifyDateLimit > todaysDate:
         shutil.copy2(file, destinationPath + filename)
   
    

     
     

    
