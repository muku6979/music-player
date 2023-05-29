# importing libraries
import os   # import the os module for file system operations
from pygame import mixer  # import the mixer submodule from pygame
from tkinter import *  # import the tkinter module for GUI programming


def playsong():  # define a function for playing a song
  currentsong=playlist.get(ACTIVE)  # get the selected song from the playlist
  print(currentsong)  # print the name of the song in the console
  mixer.music.load(currentsong)  # load the selected song into the mixer
  songstatus.set("Playing")  # update the song status to "Playing"
  mixer.music.play()  # play the loaded song

def pausesong():  # define a function for pausing a song
  songstatus.set("Paused")  # update the song status to "Paused"
  mixer.music.pause()  # pause the currently playing song

def stopsong():   # Defining the function for stopping a song
  songstatus.set("Stopped")  # Setting the status of the song as "Stopped"
  mixer.music.stop()  # Stopping the current song

def resumesong():  # Defining the function for resuming a song
  songstatus.set("Resuming")  # Setting the status of the song as "Resuming"
  mixer.music.unpause()  # Resuming the current song

root=Tk()  # Creating the tkinter window
root.title('Music player')  # Setting the title of the window
mixer.init()  # Initializing the mixer module
songstatus=StringVar()  # Creating a string variable for the status of the song
songstatus.set("choosing")  # Setting the initial status of the song as "choosing"
playlist=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('optima',10),width=100,height=20)  # Creating a listbox for the playlist
playlist.grid(columnspan=20)  # Positioning the listbox in the tkinter window
os.chdir(r'c:\songs')  # Changing the current working directory to the directory containing the music files
songs=os.listdir()  # Getting the list of music files in the directory
for s in songs:
   playlist.insert(END,s)  # Adding each music file to the playlist

playbtn=Button(root,text="Play",command=playsong)   # Creates a button named "Play" with a command to play the song
playbtn.config(font=('italic',20),bg="white",fg="violet",padx=2,pady=0)   # Configures the button's font, background color, and text color
playbtn.grid(row=1,column=0)   # Displays the button at row 1 and column 0 in the GUI

pausebtn=Button(root,text="Pause",command=pausesong)   # Creates a button named "Pause" with a command to pause the song
pausebtn.config(font=('italic',20),bg="white",fg="yellow",padx=2,pady=0)   # Configures the button's font, background color, and text color
pausebtn.grid(row=1,column=1)   # Displays the button at row 1 and column 1 in the GUI

stopbtn=Button(root,text="Stop",command=stopsong)   # Creates a button named "Stop" with a command to stop the song
stopbtn.config(font=('italic',20),bg="white",fg="red",padx=2,pady=0)   # Configures the button's font, background color, and text color
stopbtn.grid(row=1,column=2)   # Displays the button at row 1 and column 2 in the GUI

Resumebtn=Button(root,text="Resume",command=resumesong)   # Creates a button named "Resume" with a command to resume the song
Resumebtn.config(font=('italic',20),bg="white",fg="blue",padx=2,pady=0)   # Configures the button's font, background color, and text color
Resumebtn.grid(row=1,column=3)   # Displays the button at row 1 and column 3 in the GUI

mainloop()   # Starts the event loop of the GUI, allowing user interaction with the buttons and listbox.