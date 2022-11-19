import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import easygui
import shutil


'''


a. tkinter: It is the most used Graphical User Interface package in python.
b. filedialog: While working with files, filedialog provides a set of dialogs.
c. easygui: It is the most easy Graphical User Interface module. This module is not event driven.
d. os: When different files are processed from different locations.
e. messagebox: Message boxes are displayed with the help of messagebox.
'''

#Saving a file
def Save():
    def SaveAs():
        FileName = filedialog.asksaveasfile(initialdir="/",defaultextension='.txt',filetypes=[("text files",".txt"),("all files",".*")])
        FileText=str(textspace.get(1.0,END))
        FileName.write(FileText)
    Screen.destroy()
    SaveWindow= Tk()
    button = Button(text="SaveAs", command=SaveAs)
    button.pack()
    textspace = Text(SaveWindow)
    textspace.pack()

'''Code Explanation:

Save function displays a text area where we can enter the text that is to be saved. SaveAs function saves the file.
a. destroy: It is used to destroy a widget.
b. Tk(): We create Tk() to initialise the tkinter module.
c. pack(): It organizes widgets in blocks. After this they are placed in the parent widget.
d. filetypes: It contains the type of the file.'''





#opening a file
def Open():
    Read=easygui.fileopenbox()
    try:
        os.startfile(Read)
    except:
        mb.showinfo("file not found")

'''
a. fileopenbox(): It is used to display the files. Only those files are displayed whose path matches the default file path.
b. startfile(): It opens the file.
c. showinfo(): It is used to display the information in the form of a pop up.
'''

#Renaming a file
def Rename():
    Read=easygui.fileopenbox()
    pathnew = os.path.dirname(Read)
    extension=os.path.splitext(Read)[1]
    print("Enter new name of the file")
    newName=input()
    path1 = os.path.join(pathnew, newName+extension)
    print(path1)
    os.rename(Read,path1) 
    mb.showinfo("File Renamed !")


'''Code Explanation:

a. splittext(): This widget splits the path into ext and pair root.
b. showinfo(): It displays the text on the screen.
c. join(): It joins two different texts into one string.
'''

#deleting a file
def Delete():
    Read=easygui.fileopenbox()
    if os.path.exists(Read):
        os.remove(Read)             
    else:
        mb.showinfo("File not found , please check!")

'''Code Explanation:
a. exists(): It checks whether the path mentioned exists or not.
b. remove(): The given object is removed from the list with this widget.'''


#copying a file
def Copy():
    Read=easygui.fileopenbox()
    destination1=filedialog.askdirectory()
    shutil.copy(Read,destination1)
    mb.showinfo("File successfully copied ")

'''Code Explanation:
a. shutil: Various operations related to files are offered in this module.'''


#deleting a folder
def DeleteFolder():
    DelFolder = filedialog.askdirectory()
    os.rmdir(DelFolder)
    mb.showinfo("Folder successfully deleted")


'''Code Explanation:
a. rmdir(): Removal of an empty folder is done with this widget.
b. askdirectory(): Prompting the user to select a directory.'''

#creating a folder
def CreateFolder():
    Folder = filedialog.askdirectory()
    print("Enter a name for the folder")
    NewFolder=input()
    path = os.path.join(Folder, NewFolder)  
    os.mkdir(path)
    mb.showinfo("Folder created successfully")

'''Code Explanation:

a. input(): It takes input from the user.
b. mkdir(): New directory with a new path is created with this widget.'''    

#Moving the file
def MoveFile():
    Read=easygui.fileopenbox()
    Destination =filedialog.askdirectory()
    if(Read==Destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(Read, Destination)  
        mb.showinfo("File has moved been successfully")

'''Code Explanation:
a. move(): A folder can be moved to another location with this widget.'''

#creating buttons and Initializing window
Screen=Tk()
Screen.title("GUI File Explorer")
Screen.geometry("500x500")
Screen.config(bg="lightblue")

OpenButton = Button(text="Open File",command=Open)
OpenButton.place(relx=0.3,rely=0.2)
SaveButton = Button(text="Save File",command=Save)
SaveButton.place(relx=0.6,rely=0.2)


CopyButton = Button(text="Copy File",command=Copy)
CopyButton.place(relx=0.3,rely=0.4)
RenameButton = Button(text="Rename File",command=Rename)
RenameButton.place(relx=0.6,rely=0.4)

MoveFileButton = Button(text="Move File",command=MoveFile)
MoveFileButton.place(relx=0.3,rely=0.6)
DeleteButton = Button(text="Delete File",command=Delete)
DeleteButton.place(relx=0.6,rely=0.6)


CreateFolderButton = Button(text="Create Folder",command=Rename)
CreateFolderButton.place(relx=0.3,rely=0.8)
DeleteFolderButton = Button(text="Delete Folder",command=DeleteFolder)
DeleteFolderButton.place(relx=0.6,rely=0.8)
mainloop()


'''Code Explanation:
a. title(): It sets the title of the main window.
b. geometry(): The dimensions of the window are set with this widget.
c. config(): It changes the property of the widget.
d. Button(): It adds the button on screen.
e. place(): It places the widget in the specific position of the screen.'''