import tkinter
# creating and removing a directory (folder), fetching its contents, changing
import os
from tkinter import *
#  used to display message boxes in your applications. 
from tkinter.messagebox import *
#provides classes and factory functions for creating file/directory selection windows.
from tkinter.filedialog import *
import webbrowser
from tkinter import filedialog
import winsound
import pickle
#import pygame



class Notepad:
    t = Tk()

    # default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(t)
    thisMenuBar = Menu(t)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    thisMusicMenu = Menu(thisMenuBar, tearoff=0)
    #thisSongMenu = Menu(thisMusicMenu, tearoff=0)
    thisColorMenu = Menu(thisMenuBar, tearoff=0)
    thisfontColorMenu = Menu(thisColorMenu, tearoff=0)
    # music
    t.filename=""
    t.playlist = []
    t.pauseFlag = False
    t.songAdded = False
    t.i = 0
    
    # Set icon
    t.wm_iconbitmap("notepad.ico")

    # To add scrollbar
    thisScrollBar = Scrollbar(thisTextArea)
    file = None
    

    def __init__(self, **kwargs):


        # Set the window text
        self.t.title("Untitled - Notepad 2.0")

        
        
        # For top and bottom
        self.t.geometry('500x500')

        # To make the textarea auto resizable
        self.t.grid_rowconfigure(0, weight=1)
        self.t.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.thisFileMenu.add_command(label="New",
                                        command=self.newFile)

        # To open a already existing file
        self.thisFileMenu.add_command(label="Open",
                                        command=self.openFile)

        # To save current file
        self.thisFileMenu.add_command(label="Save",
                                        command=self.saveFile)

        # To create a line in the dialog
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.thisMenuBar.add_cascade(label="File",
                                       menu=self.thisFileMenu)

        # To give a feature of cut
        self.thisEditMenu.add_command(label="Cut",
                                        command=self.cut)

        # to give a feature of copy
        self.thisEditMenu.add_command(label="Copy",
                                        command=self.copy)

        # To give a feature of paste
        self.thisEditMenu.add_command(label="Paste",
                                        command=self.paste)

        # To give a feature of editing
        self.thisMenuBar.add_cascade(label="Edit",
                                       menu=self.thisEditMenu)

        # To create a feature of description of the notepad
        self.thisHelpMenu.add_command(label="About Notepad 2.0",
                                        command=self.showAbout)
        self.thisMenuBar.add_cascade(label="Help",
                                       menu=self.thisHelpMenu)
#---------Creating Media----------

        '''self.thisMenuBar.add_cascade(label="Music",
                                       menu=self.thisMusicMenu)
        
        self.thisMusicMenu.add_command(label="Open",
                                       command=self.openMusic)
        self.thisMusicMenu.add_separator()
        self.thisMusicMenu.add_command(label="Play",
                                       command=self.playMusic)
        self.thisMusicMenu.add_separator()
        self.thisMusicMenu.add_command(label="Pause",
                                       command=self.pauseMusic)
        self.thisMusicMenu.add_separator()
        self.thisMusicMenu.add_command(label="Stop",
                                       command=self.stopMusic)
        self.thisMusicMenu.add_separator()
        self.thisMusicMenu.add_command(label="Next",
                                       command=self.nextMusic)
        self.thisMusicMenu.add_separator()
        self.thisMusicMenu.add_cascade(label="Song",
                                       menu=self.thisSongMenu)'''
        
# Color
        # To give a feature of red cplor
        
        self.thisColorMenu.add_command(label="Red",
                                        command=self.redColor)

        # to give a feature of blue color
        self.thisColorMenu.add_command(label="Blue",
                                        command=self.blueColor)

        # To give a feature of green color
        self.thisColorMenu.add_command(label="Green",
                                        command=self.greenColor)

        # To give a feature of Coloring
        self.thisMenuBar.add_cascade(label="Color",
                                       menu=self.thisColorMenu)
