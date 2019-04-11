def writetext(mytext, filename):
    fp = open(filename, "w")
    fp.write(mytext)
    fp.close()
    save = ("what do you want to save")

def readtext(filename):
    fp = open(filename, "r")
    text = fp.read()
    print("read file : ", text)
    fp.close()

filenam = str(input("where do you wanna save ? :"))
writetext(input("enter what you wanna save ? :"), filenam)
readtext(filenam)
#sudo apt inatall python3-bs4