from tkinter import *

window = Tk()

window.title("MusicDownloader")

window.geometry('')
window.bind('<Return>', exit)

def readAll():
    title.value = title.entry.get()
    artist.value = artist.entry.get()

class intro:
    row = 0
    version = 1.7
    label = Label(window, text="Music Downloader Version " + str(version))
intro.label.grid(column=0, row=intro.row)
blank = Label(window, text="")
blank.grid(column=0, row = intro.row+1)

class title:
    value = ""
    row = 2
    label = Label(window, text="Title:")
    entry = Entry(window,width=30)

title.label.grid(column=0, row=title.row)
title.entry.grid(column=0, row=title.row+1)

class artist:
    value = ""
    row = 4
    label = Label(window, text="Artist:")
    entry = Entry(window, width = 30)

artist.label.grid(column=0, row=artist.row)
artist.entry.grid(column=0, row=artist.row+1)

blank = Label(window, text="")
blank.grid(column=0, row=artist.row+3)

nextButton = Button(window, text="Next", command=readAll)
nextButton.grid(column=0, row=artist.row+4, sticky=SE)

window.mainloop()