# font Color
        # To give a feature of cut
        self.thisfontColorMenu.add_command(label="Red",
                                        command=self.redFontColor)

        # to give a feature of copy
        self.thisfontColorMenu.add_command(label="Blue",
                                        command=self.blueFontColor)

        # To give a feature of paste
        self.thisfontColorMenu.add_command(label="Green",
                                        command=self.greenFontColor)

        # To give a feature of editing
        self.thisColorMenu.add_cascade(label="Font",
                                       menu=self.thisfontColorMenu)        
        

        self.t.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)

# Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

    def __quitApplication(self):
        self.t.destroy()

# exit()

    def showAbout(self):
        showinfo("Notepad 2.0", "Mancy🤗")

    def openFile(self):

        self.file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.t.title(os.path.basename(self.file) + " - Notepad 2.0")
            self.thisTextArea.delete(1.0, END)

            file = open(self.file, "r")

            self.thisTextArea.insert(1.0, file.read())

            file.close()

    def newFile(self):
        self.t.title("Untitled - Notepad 2.0")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def saveFile(self):

        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.t.title(os.path.basename(self.file) + " - Notepad 2.0")


        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):

# Run main application
        self.t.mainloop()
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#add music on notepad
# ---------Various Functions-------------
    '''def openMusic(self):
        try:
            self.songAdded = True
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select your cool music track",filetypes = (("mp3 Music Files","*.mp3"),("m4a Music Files","*.m4a")))
            playlist.append(self.filename)
            print(" Added " + self.filename)
            t.screenMessage.set("Good! Now Press on the Play Button")
        except:
            print("Cannot load the music")
            
    def playMusic():
        if(self.songAdded == False):
            t.screenMessage.set("First add some Music man!")
        else:
            try:
                if(t.pauseFlag == True):
                    pygame.mixer.music.unpause()
                else:
                    print("Playing")
                    pygame.mixer.init()
                    pygame.mixer.music.load(t.playlist[t.i])
                    pygame.mixer.music.play()
                    t.screenMessage.set("Playing " + t.playlist[t.i])
            except:
                print("Could not play the music")
    
    def pauseMusic(self):
        if(self.songAdded == False):
            self.screenMessage.set("First add some Music man!")
        else:
            try:
                pygame.mixer.music.pause()
                self.pauseFlag = True
                self.screenMessage.set("Paused")
            except:
                print("Cannot Pause the Music")
    
    def stopMusic(self):
        if(self.songAdded == False):
            self.screenMessage.set("First add some Music man!")
        else:
            pygame.mixer.music.fadeout(600)
            self.screenMessage.set("End of Playback!")
    
    def prevMusic(self):
        if(self.songAdded == False):
            self.screenMessage.set("First add some Music man!")
        else:
            try:
                if(self.playlist[self.i - 1]):
                    self.i -= 1
                    playMusic()
                else:
                    print("No previous songs")
                    self.screenMessage.set("No previous songs")
            except:
                stopMusic()
                print("No previous songs")
    
    def nextMusic(self):
        if(self.songAdded == False):
            self.screenMessage.set("First add some Music man!")
        else:
            try:
    
                if(self.playlist[self.i]):
                    self.i += 1
                    playMusic()
                else:
                    self.i -= 1
            except:
                self.screenMessage.set("End of Playback, Please add more songs")
    def end(self):
        t.destroy()'''

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def redColor(self):
        self.thisTextArea.config(bg='red')
        #self.thisTextArea = Text(self.t,bg='red')
    def blueColor(self):
        self.thisTextArea.config(bg='blue')
    def greenColor(self):
        self.thisTextArea.config(bg='green')
#font Color
    def redFontColor(self):
        self.thisTextArea.config(fg='red')
        #self.thisTextArea = Text(self.t,bg='red')
    def blueFontColor(self):
        self.thisTextArea.config(fg='blue')
    def greenFontColor(self):
        self.thisTextArea.config(fg='green')        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # Run main application

notepad = Notepad(width=600, height=400)
notepad.run() 
