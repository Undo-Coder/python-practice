import os
import shutil

def SetPath (Is_Again=False):

    if Is_Again: print("That folder doesn't exist")

    input_Path = str(input("Please enter the folder path (example: C:/Users/name/example/):"))

    return input_Path

def CheckExists(path):

    Check = os.path.exists(path)

    if Check:
        return path
    else:
        SetPath(True)

def Categorize(Keywords="none/none",path="./"):
    word = []

    word = Keywords.split('/')

    files = [f for f in os.listdir(path)]

    for element in word:

        FolderPath = str(path) + str(element)

        os.makedirs(element, exist_ok=True)

        for file in files:
            if element in file:
                shutil.move(path+file, FolderPath)

Dir_Path = CheckExists(SetPath(False))

if Dir_Path[-1] != "/":
    Dir_Path += "/"

if Dir_Path != None:
    print("Please write the keywords to classify. \n(example: banana/apple/kiwi)")

    keywords = str(input(":"))

    Categorize(keywords,Dir_Path)