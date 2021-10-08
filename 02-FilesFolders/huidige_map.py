import os

def getdir():
    workfolder = os.getcwd()
    print("The current directory is:", workfolder)

def mkdir():
    foldername = input("Choose a name for the folder: ")
    
    dirnamelength = len(foldername)
    if dirnamelength > 0:
        os.mkdir(foldername)
        print(foldername, " has been created.")
    else:
        print("Je hebt geen naam ingevoerd.")

while True:
    print('Type help for a list of commands.')
    command_line = input(">")

    if command_line == "help":
        print("getdir - Grabs the directory this program has been executed in.")
        print("help - Do I really have to explain this one?")
        print("mkdir - Creates a folder in the directory that this program has been executed in.")

    if command_line == 'getdir':
        getdir()

    if command_line == 'mkdir':
        mkdir()