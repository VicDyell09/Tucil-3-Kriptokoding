import pathlib

# fungsi read file 
def readkey(filename):
    with open(filename, "r") as f:
        text = f.read().split(",")
    return(text)    

# fungsi read file 
def readfile(filename):
    with open(filename, "r") as f:
        text = f.read()
    return(text)          

#funsi write file txt
def writefile(text,filename):
    with open('%s.txt' % (pathlib.Path(filename).stem), 'w') as f:
        f.write(text)
    f.close()

#fungsi return file extention
def fileext(filename):
    return pathlib.Path(filename).suffix

def appendfile(text, filename):
    with open('%s.txt' % (pathlib.Path(filename).stem), "a") as f:
        f.write(text)
    f.close()