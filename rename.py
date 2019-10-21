import os

#set up the rules
repl = {
    '&': '-and-',
    '_': '-',
    "’": "",
    "'": "",
    ',': '',
    ' ': '-',
    '--': '-',
}

#get current location
path = os.getcwd()

#list of all files 
filenames = os.listdir(path)

#loop through the files
for filename in filenames:

    filename_new = filename
    #print(filename_new)
    #loop through the dictionary
    for k, v in repl.items():
        #print (k, v)
        filename_new = filename_new.replace(k , v )
        print(filename_new)
        
    #final name to lower case
    filename_new = filename_new.lower()
    os.rename(os.path.join(path, filename), os.path.join(path, filename_new))
